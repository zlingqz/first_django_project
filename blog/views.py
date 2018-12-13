from django.shortcuts import render
from datetime import datetime
from . import models
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView


# Create your views here.

# def archive(request):
#     post = models.BlogPost(title='mocktitle', body='mockbody',
#                            timestamp=datetime.now())
#     return render(request, 'archive.html', {'posts': [post]})

def archive(request):
    posts = models.BlogPost.objects.all()[:10]
    # t = loader.get_template('archive.html')
    # c = {'posts': posts}
    # return HttpResponse(t.render(c))
    # return render_to_response('archive.html', {'posts': posts,
    #         'form': models.BlogPostForm()})
    return render(request, 'archive.html', {'posts': posts,
            'form': models.BlogPostForm()},)
    # return TemplateView(request, 'archive.html',
    #                           {'posts': posts, 'form': models.BlogPostForm()})


# def create_blogpost(request):
#     if request.method == 'POST':
#         models.BlogPost(
#             title=request.POST.get('title'),
#             body=request.POST.get('body'),
#             timestamp=datetime.now(),
#         ).save()
#     return HttpResponseRedirect('/blog/')

def create_blogpost(request):
    if request.method == 'POST':
        form = models.BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp=datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')
