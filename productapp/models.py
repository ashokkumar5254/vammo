from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=100)
    category_slug=models.SlugField(max_length=100)
    category_image=models.ImageField(upload_to='media')
    datetime=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='category'
        verbose_name_plural='category_content'
    def __str__(self):
        return self.category_name
    
class product(models.Model):
    category_product=models.ForeignKey(category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_slug=models.SlugField(max_length=100)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='media')
    stoke=models.IntegerField()
    is_avaliable=models.BooleanField(default=True)
    datetime=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='product'
        verbose_name_plural='product_content'
    def __str__(self):
        return self.product_name
class session_model(models.Model):
    session_id=models.CharField(max_length=500)
    date_time=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='session_model'
        verbose_name_plural='session'
    def __str__(self):
        return self.session_id
    
class cartitem(models.Model):
    cart_session=models.ForeignKey(session_model,on_delete=models.CASCADE)
    cart_product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    cart_price=models.IntegerField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='cartitem'
        verbose_name_plural='cart'
    def __str__(self):
        return self.cart_product.product_name
    
class address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    distic=models.CharField(max_length=100)
    mandal=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    pincode=models.IntegerField()
    street=models.CharField(max_length=100)
    class Meta:
        verbose_name='address'
        verbose_name_plural='address_content'
    def __str__(self):
        return self.village

