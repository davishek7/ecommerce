from django.shortcuts import render

def accounts(request):
    context={}
    return render(request,'accounts/accounts.html',context)
