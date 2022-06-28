from django.forms.models import inlineformset_factory, modelformset_factory 
from django.shortcuts import redirect, render 
import json
from account.forms import  OrderForm, OrderItemForm
from account.models import *

from django.forms import formset_factory, inlineformset_factory
from django.db import transaction, IntegrityError







# Create your views here.
def entry_create(request):
    
    typepro = TypePro.objects.get(name='فرعي')
    branchuser = ProjectPower.objects.get(user=request.user)
    barnch = Branch.objects.get(pk=branchuser.branch)
    account = Account.objects.all().filter(type=typepro,branch=barnch)
    currency = Currency.objects.all().filter(branch=barnch)
    product = Product.objects.all().filter(type=typepro,branch=barnch,)
    store = Store.objects.all().filter(branch=barnch)
    unit = Unit.objects.all().filter(type=typepro,)
    creditor = Account.objects.get(name="مبيعات",branch=barnch)
    context = {'product':product,'account':account,'currency':currency,'unit':unit,}
    if request.method == "POST":
        if request.POST.get('note')  :
            #total_price =sum(request.POST.get('qty') * request.POST.get('price'))
            if request.POST.get('currency') is not None:
                currency = Currency.objects.get(pk=request.POST.get('currency'))
                
            else:
                currency = Currency.objects.get(name='يمني')

            if request.POST.get('debitor') is not None:
                debitor = Account.objects.get(pk=request.POST.get('debitor')) 
                type = TypePro.objects.get(name='مبيعات اجله')
            else:
                debitor = Account.objects.get(username=request.user)
                type = TypePro.objects.get(name='مبيعات نقدية')

            order = Order.objects.create(
                note=request.POST.get('note'),
                finance=request.POST.get('finance'),
                #total_price=total_price,
                currency=currency,
                creditor=creditor,
                debitor=debitor,
                branch=barnch,
                created_by=request.user,
                success=True,
                type=type)
            producti = Product.objects.get(pk=request.POST.get('product'))
            uniti = Unit.objects.get(pk=request.POST.get('unit'))
            orderitem = OrderItem(success = True,
                    order=order,
                    note=request.POST.get('notei'),
                    product=producti,
                    unit=uniti,
                    quantity=request.POST.get('qty'),
                    price=request.POST.get('price'),
                    ).save()
                       
  
    
    return render(request,'entry/entry-create.html',context)

def entry_list(request):
    branchuser = ProjectPower.objects.get(user=request.user)
    branch = Branch.objects.get(pk=branchuser.branch)
    ordera = Order.objects.all().filter(branch=branch,created_by=request.user)
    products = Product.objects.all().filter(branch=branch)
    context = {'products':products}
    return render(request,'entry/entry.html',context)

def add_create(request):
    orderformset = inlineformset_factory(T1,T2,fields=('a','name1'))
    formset = orderformset(queryset = T1.objects.none())
    if request.method == 'POST':
        formset = orderformset(request.POST)
        if formset.is_valid():
            formset.save()
        
        
    context = {'formset':formset}
    return render(request,'create.html',context)

def create1(request): 
    typepro = TypePro.objects.get(name='فرعي')
    branchuser = ProjectPower.objects.get(user=request.user)
    barnch = Branch.objects.get(pk=branchuser.branch)
    product = Product.objects.all().filter(type=typepro,branch=barnch,)
    unit = Unit.objects.all().filter(type=typepro,)
    order = Order.objects.get(pk=150)
    orderietm = inlineformset_factory(Order,OrderItem,fields=('note','price','quantity','product','unit'),can_delete=True)
    if request.method == 'POST':
        formset = orderietm(request.POST,instance=order)
        if formset.is_valid():
            formset.save()
        return redirect('create')
    
    formset = orderietm(instance=order)
    context = {'product':product,'unit':unit,'formset':formset}
    #context = {'formset':formset}

    return render(request , 'create.html', context )

def create(request):
	context = {}
	MarksFormset = modelformset_factory(OrderItem, form=OrderItemForm,extra=3)	
	form = OrderForm(request.POST or None)
	formset = MarksFormset(request.POST or None, queryset= OrderItem.objects.none(), prefix='OrderItems')
	if request.method == "POST":
		if form.is_valid() and formset.is_valid():
			try:
				with transaction.atomic():
					student = form.save(commit=False)
					student.save()

					for mark in formset:
						data = mark.save(commit=False)
						data.student = student
						data.save()
			except IntegrityError:
				print("Error Encountered")

			return redirect('/')


	context['formset'] = formset
	context['form'] = form
	return render(request, 'create.html', context)
def dashboard(request):
    return render(request, 'billing/dashboard.html')

def billing(request):
    if request.method == 'GET':
        typepro = TypePro.objects.get(name='فرعي')
        branchuser = ProjectPower.objects.get(user=request.user)
        barnch = Branch.objects.get(pk=branchuser.branch)
        account = Account.objects.all().filter(type=typepro,branch=barnch)
        accountuser = Account.objects.get(username=request.user)
        return render(request, 'billing/billing.html',{'account':account,'accountuser':accountuser})
    else:
        accountuser = Account.objects.get(username=request.user)
        cid = request.POST.get('customerID', None)
        if cid is None:
            cid = accountuser.id
            
        else:
            cid = request.POST.get('customerID', None)
        customer = Account.objects.get(pk=cid)
        
        products = list(Product.objects.all())
        # context = { 'cust' : customer.identity,
        #             'name' : customer.name,
        #             'balance' : customer.balance,
        #             'products': products, }
        return render(request, 'billing/billing_details.html', {'customer': customer, 'products': products})

