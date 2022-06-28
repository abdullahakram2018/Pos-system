
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify

# Create your models here.

class TypePro(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_typepro_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_typepro_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
    
def customer_photo_directory(instance, filename):
    return 'customers/{0}_{1}'.format(instance.id, instance.name)


class Project(models.Model):
    name_ar = models.CharField(max_length=190, null=True)
    name_en = models.CharField(max_length=190, null=True)
    address_ar = models.CharField(max_length=190, null=True)
    address_en = models.CharField(max_length=190, null=True)
    logo = models.ImageField(blank=True, null=True)
    start = models.CharField(max_length=190, null=True)
    type = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    note_ar = models.TextField(null=True)
    note_en = models.TextField(null=True)
    email = models.CharField(max_length=190, null=True)
    phone = models.CharField(max_length=20, null=True)
    tele = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=190, null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_project_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_project_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    def __str__(self):
        return self.name_ar

class Branch(models.Model):
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)
    place =  models.CharField(max_length=190)
    adderss = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, null=True)
    tele = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=190, null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_branch_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_branch_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)
    def __int__(self):
        return self.pk
 
  
    
    
class Account(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    type = models.ForeignKey(TypePro,on_delete=models.SET_NULL,null=True)
    hb = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    lb = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    balance = models.DecimalField(max_digits=6, decimal_places=0)
    trname = models.CharField(max_length=200,null=True)
    photo = models.ImageField(upload_to=customer_photo_directory, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    username = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='leaves')
    note = models.TextField(null=True)
    adderss = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20, null=True)
    tele = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    web = models.CharField(max_length=190, null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_account_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_account_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
    
    
class Company(models.Model):
    name = models.CharField(max_length=190)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_company_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_company_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
class Store(models.Model):
    name = models.CharField(max_length=190,null=True)
    place = models.CharField(max_length=190,null=True)
    tele = models.CharField(max_length=190,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_store_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_store_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
    

    


    
class Unit(models.Model):
    group = models.CharField(max_length=190)
    name = models.CharField(max_length=190)
    type = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_unit_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_unit_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=190)
    group = models.CharField(max_length=190)
    type = models.ForeignKey(TypePro, null=True, on_delete=models.SET_NULL)
    company_item = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True)
    balance = models.DecimalField(max_digits=6, decimal_places=0)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    package = models.FloatField(null=True)
    la = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    ha = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    puprice = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    sprice = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_produt_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_product_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    
class Currency(models.Model):
    name = models.CharField(max_length=190)
    code = models.CharField(max_length=3,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_currency_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_currency_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    

class Exchange(models.Model):
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_exchange_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_exchange_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.price
    
class Order(models.Model):
    #البيان او الملاحضات
    note = models.TextField(null=True)
    #قيمة الفاتورة او الحركة
    total_price = models.FloatField(  default=0 ,null=True)
    #تاريخ الحركة
    date = models.DateField(null=True)
    #  الدائن
    creditor = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='creditor_order_set')
    #  المدين
    debitor = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='debitor_order_set')
    #رقم المالية او الفاتورة او المستند
    finance = models.CharField(max_length=190,null=True)
    #اعتماد الحركة او تاكيده
    success = models.BooleanField(default=False)
    # نوع الحركة
    type = models.ForeignKey(TypePro,on_delete=models.SET_NULL,null=True)
    # عمولة الحركة
    currency = models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True,related_name='currency_order_set')
    #المرفقات
    attached = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    #الفرع
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_order_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_order_set')
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return 'Order {0}'.format(self.id)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0,null=True)
    stors = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)
    attached = models.IntegerField(null= True)
    note = models.TextField(null=True)
    success = models.BooleanField(default=False, null=True)
    attached = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None, null=True)


class ProjectPower(models.Model):
    user = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True) 
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True) 
    created_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='created_by_projectpower_set')
    update_by = models.ForeignKey(User, null=True,auto_created=True, on_delete=models.SET_NULL,related_name='update_by_projectpower_set')
   

class T1(models.Model):
    name1 = CharField(max_length=3,null=True)
    a = CharField(max_length=3,null=True)
    
class T2(models.Model):
    name2 = CharField(max_length=3,null=True)
    name = models.ForeignKey(T1,on_delete=models.SET_NULL,null=True) 
  
