"""backendprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
	path('it/test/<int:id>', views.itTest, name='itTest'),
    path('it/submit/', views.itSubmit, name='itSubmit'),
    path('it/result/<int:major_id>/', views.itResult, name='itResult'),
    path('IT_QnA/', views.IT_QnA.as_view()),

    path('humanity/test/<int:id>', views.humanityTest, name='humanityTest'),
    path('humanity/submit/', views.humanitySubmit, name='humanitySubmit'),
    path('humanity/result/<int:major_id>/', views.humanityResult, name='humanityResult'),
    path('Humanity_QnA/', views.Humanity_QnA.as_view()),

    path('society/test/<int:id>', views.societyTest, name='societyTest'),
    path('society/submit/', views.societySubmit, name='societySubmit'),
    path('society/result/<int:major_id>/', views.societyResult, name='societyResult'),
    path('society_QnA/', views.Society_QnA.as_view()),

    path('mecon/contest/<int:id>', views.meconTest, name='mediacontentTest'),
    path('mecon/submit/', views.meconSubmit, name='mediacontentSubmit'),
    path('mecon/result/<int:major_id>/', views.meconResult, name='mediacontentResult'),
    path('mecon_QnA/', views.MediaContents_QnA.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)