def sales_bill(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        typepro = TypePro.objects.get(name='فرعي')
        branchuser = ProjectPower.objects.get(user=request.user)
        barnch = Branch.objects.get(pk=branchuser.branch)
        account = Account.objects.all().filter(type=typepro,branch=barnch)
        currency = Currency.objects.all().filter(branch=barnch)
        currency_defult = Currency.objects.get(name='يمني')
        product = Product.objects.all().filter(type=typepro,branch=barnch,)
        store = Store.objects.get(branch=barnch,name='الرئيسي')
        unit = Unit.objects.all().filter(type=typepro,)
        creditor = Account.objects.get(name="مبيعات",branch=barnch)
        
        
        customer = Account.objects.get(pk=data['customer_id'])
        if customer is None:
            customer = Account.objects.get(username=request.user)
            type = TypePro.objects.get(name='مبيعات نقدية')
        else:
            customer = Account.objects.get(pk=data['customer_id'])
            type = TypePro.objects.get(name='مبيعات اجله')
        order = Order.objects.create(creditor=creditor,debitor=customer,total_price=data['total_price'],success=False,note="مبيعات",type=type,branch=barnch,created_by=request.user,currency=currency_defult)
        for product_id in data['product_ids']:
            product =Product.objects.get(pk=product_id)
            unit = Unit.objects.get(name=product.unit)
            OrderItem(product=Product.objects.get(pk=product_id),stors=store, order=order,quantity=1,price=product.price,unit=unit).save()
            customer.balance -= int(data['total_price'])
            customer.save()
            order.success = True
        order.save()
        return render(request, 'billing/order.html', {'success' : order.success})

def sales_bill_pdf(request):
    branchuser = ProjectPower.objects.get(user=request.user)
    barnch = Branch.objects.get(pk=branchuser.branch)
    project = Project.objects.get(pk=barnch.project.id)
    order = Order.objects.get(pk=277)
    orderItem = order.orderitem_set.all()
  

    context = {'project':project,'barnch':barnch,'order':order,'orderItem':orderItem}
    return render(request, 'billing/sales_bill.html' ,context)

def purchases_bill(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        typepro = TypePro.objects.get(name='فرعي')
        branchuser = ProjectPower.objects.get(user=request.user)
        barnch = Branch.objects.get(pk=branchuser.branch)
        account = Account.objects.all().filter(type=typepro,branch=barnch)
        currency = Currency.objects.all().filter(branch=barnch)
        currency_defult = Currency.objects.get(name='يمني')
        currency_defult = Currency.objects.get(name='يمني')
        product = Product.objects.all().filter(type=typepro,branch=barnch,)
        store = Store.objects.get(branch=barnch,name='الرئيسي')
        unit = Unit.objects.all().filter(type=typepro,)
        creditor = Account.objects.get(name="مبيعات",branch=barnch)
        
        
        customer = Account.objects.get(pk=data['customer_id'])
        if customer is None:
            customer = Account.objects.get(username=request.user)
            type = TypePro.objects.get(name='مبيعات نقدية')
        else:
            customer = Account.objects.get(pk=data['customer_id'])
            type = TypePro.objects.get(name='مبيعات اجله')
        order = Order.objects.create(creditor=creditor,debitor=customer,total_price=data['total_price'],success=False,note="مبيعات",type=type,branch=barnch,created_by=request.user,currency=currency_defult)
        for product_id in data['product_ids']:
            product =Product.objects.get(pk=product_id)
            unit = Unit.objects.get(name=product.unit)
            OrderItem(product=Product.objects.get(pk=product_id),stors=store, order=order,quantity=1,price=product.price,unit=unit).save()
            customer.balance -= int(data['total_price'])
            customer.save()
            order.success = True
        order.save()
        return render(request, 'billing/order.html', {'success' : order.success})

def order_try(request):
    if request.method == "POST":
        Orders=formset_factory(OrderForm,extra=3)
        formset=Orders(request.POST)
        if formset.is_valid():
            for form in formset:
                note=form.cleaned_data.get('note')
                creditor=form.cleaned_data.get('creditor')
                debitor=form.cleaned_data.get('debitor')
                finance=form.cleaned_data.get('finance')
                if note:
                    Order.objects.create(note=note,creditor=creditor,debitor=debitor,finance=finance).save()
                return redirect(dashboard)
    else:
        Orders=formset_factory(OrderForm,extra=3)
        formset=Orders()
        return render(request,"order.html",{'formset':formset})

def createMu(request):
	context = {}
	MarksFormset = modelformset_factory(OrderItem, form=OrderItemForm)	
	form = OrderForm(request.POST or None)
	formset = MarksFormset(request.POST or None, queryset= OrderItem.objects.none(), prefix='OrderItem')
	if request.method == "POST":
		if form.is_valid() and formset.is_valid():
			try:
				with transaction.atomic():
					student = form.save(commit=False)
					student.save()

					for mark in formset:
						data = mark.save(commit=False)
						data.order = student
						data.save()
			except IntegrityError:
				print("Error Encountered")

			return redirect('dashboard')


	context['formset'] = formset
	context['form'] = form
	return render(request, 'multi_forms/create1.html', context)

