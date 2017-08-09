import hashlib
import random

from django.db import models

from taggit.managers import TaggableManager


class TimeStamped(models.Model):
    """
    Inherit this abstract model to provide self-updating created and modified
    field for your model
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(TimeStamped):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Food(TimeStamped):
    FOOD_TYPE = (
        ('F', 'Fruit'),
        ('V', 'Vegetable'),
    )
    name = models.CharField(max_length=250, unique=True)
    food_type = models.CharField(max_length=1, choices=FOOD_TYPE)

    def __str__(self):
        return self.name


class Employee(TimeStamped):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    _id = models.CharField(max_length=30, unique=True)
    company = models.ForeignKey(Company)
    guid = models.CharField(max_length=40, unique=True)
    has_died = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    picture_url = models.URLField()  # Discuss and store image in the server
    age = models.IntegerField()
    eye_color = models.CharField(max_length=25)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    username = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    about = models.TextField()
    registered = models.DateTimeField()
    tags = TaggableManager()
    greeting = models.CharField(max_length=250)
    friends = models.ManyToManyField('Employee')
    favorite_foods = models.ManyToManyField(Food)

    def save(self, *args, **kwargs):
        """
        We will get guid from the source json but if some data doesn't have
        guid create on our own
        """

        if not self.guid:
            self.guid = hashlib.sha1(str(random.random())).hexdigest()

        super(Employee, self).save(*args, **kwargs)

    def balance_aud(self):
        return "${}".format(self.balance)

    def get_tags(self):
        return [tag.name for tag in self.tags.all()]

    def get_favorite_fruits(self):
        return [fruit.name for fruit in self.favorite_foods.all() if
                fruit.food_type == 'F']

    def get_favorite_vegetables(self):
        return [veggie.name for veggie in self.favorite_foods.all() if
                veggie.food_type == 'V']

    def __str__(self):
        return self.name
