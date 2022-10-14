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

class IT_QnA(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.title

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

class Humanity_QnA(models.Model):
    humanity_title = models.CharField(max_length=100)
    humanity_body = models.TextField()
    humanity_name = models.CharField(max_length=10)

    def __str__(self):
        return self.humanity_title
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

class Society_QnA(models.Model):
    society_title = models.CharField(max_length=100)
    society_body = models.TextField()
    society_name = models.CharField(max_length=10)

    def __str__(self):
        return self.society_title
    
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

class MediaContents_QnA(models.Model):
    mediaContents_title = models.CharField(max_length=100)
    mediaContents_body = models.TextField()
    mediaContents_name = models.CharField(max_length=10)

    def __str__(self):
        return self.mediaContents_title