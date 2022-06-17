from django import forms
from receipts.models import Receipt, ExpenseCategory, Account


class CreateReceiptForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(CreateReceiptForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["category"].queryset = ExpenseCategory.objects.filter(
                owner=user
            )
            self.fields["account"].queryset = Account.objects.filter(
                owner=user
            )

    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]
