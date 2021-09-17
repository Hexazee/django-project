# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import SignUpForm
# from django.contrib.auth.decorators import login_required


# def signup(request):

#     if request.method == "POST":
#         form = SignUpForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome to My Website, {username}')
#             return redirect('user-signin')


#     else:
#         form = SignUpForm()

#     return render(request, 'users/signup.html', {'title': 'OX | Sign Up', 'form': form})

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')
