from django.shortcuts import render, redirect
from blog.models import Post, Comment, Category
from blog.forms import CommentForm, PostForm, CategorySearchForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login') #redirect when user is not logged in
def blog_index(request):

    if request.method == 'POST':
        form = CategorySearchForm(request.POST)
        category = form.data['category']
        posts = Post.objects.filter(categories__name__contains =category)
        context = {
        "form": form,
        "posts": posts,
            }
        return render(request, "blog_index.html", context)

    posts = Post.objects.all().order_by('-created_on')
    form = CategorySearchForm()
    context = {
        "form": form,
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains
    =category)
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)
@login_required(login_url='login') #redirect when user is not logged in
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=request.user,
                body=form.cleaned_data["body"], 
                post=post)
            

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)


