from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects
    #blogs (변수)에 Blog (모델)의 쿼리셋을 담는다

    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()

    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)

    # request된 페이지가 뭔지를 알아내고 ( requset페이지를 변수에 담아냄 )
    page = request.GET.get('page')

    # request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html',
    { 'blogs':blogs , 'posts':posts }) # blogs (object)를 전달
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str( blog.id ))
    
"""
def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')

    else:
        form = BlogPost()
        return render(request, 'new.html', { 'form': form })
"""