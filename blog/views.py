from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import NewCommentForm, BookForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from django.contrib import messages

def home(request):

    all_posts = Post.newmanager.all()

    return render(request, 'index.html', {'posts': all_posts})


def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')

    comments = post.comments.filter(status=True)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'single.html', {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form})


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context


# add new book

class AddBookView(CreateView):
    model = Post
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('blog:homepage')


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:homepage')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {
        'form': form
    })


# delete book

class DeleteBookView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:homepage')

    def testfunc(self):
        Post = self.request.get_object()
        if self.request.user == Post.author:
            return True
        return False


# update book

class UpdateBookView(UpdateView):
    model = Post
    fields = ['title', 'book_author', 'content']

    def form_valid(self, form):
        form.instance.author == self.request.user
        return super().form_valid(form)

        def testfunc(self):
            Post = self.request.get_object()
            if self.request.user == Post.author:
                return True
            return False


# about

def about(request):
    return render(request, 'about.html', {})


def password_success(request):
    return render(request, 'registration/password_success.html', {})


# contact
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        #subject = request.POST['subject']
        message = request.POST['message']

        # send email

        send_mail(

            email,  # from email
            message + "\n" + f"Sender Name:  {name} \n Sender Email: {email}",  # message
            name,  # name

            [settings.EMAIL_HOST_USER]  # to email


        )

        return render(request, 'contact.html', {'name': name})

    else:

        return render(request, 'contact.html', {})


# users list
class UserEntryListView(ListView):
    model = Post
    template_name = 'user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-publish')
