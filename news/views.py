from django.views.generic import ListView, DetailView
from .models import Post, Author
from django_filters.views import FilterView
from .filters import PostFilter
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm

class PostList(ListView):
    model = Post
    ordering = ['-created_at']
    template_name = 'news/news.html'
    context_object_name = 'news'
    paginate_by = 10

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'

class PostSearchView(FilterView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search_results'
    filterset_class = PostFilter
    paginate_by = 10


class NewsCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'news'

        # Создать автора, если его нет
        author, created = Author.objects.get_or_create(user=self.request.user)
        post.author = author

        post.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news_list')


class ArticleCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'article'

        # Создать автора, если его нет
        author, created = Author.objects.get_or_create(user=self.request.user)
        post.author = author

        post.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news_list')


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news/post_confirm_delete.html'
    success_url = reverse_lazy('news_list')