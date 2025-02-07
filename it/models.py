from django.db import models

# Create your models here.
# IT 모델
class IT(models.Model):
    major = models.CharField(max_length=100)

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

#영어
class IT_eng(models.Model):
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.major

class ITQuestion_eng(models.Model): 
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length= 255)

    def __str__(self):
         return f'{self.number}. {self.question}'

class ITAnswer_eng(models.Model):
    major = models.ForeignKey(IT_eng, on_delete=models.CASCADE)
    question = models.ForeignKey(ITQuestion_eng, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer

#중국어
class IT_ch(models.Model):
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.major

class ITQuestion_ch(models.Model): 
    number = models.IntegerField(unique=True)
    question = models.CharField(max_length= 255)

    def __str__(self):
         return f'{self.number}. {self.question}'

class ITAnswer_ch(models.Model):
    major = models.ForeignKey(IT_ch, on_delete=models.CASCADE)
    question = models.ForeignKey(ITQuestion_ch, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.answer

    
class ITRequirement(models.Model):
    major = models.ForeignKey(IT, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=255)
    ENGrequirement = models.CharField(max_length=255)
    CNrequirement = models.CharField(max_length=255)
    
    def __str__(self):
        return self.requirement
    
class ITLearning(models.Model):
    major = models.ForeignKey(IT, on_delete=models.CASCADE)
    learning = models.CharField(max_length=255)
    ENGlearning = models.CharField(max_length=255)
    CNlearning = models.CharField(max_length=255)
    
    def __str__(self):
        return self.learning