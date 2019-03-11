from django.db import models
from django.contrib.auth.models import User
import numpy as np
from django.db.models import Avg
from django.db.models import Count
from django.db.models import Sum

class Wine(models.Model):
    name = models.CharField(max_length=200)
    
    def average_rating(self):
        all_ratings = Review.objects.values('wine').annotate(Sum('rating'))
    #    print ("MAPFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", self.review_set.all()[0].rating)
    #    all_ratings = map(lambda x: x.rating, self.review_set.all())
    #    return self.review_set.aggregate(Avg('rating'))['rating__avg']
        return all_ratings
    #    return self.review_set.annotate(Count('rating'))['rating__avg']
        #return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
#    wine = models.ForeignKey(Wine)
    wine = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])
