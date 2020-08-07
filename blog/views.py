from django.shortcuts import HttpResponse,render
from blog.models import Feed


def bloghome(request):
    allfeeds=Feed.objects.all()
    context={'allfeeds':allfeeds}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    feed=Feed.objects.filter(slug=slug)[0]
    context={'feed':feed}
    return render(request,'blog/blogpost.html',context)    