from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Comment, Post
from django.views.generic import DetailView
from django.urls import reverse
from .forms import CommentForm

# Create your views here.
def post_index(request):
    entry = Post.objects.filter(status='published')
    context = {
        'entry':entry
    }
    return render(request,'blog/index.html',context)

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    

    # def post(request):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return reverse('detail')



def detail(request,slug):
    item = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=item.id)

   

    form = CommentForm()
    context = {
                # 'form':form,
                'post':item
            }
    if request.method == 'POST':
        form = form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.author = request.user.username
            form.save()
            return render(request,'blog/post_detail.html',context)
        else:
            return render(request,'blog/post_detail.html',context)
    return render(request,'blog/post_detail.html',context)
    


def draft(request):
    entry = Post.objects.filter(status='draft')
    context={
        'entry':entry
    }
    return render (request,'blog/draft.html',context)

class DraftDetail(DetailView):
    queryset = Post.objects.filter(status='draft')
    context_object_name = 'drafts'
    template_name = 'blog/drafts.html'


def publish(request,slug,pk):
    item = Post.objects.get(id=pk,slug=slug)
    item.status = 'published'
    item.save()
    return reverse('home')