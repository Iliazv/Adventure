from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=1500)
    date = models.DateTimeField('Published')

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=120)
    price = models.CharField(max_length=20)
    description = models.TextField()
    rating = models.CharField(max_length=10)
    stars = models.IntegerField(default=0)
    main_image = models.ImageField(upload_to = 'tour_images/', blank = True, default='')
    feeding = models.CharField(max_length=50, default='Нет')
    country = models.CharField(max_length=60, default='')

    INCLUDE_CHOICES = (
        ('YES', 'Yes'),
        ('NOT', 'Not') 
        
    )

    fly_include = models.CharField(max_length=50, choices=INCLUDE_CHOICES, default='NOT')

    def __str__(self):
        return self.name

class Image(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to = 'tour_images/', blank = True)

    def __str__(self): 
        return self.tour.name

class Response(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='responses')
    user_name = models.CharField(max_length=100)
    user_text = models.TextField(max_length=2000)
    rate = models.IntegerField()

    def __str__(self):
        return self.user_name