from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def count(request):
    fulltext=request.GET['FullText']
    words =fulltext.split()
    dic={i:words.count(i) for i in words}
    s_words=sorted(dic.items(),key=operator.itemgetter(1), reverse=True)
    print(s_words)
    return render(request, 'count.html', {'fulltext':fulltext, 'length':len(words),'tot':s_words})
