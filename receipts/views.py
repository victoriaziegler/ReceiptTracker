from django.views.generic import ListView
from receipts.models import Receipt
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)
