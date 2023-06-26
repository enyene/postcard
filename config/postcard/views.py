
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "post"
    template_name = "postcard/list.html"

class PostTagListView(ListView):
    template_name = "postcard/taglist.html"

    def get_tag(self):
        return self.kwargs.get("tag")
    
    def get_queryset(self) :
        return self.model.objects.filter(tags__slug=self.get_tag())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = "postcard/detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post

    fields = ['title', 'description', 'image', 'tags']

    template_name = 'photoapp/create.html'

    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):

        form.instance.submitter = self.request.user

        return super().form_valid(form)
    

class UserIsSubmitter(UserPassesTestMixin):

    # Custom method
    def get_photo(self):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))

    def test_func(self):

        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')
        
class PostUpdateView(UserIsSubmitter, UpdateView):

    template_name = 'postcard/update.html'

    model = Post

    fields = ['title', 'description', 'tags']

    success_url = reverse_lazy('post:list')

class PostDeleteView(UserIsSubmitter, DeleteView):

    template_name = 'postcard/delete.html'

    model = Post

    success_url = reverse_lazy('post:list') 