from django.shortcuts import render
from .forms import SignUpForm

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form, 'name':name})

