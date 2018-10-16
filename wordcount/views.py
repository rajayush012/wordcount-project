from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    sentence=request.GET['fulltext']
    words=sentence.split()
    count=len(words)
    wordFrequency = {}
    for word in words:
        if word in wordFrequency:
            #increase
            wordFrequency[word]+=1
        else:
            #add word
            wordFrequency[word]=1

    sortedWords=sorted(wordFrequency.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':sentence,'count':count,'sortedWords':sortedWords})

def about(request):
    return render(request,'about.html')
