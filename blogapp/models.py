from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)



class Blog(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', "Draft"
        Published = 'PB','Published'

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='blog_images')
    auth = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])



class MyBooks(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=60)
    about = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='books_images')
    stars = models.IntegerField()

    def __str__(self):
        return self.name





class AboutMe(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth = models.DateField()
    image = models.ImageField(upload_to='my_images')
    profession = models.CharField(max_length=25)
    motto = models.CharField(max_length=255)
    about_me = models.TextField()
    phone_number = models.CharField(max_length=30)
    instagram = models.CharField(max_length=60)
    telegram = models.CharField(max_length=60)
    email = models.EmailField()
    linkedin = models.CharField(max_length=60)

    def age(self):
        today = date.today()
        return today.year - self.birth.year - (
                    (today.month, today.day) < (self.birth.month, self.birth.day))



    def belgi(self):
        return self.about_me[0]


    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email



