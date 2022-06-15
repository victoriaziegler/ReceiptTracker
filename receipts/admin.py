from django.contrib import admin
from receipts.models import ExpenseCategory, Receipt, Account

# Register your models here.


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


class ReceiptAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Account, AccountAdmin)
