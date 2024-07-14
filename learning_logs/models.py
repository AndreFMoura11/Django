from django.db import models

# Create your models here.

class Topic( models.Model):
    """Um assunto sobre qual o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representção em sring do modelo"""
        return self.text

class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'entries'  # Quando for para usar palavras no plural em ENTRY

    def __str__(self):  
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...'