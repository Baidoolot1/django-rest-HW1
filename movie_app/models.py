from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)

