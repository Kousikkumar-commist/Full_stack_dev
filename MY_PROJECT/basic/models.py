from django.db import models

class userdb(models.Model):
    name = models.CharField(max_length=255, null=True)
    mail = models.CharField(max_length=255, null=True)
    phno = models.CharField(max_length=255 ,null=True)  # IntegerField does not take max_length
    '''msg = models.CharField(max_length=255, null=True)'''

    class Meta:
        db_table = 'bio'  # Correct indentation
