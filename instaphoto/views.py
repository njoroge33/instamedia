from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm
from django.core.mail import send_mail
from .models import Post

@login_required(login_url='/login/')
def index(request):
    current_user = request.user
    posts = Post.get_posts()
    
   
    return render(request, 'index.html', {'current_user':current_user, 'posts':posts})

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            send_mail(
            'Welcome to insta app.',
            f'Hello {name},\n '
            'Welcome to insta app, where you can share your photos with the world.',
            'johngichuhi769@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name':name})

@login_required(login_url='/login/')
def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= current_user
            post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'current_user':current_user, 'form':form})
    
