from django.shortcuts import render
from .models import Profile, Skill, About, Portfolio, Post
from django.shortcuts import get_object_or_404


def index(request):
    profile = Profile.objects.first()
    print(profile)
    skills = Skill.objects.all()
    
    context = {"profile": profile, "skills": skills}
    return render(request, "index.html", context)



def skill(request):
    skill = Skill.objects.all()
    context = {"skill": skill}
    return render(request, "about-us.html", context)

def about(request):
    about = About.objects.all()
    context = {"about": about}
    return render(request, "about-us.html", context)

def portfolio(request):
    portfolio = Portfolio.objects.all()
    context = {"portfolio": portfolio}
    return render(request, "portfolio.html", context)

def blog(request):
    post = Post.objects.all()
    context = {"post": post}
    return render(request, "blog.html", context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "single-blog.html", {"post": post})