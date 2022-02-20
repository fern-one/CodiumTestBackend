from pydoc import describe
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse

from blogs.form import PostModelForm
from .models import Post

# Create your views here.
def hello(task):
    return HttpResponse("<h1>Hello World</h1>")

def home(task):
    return render(task,'index.html',
    {
        'name' : 'Hello'
        
    })

def Home(task):
    data = Post.objects.all()
    return render(task,'home.html',
    {
        'Posts':data
    
    })

def createForm(task):
    form = PostModelForm
    return render(task,'form.html', {'form' :  form})

def addBlog(task):
    #name = task.POST['name']
    #description = task.POST['description']

    #return render(task,'home.html',
    #{
       # 'name' : name,
       # 'description' : description,

    #})
    
    form = PostModelForm(task.POST)
    if form.is_valid():
        form.save(commit=True)

    return redirect("home.html")

def edit(task, post_id):
    post = Post.objects.get(id = post_id)
    post_form = PostModelForm(instance=post_id)

    return render(task, "edit.html", {"form": post_form, 'post_id': post_id})


def post_save(task, post_id):
    post = Post.objects.get(id=post_id)
    form = PostModelForm(instance=post, data=task.POST)
    if form.is_valid():
        form.save(commit=True)
    return redirect("home.html")

def delete(task, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home.html')