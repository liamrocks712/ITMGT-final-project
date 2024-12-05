from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False) 

class BarberItem(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=255, blank=True)  # e.g., "Haircuts, Beard Trims"
    experience = models.IntegerField(default=0)  # Years of experience
    profile_picture = models.ImageField(upload_to='barbers/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name
    
    

class ServiceItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name  # Return the name of the service
    
class Appointment(models.Model):
    barber = models.ForeignKey(BarberItem, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceItem, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100, default='Unknown Client')  # Set a default value
    client_phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ('barber', 'date', 'time')  # Ensure no double bookings

    def __str__(self):
        return f"Appointment with {self.barber} on {self.date} at {self.time} for {self.service.name} with {self.client_name}"
    
class Appointment(models.Model):
    barber = models.ForeignKey(BarberItem, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceItem, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)  # Ensure this is present
    client_phone = models.CharField(max_length=20)  # Ensure this is present
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ('barber', 'date', 'time')  # Ensure no double bookings

    def __str__(self):
        return f"Appointment with {self.barber} on {self.date} at {self.time} for {self.service.name} with {self.client_name}"
