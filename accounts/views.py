
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    #form_class ayuda a crear un formulario de registro de usuario.
    success_url = reverse_lazy('post_list')
    #success_url ayuda a redirigir al usurio a la pagina login. 

class LogoutView(TemplateView):
    template_name = 'registration/logout.html'

def home(request):
    return render(request, 'index.html')