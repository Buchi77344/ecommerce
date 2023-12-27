from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=234,db_index=True)
    slug = models.SlugField(max_length=234, unique=True)

    def get_absolute_url(self):
        return reverse ('product_de', args=[self.slug])

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=345)
    author = models.CharField(max_length=234, default='admin')
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=234)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    instock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    creatd  =models.DateTimeField(auto_now_add=True)
    updated  =models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_de',args=[self.slug])

    def __str__(self):
        return self.title

    



        
