from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    DetailView

from blog.models import BlogPost


# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        queryset = BlogPost.objects.filter(publication_sign=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = new_post.title
            new_post.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'publication_sign')

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('slug')])

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = new_post.title
            new_post.save()
        return super().form_valid(form)


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:list')


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        if self.object.number_of_views == 100:
            send_mail(
                subject='Поздравление',
                message=f'Поздравляю ваш пост {self.object.title} набрал 100 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['victoria.gaponava@gmail.com'],
                fail_silently=False,
            )
        self.object.save()
        return self.object
