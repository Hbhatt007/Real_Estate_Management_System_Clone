from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class State(models.Model):
    statename = models.CharField(max_length=100, null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.statename

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    cityname = models.CharField(max_length=100, null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cityname

class PropertyType(models.Model):
    typename = models.CharField(max_length=100, null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.typename

class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=100, null=True)
    postingdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.first_name

class Property(models.Model):
    user = models.ForeignKey(UserType, on_delete=models.CASCADE)
    propertytitle = models.CharField(max_length=100, null=True)
    propertydescription = models.CharField(max_length=300, null=True)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    bedrooms = models.CharField(max_length=100, null=True)
    bathrooms = models.CharField(max_length=100, null=True)
    floors = models.CharField(max_length=100, null=True)
    garages = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100, null=True)
    rentorsaleprice = models.CharField(max_length=100, null=True)
    beforepricelabel = models.CharField(max_length=100, null=True)
    afterpricelabel = models.CharField(max_length=100, null=True)
    propertyid = models.CharField(max_length=100, null=True)
    centercooling = models.CharField(max_length=100, null=True)
    balcony = models.CharField(max_length=100, null=True)
    petfriendly = models.CharField(max_length=100, null=True)
    barbeque = models.CharField(max_length=100, null=True)
    firealarm = models.CharField(max_length=100, null=True)
    modernkitchen = models.CharField(max_length=100, null=True)
    storage = models.CharField(max_length=100, null=True)
    dryer = models.CharField(max_length=100, null=True)
    heating = models.CharField(max_length=100, null=True)
    pool = models.CharField(max_length=100, null=True)
    laundry = models.CharField(max_length=100, null=True)
    sauna = models.CharField(max_length=100, null=True)
    gym = models.CharField(max_length=100, null=True)
    elevator = models.CharField(max_length=100, null=True)
    dishwasher = models.CharField(max_length=100, null=True)
    emergencyexit = models.CharField(max_length=100, null=True)
    featuredimage = models.FileField(null=True,blank=True)
    galleryimage1 = models.FileField(null=True,blank=True)
    galleryimage2 = models.FileField(null=True,blank=True)
    galleryimage3 = models.FileField(null=True,blank=True)
    galleryimage4 = models.FileField(null=True,blank=True)
    galleryimage5 = models.FileField(null=True,blank=True)
    address = models.CharField(max_length=300, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=30, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    listingdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.propertytitle

class Enquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100, null=True)
    emailid = models.CharField(max_length=100, null=True)
    mobileno = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=500, null=True)
    enquiryno = models.CharField(max_length=50, null=True)
    enquirydate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=500, null=True)
    remarkdate = models.DateField(null=True)
    def __str__(self):
        return self.enquiryno

class Feedback(models.Model):
    user = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    userremark = models.CharField(max_length=500, null=True)
    postingdate = models.DateTimeField(auto_now_add=True)
    ispublish = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.id

