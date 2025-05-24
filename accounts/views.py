
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# accounts/views.py
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ← Log the user in immediately
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    #form_class ayuda a crear un formulario de registro de usuario.
    success_url = reverse_lazy('article_list')
    #success_url ayuda a redirigir al usurio a la pagina login. 

class LogoutView(TemplateView):
    template_name = 'registration/logout.html'

def home(request):
    return render(request, 'index.html')