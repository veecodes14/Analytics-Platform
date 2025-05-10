from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Site, Profile, Visitor, UserActivity
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SiteListView(ListView):
    model = Site
    template_name = 'site_list.html'

class SiteDetailView(DetailView):
    model = Site
    template_name = 'site_detail.html'

class SiteCreateView(CreateView):
    model = Site
    fields = ['name', 'domain']
    template_name = 'site_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class SiteUpdateView(UpdateView):
    model = Site
    fields = ['name', 'domain']
    template_name = 'site_create.html'

class SiteDeleteView(DeleteView):
    model = Site
    success_url = reverse_lazy('site_list')
    template_name = 'site_confirm_delete'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_detail.html'

    def get_object(self):
        return self.request.user.profile
    
class VisitorListView(ListView):
    model = Visitor
    template_name = 'visitor_list.html'

class ActivityListView:
    model = UserActivity
    template_name = 'activity_list.html'

    




    


# Create your views here.
