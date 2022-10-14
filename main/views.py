from django.shortcuts import render
from .models import IT, ITAnswer, ITQuestion ,IT_QnA
from .models import Humanity , HumanityQuestion , HumanityAnswer, Humanity_QnA
from .models import Society, SocietyQuestion, SocietyAnswer  , Society_QnA
from .models import MediaContent, MediaContentsAnswer, MediaContentsQuestion, MediaContentsAnswer ,MediaContents_QnA
from .serializers import ITSerializer , ITQuestionSerializer , ITAnswerSerializer , IT_QnASerializer
from .serializers import HumanitySerializer , HumanityQuestionSerializer , HumanityAnswerSerializer , Humanity_QnASerializer
from .serializers import SocietySerializer , SocietyQuestionSerializer , SocietyAnswerSerializer, Society_QnASerializer
from .serializers import MediaContentsSerializer , MediaContentsQuestionSerializer , MediaContentsAnswerSerializer , MediaContentsQnASerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response()
    
@api_view(['GET'])
def itTest(request, id):
    question = ITQuestion.objects.get(id=id)
    answers = ITAnswer.objects.filter(question_id=id)

    serializer = {
        'Qserializer' : ITQuestionSerializer(question).data,
        'Aserializer' : ITAnswerSerializer(answers, many=True).data,
    }
    
    return Response(serializer)

@api_view(['GET'])
def itSubmit(request): 
    # 문항 수
    N = ITQuestion.objects.count()
    # 개발자 유형 수
    K = IT.objects.count()
    # 개발유형마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)  
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
    it_major_id = max(range(1, K + 1), key=lambda id: counter[id])
    it_major_id = IT.objects.get(pk=it_major_id)
    it_major_id.count += 1
    it_major_id.save()
    
    itresult_major_id = it_major_id
    serializer = ITSerializer(itresult_major_id)
    return Response(serializer.data)

@api_view(['GET'])
def itResult(request, major_id):
    major = IT.objects.get(id=major_id)
    serialize = ITSerializer(major)
    return Response(serialize.data)

#Generic CBV (Class Based Views) 의 상속으로 코드 간결화 가능
class IT_QnA(generics.ListCreateAPIView):#CR가능
    queryset = IT_QnA.objects.all()
    serializer_class = IT_QnASerializer


@api_view(['GET'])
def humanityTest(request, id):
    humanity_question = HumanityQuestion.objects.get(id=id)
    humanity_answers = HumanityAnswer.objects.filter(question_id=id)

    serializer = {
        'Qserializer' : HumanityQuestionSerializer(humanity_question).data,
        'Aserializer' : HumanityAnswerSerializer(humanity_answers, many=True).data,
    }
    
    return Response(serializer)

@api_view(['GET'])
def humanitySubmit(request): 
    # 문항 수
    N = HumanityQuestion.objects.count()
    # 개발자 유형 수
    K = Humanity.objects.count()
    # 개발유형마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)  
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
    humanity_major_id = max(range(1, K + 1), key=lambda id: counter[id])
    humanity_major_id = IT.objects.get(pk=humanity_major_id)
    humanity_major_id.count += 1
    humanity_major_id.save()
    
    humanityresult_major_id = humanity_major_id
    serializer = HumanitySerializer(humanityresult_major_id)
    return Response(serializer.data)

@api_view(['GET'])
def humanityResult(request, major_id):
    major = Humanity.objects.get(id=major_id)
    serialize = HumanitySerializer(major)
    return Response(serialize.data)

#Generic CBV (Class Based Views) 의 상속으로 코드 간결화 가능
class Humanity_QnA(generics.ListCreateAPIView):#CR가능
    queryset = Humanity_QnA.objects.all()
    serializer_class = Humanity_QnASerializer

#사회
@api_view(['GET'])
def societyTest(request, id):
    question = SocietyQuestion.objects.get(id=id)
    answers = SocietyAnswer.objects.filter(question_id=id)

    serializer = {
        'Qserializer' : SocietyQuestionSerializer(question).data,
        'Aserializer' : SocietyAnswerSerializer(answers, many=True).data,
    }

    return Response(serializer)

@api_view(['GET'])
def societySubmit(request):
    N = ITQuestion.objects.count()
    K = IT.objects.count()
    counter = [0] * (K + 1)
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1

    best_major_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_major_id = Society.objects.get(pk=best_major_id)
    best_major_id.count += 1
    best_major_id.save()

    major_id = best_major_id
    serializer = SocietySerializer(major_id)
    return Response(serializer.data)

@api_view(['GET'])
def societyResult(request, major_id):
    major = Society.objects.get(id=major_id)
    serialize = SocietySerializer(major)
    return Response(serialize.data)

class Society_QnA(generics.ListCreateAPIView):#CR가능
    queryset = Society_QnA.objects.all()
    serializer_class = Society_QnASerializer

#미컨
@api_view(['GET'])
def meconTest(request, id):
    question = MediaContentsQuestion.objects.get(id=id)
    answers = MediaContentsAnswer.objects.filter(question_id=id)

    serializer = {
        'Qserializer' : MediaContentsQuestionSerializer(question).data,
        'Aserializer' : MediaContentsAnswerSerializer(answers, many=True).data,
    }

    return Response(serializer)

@api_view(['GET'])
def meconSubmit(request):
    N = MediaContentsQuestion.objects.count()
    K = MediaContent.objects.count()
    counter = [0] * (K + 1)
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1

    best_major_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_major_id = MediaContent.objects.get(pk=best_major_id)
    best_major_id.count += 1
    best_major_id.save()

@api_view(['GET'])
def meconResult(request, major_id):
    major = MediaContent.objects.get(id=major_id)
    serialize = MediaContentsSerializer(major)
    return Response(serialize.data)

class MediaContents_QnA(generics.ListCreateAPIView):#CR가능
    queryset = MediaContents_QnA.objects.all()
    serializer_class = MediaContentsQnASerializer
