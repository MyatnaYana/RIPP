from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=25)
    house = models.CharField(max_length=10)
    post_code = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='address_id')
    phone_number = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'customer'


class Mins(models.Model):
    id_min = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    origin = models.CharField(max_length=50)
    definition = models.CharField(max_length=255, blank=True, null=True)
    available = models.IntegerField()
    size = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mins'


class Reservation(models.Model):
    reserve_id = models.AutoField(primary_key=True)
    id_min = models.ForeignKey(Mins, models.DO_NOTHING, db_column='id_min')
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_id')
    reservation_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    sent_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reservation'
