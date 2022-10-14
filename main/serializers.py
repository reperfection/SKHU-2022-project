from rest_framework import serializers
from .models import IT, ITQuestion, ITAnswer , IT_QnA
from .models import Humanity, HumanityQuestion, HumanityAnswer , Humanity_QnA
from .models import Society, SocietyQuestion, SocietyAnswer , Society_QnA
from .models import MediaContent, MediaContentsAnswer, MediaContentsQuestion, MediaContentsAnswer , MediaContents_QnA

class ITSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT
        fields ='__all__' #라우팅을 시리얼라이즈에서 도와줌을로 서 API구현을 쉽게 해준다.

class ITQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITQuestion
        fields = ['number', 'question']

class ITAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITAnswer
        fields = ['answer', 'major', 'question']

class IT_QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_QnA
        fields = ('title','body' ,'name')

class HumanitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humanity
        fields ='__all__' #라우팅을 시리얼라이즈에서 도와줌을로 서 API구현을 쉽게 해준다.

class HumanityQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanityQuestion
        fields = ['number', 'question']

class HumanityAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanityAnswer
        fields = ['answer', 'major', 'question']

class Humanity_QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = Humanity_QnA
        fields = ('humanity_title','humanity_body' ,'humanity_name')

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields ='__all__' #라우팅을 시리얼라이즈에서 도와줌을로 서 API구현을 쉽게 해준다.

class SocietyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyQuestion
        fields = ['number', 'question']

class SocietyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyAnswer
        fields = ['answer', 'major', 'question']

class Society_QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = Society_QnA
        fields = ('society_title','society_body' ,'society_name')

class MediaContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContent
        fields = 'all'

class MediaContentsQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContentsQuestion
        fields = ['number', 'question']

class MediaContentsAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContentsAnswer
        fields = ['answer', 'major', 'question']

class MediaContentsQnASerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContents_QnA
        fields = ['mediaContents_title', 'mediaContents_body', 'mediaContents_name']
