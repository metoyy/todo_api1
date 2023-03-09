from django.db import models


# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.country} - {self.title}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Car(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='images')
    contacts = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} | {self.price} | {self.owner}'


class Musician(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(default=None, max_length=50, blank=True)

    def __str__(self):
        if self.nickname:
            return f'{self.nickname}'
        return f'{self.name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='songs')
    feat = models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True, related_name='feats', blank=True)
    poster = models.ImageField(upload_to='images/posters/')
    year = models.DateField()

    def __str__(self):
        if self.feat:
            return f'{self.author} - {self.title} feat {self.feat}'
        return f'{self.author} - {self.title}'


class Award(models.Model):
    import datetime

    @staticmethod
    def create_choice():
        from datetime import datetime
        YEAR_CHOICES = []
        for r in range(1980, (datetime.now().year + 1)):
            YEAR_CHOICES.append((r, r))
        return YEAR_CHOICES

    nominant = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='awards', unique=True)
    year = models.IntegerField('year', choices=create_choice())

    def __str__(self):
        return f'{self.nominant} - Golden Voice {self.year}'
