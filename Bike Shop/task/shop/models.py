from django.db import models


# write your models here
class Frame(models.Model):
    color = models.CharField(max_length=56)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color

    def decrease_quantity(self):
        self.quantity -= 1
        self.save()


class Seat(models.Model):
    color = models.CharField(max_length=56)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color

    def decrease_quantity(self):
        self.quantity -= 1
        self.save()


class Tire(models.Model):
    type = models.CharField(max_length=56)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type

    def decrease_quantity(self):
        self.quantity -= 2
        self.save()


class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.quantity)

    def decrease_quantity(self):
        self.quantity -= 1
        self.save()


class Bike(models.Model):

    name = models.CharField(max_length=56)
    description = models.TextField()
    has_basket = models.BooleanField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_available(self):
        if self.has_basket and Basket.objects.all().first().quantity < 1:
            return False
        if self.seat.quantity < 1:
            return False
        if self.frame.quantity < 1:
            return False
        if self.tire.quantity < 2:
            return False
        return True

    def decrease_quantity(self):
        self.frame.decrease_quantity()
        self.tire.decrease_quantity()
        self.seat.decrease_quantity()
        if self.has_basket:
            Basket.objects.all().first().decrease_quantity()


class Order(models.Model):
    name = models.CharField(max_length=56)
    surname = models.CharField(max_length=56)
    phone_number = models.CharField(max_length=56)
    status = models.CharField(max_length=10, choices=[('P', 'pending'), ('R', 'ready')])
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



