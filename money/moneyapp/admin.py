from django.contrib import admin
from moneyapp.models import Statement

class StatementAdmin(admin.ModelAdmin):
    list_display=["name","amount","catagory"]
    list_per_page = 3
    list_editable=["amount","catagory"]
    list_filter=["catagory","amount"]
    search_fields=["name"]
    fields=["catagory","name","amount"]

# Register your models here.
admin.site.register(Statement,StatementAdmin)