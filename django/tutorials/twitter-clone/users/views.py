from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, PorfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.clean_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if uform.is_valid() and pfrom.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Account has been updated.')
            return redirect('profile')
        else:
            uform = UserUpdateForm(instance=request.user)
            pform = PorfileUpdateForm(instance=request.user.profile)

@login_required
def SearchView(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        print(query)
        results = User.objects.filter(username__contains=query)
        context = {
            'results':results
        }
        return render(request, 'users/search_results.html', context)