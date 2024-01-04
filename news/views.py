from django.db.models.functions import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class PostsList(ListView):
    model = Post
    ordering = '-id'
    template_name = 'post.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_template_names(self):
        if self.request.path == '/posts/':
            self.template_name = 'post.html'
        elif self.request.path == '/posts/search/':
            self.template_name = 'search.html'
        return self.template_name

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_post'] = "Next news will be tomorrow"
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'post'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post_content = 'NE'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post_content = 'AR'
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post

    def get_template_names(self):
        if self.request.path == f'/article/{self.object.pk}/edit/':
            self.template_name = 'article_edit.html'
        else:
            self.template_name = 'news_edit.html'
        return self.template_name

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

    def get_template_names(self):
        if self.request.path == f'/article/{self.object.pk}/delete/':
            self.template_name = 'article_delete.html'
        else:
            self.template_name = 'news_delete.html'
        return self.template_name


