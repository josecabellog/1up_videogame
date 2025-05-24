from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(TemplateView):
    template_name = 'registration/logout.html'

def home(request):
    return render(request, 'index.html')