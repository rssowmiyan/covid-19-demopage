from django.shortcuts import render,redirect,get_object_or_404
from .models import Question,Choice
from django.http import HttpResponse,JsonResponse
from django.conf.urls import url, include
from django.contrib.auth.models import User
# ###########################################################################
def pollpage(request):
    latestqns=Question.objects.order_by('-pub_date')[:5]
    context={'latestqns':latestqns}
    return render(request,'poll_home.html',context)

def details(request,qn_id):
    qn = get_object_or_404(Question,pk=qn_id)
    return render(request,'poll_details.html',{'qn':qn})

def results(request,qn_id):
    qn = get_object_or_404(Question,pk=qn_id)
    return render(request,'poll_results.html',{'qn':qn})

def vote(request,qn_id):
    qn = get_object_or_404(Question,pk=qn_id)
    try:
        selected_choice = qn.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'details.html',{'qn':qn,'error':'choice does not exist.Please try again'})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return redirect('polls:results',qn_id=qn.id)#this is how use pass values in redirect

def resultsdata(request,obj):
    print(obj)
    qn =Question.objects.get(id=obj)
    print(qn)
    votes = qn.choice_set.all()
    votesdata=[]
    for i in votes:
        votesdata.append({i.choice_text:i.votes})
    print(votesdata)
    return JsonResponse(votesdata , safe=False)