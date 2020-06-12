from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request,'index.html')

def read(request):
    blogs=Blog.objects.all()
    paginator = Paginator(blogs,2) #1p에 블로그 객체 최대 2개
    page=request.GET.get('page') #request된 페이지를 변수에 담기
    posts=paginator.get_page(page) #request된 페이지를 저장한 후 return
    return render(request,'funccrud.html',{'blogs':blogs, 'posts':posts})

def create(request):
   #새로운 데이터, 블로그 글 저장이 안됨! (POST)
    if request.method == 'POST':
    #입력된 블로그 글들을 저장해라 / 현재 오류 발생. return 값 없다함
        form=NewBlog(request.POST,request.FILES) #POST는 글만 받아옴. FILES까지 받아와야지 media 올라감!!!!!!

        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
        return redirect('home')

    # 글쓰기 페이지를 띄워주는 역할:GET(!=POST)
    else:
    #단순히 입력받을 수 있는 form을 띄워주라 => 이상없음
        form = NewBlog()
        return render(request,'new.html', {'form':form})

def update(request, pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    #해당하는 블로그 객체 번호에 맞는 입력공간
    form = NewBlog(request.POST, instance = blog) #객체는 위에 있는 블로그 객체
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'new.html', {'form':form})

def delete(request,pk):
    blog=get_object_or_404(Blog, pk=pk) #기본키명이 pk
    blog.delete()
    return redirect('home')


