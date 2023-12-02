import os

import requests
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from .forms import PostForm
from .models import Post


def home_page(request):
    sort_param = request.GET.get('sort', 'created_at')
    query = request.GET.get('q', '')
    print(query)
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    if sort_param == 'title':
        posts = posts.order_by('title')
    elif sort_param == 'created_at':
        posts = posts.order_by('-created_at')

    context = {'posts': posts, 'sort_param': sort_param, 'query': query, 'url_params': request.GET.urlencode()}
    return render(request, 'blog/home.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user if request.user.is_authenticated else None
            post.main_image = request.FILES['main_image']
            post.save()
            return redirect('post-details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post-create.html', {'form': form, 'error': form.errors})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post-create.html'
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'blog/post-delete.html'

    def form_valid(self, form):
        post = self.get_object()

        image_path = post.main_image.path

        if os.path.exists(image_path):
            os.remove(image_path)

        return super().form_valid(form)
