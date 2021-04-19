from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.
class Questions(models.Model):
    questions_text=models.TextField(max_length=1000,db_index=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    answer=models.OneToOneField('Answer',on_delete=models.PROTECT,null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=True)
    class Meta:
        ordering = ['user']
    def get_absolute_url(self):
        return reverse('guide-detail', args=[str(self.id)])
    def __str__(self):
        return self.questions_text
class Answer(models.Model):
    answer_text=models.TextField(max_length=1000,db_index=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.answer_text
class Category(models.Model):
    category_text=models.CharField(max_length=100,db_index=True)
    def __str__(self):
        return self.category_text
class Comment(models.Model):
    сomment_text=models.TextField(max_length=200,db_index=True,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    questions=models.ForeignKey('Questions',on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.сomment_text


# Create your models here.
