from django.views.generic import ListView, CreateView
from receipts.models import Account, ExpenseCategory, Receipt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from receipts.forms import CreateReceiptForm


# Create your views here.
class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "expense_categories/list.html"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "expense_categories/create.html"
    fields = ["name"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_categories")


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/create.html"
    fields = ["name", "number"]

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        return redirect("list_accounts")


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/create.html"
    form_class = CreateReceiptForm

    def get_form_kwargs(self):
        kwargs = super(ReceiptCreateView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        item = form.save(commit=False)
        item.purchaser = self.request.user
        item.save()
        return redirect("home")
