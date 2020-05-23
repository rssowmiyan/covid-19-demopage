from django.urls import path
from . import views

app_name='polls'

urlpatterns=[
    path('',views.pollpage,name='pollpage'),
    path('<int:qn_id>/',views.details,name='details'),
    path('<int:qn_id>/results/',views.results,name='results'),
    path('<int:qn_id>/vote/',views.vote,name='vote'),
    path('resultsdata/<str:obj>/',views.resultsdata,name='resultsdata'),
]