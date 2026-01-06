from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm, CommentForm, ProfileForm
from django.core.mail import send_mail
from .models import Post, Comment, Profile

@login_required(login_url='/login/')
def index(request):
    current_user = request.user
    posts = Post.get_posts()
    comments = Comment.get_comments()
    form1 = NewPostForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = Post.objects.get(id=int(request.POST["post_id"]))
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    
   
    return render(request, 'index.html', {'current_user':current_user, 'posts':posts, 'form':form, 'form1':form1, 'comments':comments})

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form)
        if form.is_valid():
            print ("here")
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            # send_mail(
            # 'Welcome to insta app.',
            # f'Hello {name},\n '
            # 'Welcome to insta app, where you can share your photos with the world.',
            # 'johngichuhi769@gmail.com',
            # [email],
            # fail_silently=False,
            # )
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

@login_required(login_url='/login/')
def update_profile(request):
    current_user = request.user
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        # Pass the existing profile instance to the form
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # No need to set user or create new profile - just save the form
            form.save()
            # messages.success(request, 'Your profile has been updated!')
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user, 'form':form})

def profile(request):
    current_user = request.user

    posts = Post.get_posts()
    comments = Comment.get_comments()
    
    return render(request, 'profile.html', {'current_user':current_user, 'posts':posts, 'comments':comments})
    
