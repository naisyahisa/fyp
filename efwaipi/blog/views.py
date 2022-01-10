from django.db.models import query
from django.db.models.query import QuerySet
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from .models import Vaksinasi 
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
 
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 

# def vac_chart(request):
#     labels = []
#     data = []

#     percentage = (Vaksinasi.objects.values('vac_done')/Vaksinasi.objects.values('vac_able'))*100
#     queryset = Vaksinasi.objects.values('district').annotate(perc = Sum(percentage)).order_by('-perc')
#     for entry in queryset:
#         labels.append(entry['district'])
#         data.append(entry[percentage])

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]
