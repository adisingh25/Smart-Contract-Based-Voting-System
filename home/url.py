
from django.contrib import admin
from django.urls import path
from . import views
import web3

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('candidateaura/',views.candidateaura,name='candidateaura'),
    path('candidatepalg/',views.candidatepalg,name='candidatepalg'),
    path('candidateudma/', views.candidateudma, name='candidateudma'),
    path('palghar/',views.palghar,name='palghar'),
    path('amroha/',views.amroha,name='amroha'),
    path('udma/', views.udma, name='udma'),
    path('palghar/votehere/',views.votepalghar,name='vote'),
    path('amroha/votehere/',views.voteamroha,name='votea'),
    path('udma/votehere/',views.voteudma,name='voteu'),
    path('palghar/thankyou/',views.thankyou,name='thankyou'),
    path('winner/',views.winnervote,name='winnervote'),
    path('winnera/', views.winnervotea, name='winnervotea'),
    path('winneru/', views.winnervoteu, name='winnervoteu'),
    path ('winneroverall/',views.winneroverall,name='winneroverall'),
    path('winnerdetails',views.winnerdetails,name='winnerdetails')
    # path('success/',views.success,name='success')
]
