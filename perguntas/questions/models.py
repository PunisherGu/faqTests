from django.db import models

class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    answer = models.TextField()
    ordem = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='questions', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
            ordering = ('ordem',)
