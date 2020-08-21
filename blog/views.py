from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import CV
from .forms import PostForm
from .forms import CVForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
    Post.objects.get(pk=pk)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def my_cv(request):
    all = CV.objects.all()
    my_cv = all[0]
    return render(request, 'blog/my_cv.html', {'my_cv': my_cv})

def my_cv_edit(request):
    all = CV.objects.all()
    my_cv = all[0]
    if request.method == "POST":
        form = CVForm(request.POST, instance=my_cv)
        if form.is_valid():
            my_cv = form.save(commit=False)
            my_cv.author = request.user
            my_cv.published_date = timezone.now()
            my_cv.save()
            return redirect('my_cv')
    else:
        form = CVForm(instance=my_cv)
    return render(request, 'blog/my_cv_edit.html', {'form': form})
