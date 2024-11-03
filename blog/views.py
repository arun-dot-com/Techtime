from django.shortcuts import render, redirect #need to import redirect module for redirections and all
from django.urls import reverse
from django.http import HttpResponse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm


#Create index page of the app
#the below list is for static data
# posts = [
#         {'id':1,'title': 'Post 1', 'content': 'content of post 1'},
#         {'id':2,'title': 'Post 2', 'content': 'content of post 2'},
#         {'id':3,'title': 'Post 3', 'content': 'content of post 3'},
#         {'id':4,'title': 'Post 4', 'content': 'content of post 4'},
#     ]
def index(request):
    blog_title = "Latest Posts"
    #getting data from post model
    all_posts = Post.objects.all()

    #paginate
    paginator = Paginator(all_posts, 5)
    #we need which page we are currently in
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)


    return render(request, 'blog/index.html', {'blog_title': blog_title , 'page_object': page_object})

#create function for post detail
#post_id is for dynamic url change
def detail(request, slug):
    #static data
    #post = next((item for item in post if item['id']==int(post_id)),None)
    #logger = logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    try:
    #getting data from model by post id
     post = Post.objects.get(slug=slug)
     related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
       raise Http404("Post doesnot exist!")
    return render(request, 'blog/detail.html', {'post':post, 'related_posts':related_posts})

#redirects directly from url to url
def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url")) #this is hardcoding and not an efficient method later we need to change in many places

def new_url_view(request):
    return HttpResponse("This is new Url")

def contact_view(request):
   if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = "Your email has been sent"
            return render(request,'blog/contact.html', {'form':form, 'success_message':success_message} )
        else:
            logger.debug("Form validation failure")
        return render(request,'blog/contact.html', {'form':form, 'name':name, 'email':email, 'message':message} )
   return render(request, 'blog/contact.html')

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request, "blog/about.html", {'about_content':about_content})