from django.shortcuts import render, redirect
from sqltest import onetest
import sqltest.onetest


# Create your views here.
def update_sql(request):
    db = onetest.DB()
    table_name = 'sign_guest'
    table_name1 = 'easy_agent_account'
    table_name2 = 'easy_agent'
    data = {'phone': 18768494086}
    data1 = {'balance': 6000000}
    db.select(table_name1, table_name2, data['phone'], data1['balance'])
    return render(request, 'migrations/index.html')

