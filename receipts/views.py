from django.views.generic import ListView
from receipts.models import Receipt


# Create your views here.


class ReceiptListView(ListView):
    model = Receipt
    template_name = "receipts/list.html"
