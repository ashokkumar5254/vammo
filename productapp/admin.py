from django.contrib import admin
from .models import category,product,session_model,cartitem,address

class category_admin(admin.ModelAdmin):
    model=category
    prepopulated_fields={'category_slug':('category_name',)}
    list_display=['category_name','category_slug']
admin.site.register(category,category_admin)
class product_admin(admin.ModelAdmin):
    model=product
    prepopulated_fields={'product_slug':('product_name',)}
    list_display=['product_name','product_price','product_slug']
admin.site.register(product,product_admin)
# Register your models here.
class session_admin(admin.ModelAdmin):
    model=session_model
    list_display=['session_id',]
admin.site.register(session_model,session_admin)
class cart_item(admin.ModelAdmin):
    model=cartitem
    list_display=['id','cart_session','cart_product']
admin.site.register(cartitem,cart_item)
class address_admin(admin.ModelAdmin):
    model=address
    list_display=['first_name','middle_name','last_name','village','distic','mandal']
admin.site.register(address,address_admin)