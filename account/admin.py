from django.contrib import admin


from .models import *

# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name_ar','name_en','type','email',)
    list_filter = ('type','created_by','update_by','created','update')
    search_fields = ['name_ar','name_en','email']
  
admin.site.register(Project,ProjectAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id','place','adderss','project','email',)
    list_filter = ('project','created_by','update_by','created','update')
    search_fields = ['place','adderss','email']
  
admin.site.register(Branch,BranchAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','name','group','hb','lb','balance',)
    list_filter = ('type','created_by','update_by','created','update','group',)
    search_fields = ['name','branch','adderss']

admin.site.register(Account)
admin.site.register(TypePro)
admin.site.register(Company)
admin.site.register(Store)
admin.site.register(Unit)
admin.site.register(Currency)
admin.site.register(Exchange)
admin.site.register(ProjectPower)
admin.site.register(T1)
admin.site.register(T2)
class ProducttAdmin(admin.ModelAdmin):
    list_display = ('id','name','group','ha','la','balance',)
    list_filter = ('type','created_by','update_by','created','update''group',)
    search_fields = ['name','branch','adderss']

admin.site.register(Product)

class OrderItemAdmin(admin.TabularInline):

    model = OrderItem


class OrdertAdmin(admin.ModelAdmin):
    list_display = ('id','note','total_price','type','creditor','debitor','currency',)
    list_filter = ('type','created_by','update_by','created','update','creditor','debitor','currency',)
    search_fields = ['creditor','debitor','note']
    inlines = [
	OrderItemAdmin,
	]
admin.site.register(Order,OrdertAdmin)


