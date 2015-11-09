from django.db import models

# Create your models here.
class Family(models.Model):
	family_name = models.CharField(max_length=40)
	def __str__(self):
		return self.family_name

class Person(models.Model):
	name = models.CharField(max_length=100, default="NoName")
	family = models.ForeignKey(Family)
	gift_preference = models.CharField(max_length=200)
	def __str__(self):
		return self.name


class Gifts(models.Model):
	gifter = models.ForeignKey(Person, related_name="giver")
	giftee = models.ForeignKey(Person, related_name="receiver")
	def __str__(self):
		return str(self.gifter) + "-->" + str(self.giftee)


