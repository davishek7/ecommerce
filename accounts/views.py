from django.shortcuts import render,redirect
from .forms import CreateUserForm,CustomerForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib import messages
from store.models import *
from .decorators import unauthenticated_user,allowed_users,admin_only

@unauthenticated_user
def register(request):

	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,'Your Account has been created! You can now login.')
			return redirect('login')
	else:
		form=CreateUserForm()
	context={'form':form}
	return render(request,'accounts/register.html',context)

@login_required
def logoutUser(request):
	logout(request)
	return render(request,'accounts/logout.html')

@allowed_users(allowed_roles=['customer'])
def profile(request):
	customer=request.user.customer
	order,created=Order.objects.get_or_create(customer=customer,complete=False)
	items=order.orderitem_set.all()
	cartItems=order.get_cart_items
	form=CustomerForm()
	context={'form':form,'cartItems':cartItems}
	return render(request,'accounts/customer_profile.html',context)

@allowed_users(allowed_roles=['customer'])
def orders(request):
	context={}
	return render(request,'accounts/customer_order.html',context)

@admin_only
def dashboard(request):
	orders=Order.objects.all()
	customers=User.objects.filter(groups=2)
	items=OrderItem.objects.all()
	total_orders=orders.count()
	context={'orders':orders,'customers':customers,'total_orders':total_orders,'items':items}
	return render(request,'accounts/dashboard.html',context)
