from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    from_email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
		return self.name
    
    
