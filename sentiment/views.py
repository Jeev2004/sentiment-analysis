from django.shortcuts import render
from .models import sentiment
from .code import sentimentanalysis
def analysis(request):
    if request.method =='POST':
          
      text = request.POST.get('text')
      data = sentiment(text = text)
      data.save()
      a = sentimentanalysis(text)
      context = {}
      context['a'] = a
      return render(request,'base.html',context)  
    return render(request,'index.html')