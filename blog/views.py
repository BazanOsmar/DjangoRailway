from django.shortcuts import render

# Create your views here.
def renderArticles(request):
    return render(request, 'article.html')