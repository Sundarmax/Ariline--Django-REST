from django.db import models
# Create your models here.
# Model for Airline booking System.
class flight(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    airline_id = models.IntegerField()
    airline_name =  models.CharField(max_length=15)
    from_loc = models.CharField(max_length=20)
    to_loc = models.CharField(max_length=20)
    dep_time = models.TimeField()
    arrival_time = models.TimeField()
    duration = models.CharField(max_length=4)
    no_seats = models.IntegerField()

class flight_details(models.Model):
    flight_id = models.ForeignKey(flight,on_delete=models.CASCADE,null=True)
    flight_dep_date = models.DateField()
    price = models.IntegerField()
    avail_seats = models.IntegerField()

class passenger_info(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length = 15)
    firstname = models.CharField(max_length = 25)
    lastname = models.CharField(max_length = 25)
    address = models.CharField(max_length=50)
    tel_no = models.CharField(max_length = 20)
    email_id = models.EmailField()
class ticket_info(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    rofile_id = models.ForeignKey(passenger_info,on_delete=models.CASCADE,null=True)
    flight_id = models.ForeignKey(flight,on_delete=models.CASCADE,null=True)

class card_details(models.Model):
    profile_id = models.ForeignKey(passenger_info,on_delete=models.CASCADE,null=True)
    card_no = models.IntegerField()
    card_type = models.CharField(max_length=20)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField() 
