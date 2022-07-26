from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from clerk.models import ClerkApps


class ClerkLogin(LoginView):
    template_name = 'clerk/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("users")


class Register(FormView):
    template_name = 'clerk/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("users")

    def form_valid(self, form):
        clerk = form.save()
        if clerk is not None:
            login(self.request, clerk)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('users')
        return super(Register, self).get(*args, **kwargs)


# Create your views here.
class Userlist(LoginRequiredMixin, ListView):
    model = ClerkApps
    context_object_name = 'application_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['application_list'] = context['application_list'].filter(clerk=self.request.user)
        context['count'] = context['application_list'].filter(status=False).count()
        context['c_count'] = context['application_list'].filter(status=True).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['application_list'] = context['application_list'].filter(apptitle__icontains=search_input)
        # apptitle__startswith

        context['search_input'] = search_input

        return context


class Userdetail(LoginRequiredMixin, DetailView):
    model = ClerkApps
    context_object_name = 'app_detail'
    template_name = 'clerk/clerkapps_detail.html'


class AppCreate(LoginRequiredMixin, CreateView):
    model = ClerkApps
    template_name = 'clerk/clerkapps_create.html'
    # fields = "__all__"
    fields = ["apptitle", "appdesc", "status"]
    success_url = reverse_lazy("users")

    def form_valid(self, form):
        form.instance.clerk = self.request.user
        return super(AppCreate, self).form_valid(form)


class AppUpdate(LoginRequiredMixin, UpdateView):
    model = ClerkApps
    template_name = 'clerk/clerkapps_create.html'
    fields = ["apptitle", "appdesc", "status"]
    success_url = reverse_lazy("users")


class AppDelete(LoginRequiredMixin, DeleteView):
    model = ClerkApps
    context_object_name = 'app_detail'
    success_url = reverse_lazy("users")
    template_name = 'clerk/clerkapps_delete.html'