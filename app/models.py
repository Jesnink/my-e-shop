

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.


STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Goa','Goa'),
    ('Haryana','Haryana'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Tamil Nadu','Tamil Nadu')
    
)
class Customer(models.Model):
    Id=models.BigAutoField(
        primary_key=True
    )
    User=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    Name=models.CharField(
        max_length=50,
        verbose_name='Name'
        )
    Locality=models.CharField(
        max_length=200,
        verbose_name='Locality'
        )
    City=models.CharField(
        max_length=200,
        verbose_name='City'
        
    )
    ZipCode=models.IntegerField(

        verbose_name='ZipCode'
        )
    State=models.CharField(
        max_length=50,
        choices=STATE_CHOICES
        
    )
    def __str__(self):
        return str(self.Id)

CATEGORY_CHOICES=(
    ('MT','Men Top Wear'),
    ('MB','Men Bottom Wear'),
    ('WEC','Women Ethnic Churidar '),
    ('WES','Women Ethnic Saree '),
    ('WWT','Women Western Top'),
    ('WWB','Women Western Bottom'),
    ('WW','Women Western Wear'),
    ('MO','Mobile'),
    ('LA','Laptop')
    
)
class Product(models.Model):
    Id=models.BigAutoField(
        primary_key=True
    )
    Title=models.CharField(
        verbose_name='Title',
        max_length=200
        )
    Selling_price=models.FloatField(
        verbose_name='Selling Price'
        )
    Discounted_Price=models.FloatField()
    Descriptio=models.TextField (
        verbose_name='Description',
        
        )
    Brand=models.CharField(
        max_length=50,
        verbose_name='Brand',
       
        )
    Category=models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=5
        )
    
    Product_image=models.ImageField(upload_to='product_img')
    def __str__(self):
        return str(self.Id)

       
        
class Cart(models.Model):
    Id=models.BigAutoField(
        primary_key=True
    )
    User=models.ForeignKey(
        to=User,
        on_delete=CASCADE
       
    )
    Product=models.ForeignKey(
        to=Product,
        on_delete=CASCADE,
        
    )
    Quantity=models.PositiveIntegerField(default=1)  
    def __str__(self):
        return str(self.Id)

    @property
    def single_cart_cost(self):
        return self.Quantity * self.Product.Discounted_Price

STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
class Order(models.Model):
    Id=models.BigAutoField(
        primary_key=True
    )
    User=models.ForeignKey(
        to=User,
        on_delete=CASCADE
       
    )
    Product=models.ForeignKey(
        to=Product,
        on_delete=CASCADE,
    )
    Customer=models.ForeignKey(
        to=Customer,
        on_delete=CASCADE,
    )
    Quantity=models.PositiveIntegerField(default=1)
    Ordered_date=models.DateTimeField(auto_now_add=True)
    Status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    def __str__(self):
        return str(self.Id)
    @property
    def single_cart_cost(self):
        return self.Quantity * self.Product.Discounted_Price

        
    
    



    

   