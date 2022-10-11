from tkinter.messagebox import QUESTION
from django.db import models

# IT 모델
class IT(models.Model):#디벨로퍼에 카운트가 들어가야하는 이유는 사실 딱히 없긴 하지만, 메인에서 보여줄때 연결하기 쉬우니..
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.major

class ITQuestion(models.Model): 
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length= 255)

    def __str__(self):
         return f'{self.number}. {self.question}'

class ITAnswer(models.Model):
    major = models.ForeignKey(IT, on_delete=models.CASCADE)
    question = models.ForeignKey(ITQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
#인문 model
class Humanity(models.Model):
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    #image = models.ImageField('image') 학과별 이미지
    
    def __str__(self):
        return self.major
    
class HumanityQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class HumanityAnswer(models.Model):
    major = models.ForeignKey(Humanity, on_delete=models.CASCADE)
    question = models.ForeignKey(HumanityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
#사회 model
class Society(models.Model):
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    #image = models.ImageField('image') 학과별 이미지

    def __str__(self):
        return self.major
    
class SocietyQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.number}. {self.question}'
    
class SocietyAnswer(models.Model):
    major = models.ForeignKey(Society, on_delete=models.CASCADE)
    question = models.ForeignKey(SocietyQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer
    
#미컨 model
class MediaContent(models.Model):
    major = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    #image = models.ImageField('image') 학과별 이미지
    
    def __str__(self):
        return self.major
    
class MediaContentsQuestion(models.Model):
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.number}. {self.question}'
    
class MediaContentsAnswer(models.Model):
    major = models.ForeignKey(MediaContent, on_delete=models.CASCADE)
    question = models.ForeignKey(MediaContentsQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer