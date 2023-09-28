from django.shortcuts import render
from django.http import HttpResponse
from moneyapp.models import Statement
from django.db.models import Sum

# Create your views here.
def index(request):
    total_income = Statement.objects.filter(catagory="income").aggregate(Sum("amount"))
    total_expense = Statement.objects.filter(catagory="expense").aggregate(Sum("amount"))
    return render(request, "index.html", {"income": total_income, "expense": total_expense})


def account(request):
    data=Statement.objects.all()
    return render(request,"account.html",{"data":data})
    