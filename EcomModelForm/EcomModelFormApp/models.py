from django.db import models

# Create your models here.


    
class Ecom(models.Model):
    customer=models.CharField(max_length=100,verbose_name="Name of customer",unique=True)
    Product= models.CharField(max_length=100, verbose_name="Product")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category  =  models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_no= models.CharField(max_length=15) 
    emailid= models.EmailField(max_length=100)

    def __str__(self):
        return self.customer

    class Meta:
	    db_table='EcomModelForm_Ecom'

   


