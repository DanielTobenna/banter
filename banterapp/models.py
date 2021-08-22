from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name= models.CharField(max_length=200, null=True)
	phone= models.CharField(max_length=200, null=True)
	email= models.CharField(max_length=200, null=True)
	Wallet_address= models.CharField(max_length=400, null=True)
	profile_pic= models.ImageField(default='profile_pic.PNG',null=True, blank=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

	@property
	def profile_picUrl(self):
		try:
			url= self.profile_pic.url
		except:
			url=''
		return url

class Investment(models.Model):
	customer= models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
	deposite= models.FloatField(default=0, null=True)
	balance= models.FloatField(default=0,null=True)
	withdrawal= models.FloatField(default=0,null=True)
	profit= models.FloatField(default=0,null=True)

	def __str__(self):
		return self.customer.name


class Plan(models.Model):
	name= models.CharField(max_length=200, null=True, blank=True)
	description= models.CharField(max_length=2000, null=True, blank=True)
	max_deposite= models.FloatField(null=True)
	min_deposite= models.FloatField(null=True)
	image= models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url= self.image.url
		except:
			url= ''
		return url

class Product(models.Model):
    product_id= models.CharField(max_length=50, null=True, blank=True)
    title=models.CharField(max_length=200,  null=True, blank=True)
    plan_name= models.CharField(max_length=200,  null=True, blank=True)
    price= models.FloatField()
    customer= models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.plan_name

class Invoice(models.Model):
    STATUS_CHOICES = ((-1,"Not Started"),(0,'Unconfirmed'), (1,"Partially Confirmed"), (2,"Confirmed"))
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=-1)
    order_id = models.CharField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)
    btcvalue = models.IntegerField(blank=True, null=True)
    received = models.IntegerField(blank=True, null=True)
    txid = models.CharField(max_length=250, blank=True, null=True)
    rbf = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.address
