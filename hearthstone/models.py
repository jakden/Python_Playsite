from django.db import models

# Create your models here.
#class Card(models.Model):

	#mana_cost = models.CharField(max_length=200)
	#card_name = models.CharField(max_length=200) 

	#def __str__(self):
		#return self.card_name

class CardViewer(models.Model):
	
	mana = models.CharField(max_length=200)
	card = models.CharField(max_length=200) 
	card_attack = models.CharField(max_length=200)
	card_health = models.CharField(max_length=200)
	card_class = models.CharField(max_length=200)
	card_ability_1 = models.CharField(max_length=200)
	card_ability_2 = models.CharField(max_length=200)
	card_ability_3 = models.CharField(max_length=200)
	card_png = models.CharField(max_length=200)
	card_flavor_text = models.CharField(max_length=200)
	
	def __str__(self):
		return self.card

		