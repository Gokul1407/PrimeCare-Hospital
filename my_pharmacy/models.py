from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.CharField(unique=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.category_name
    


class Products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_img = models.ImageField(upload_to='picture')
    product_price = models.IntegerField(default=0)
    product_description = models.TextField(null=True)
    product_stock = models.IntegerField(default=0)
    product_is_available = models.BooleanField(default=False)
    product_modified_date = models.DateTimeField(auto_now_add=True)
    product_expiry_date = models.DateField() 

    def __str__(self):
        return self.product_name    