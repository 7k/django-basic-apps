from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from basic.profiles.models import *
from basic.profiles.forms import *


class ProfileList(ListView):
    model = Profile
    paginate_by = 20


class ProfileDetail(DetailView):
    def get_object(self):
        username = self.kwargs.get('username', None)
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise Http404
        return Profile.objects.get(user=user)


@login_required
def profile_edit(request, template_name='profiles/profile_form.html'):
    """Edit profile."""

    if request.POST:
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        service_formset = ServiceFormSet(request.POST, instance=profile)
        link_formset = LinkFormSet(request.POST, instance=profile)

        if profile_form.is_valid() and user_form.is_valid() and service_formset.is_valid() and link_formset.is_valid():
            profile_form.save()
            user_form.save()
            service_formset.save()
            link_formset.save()
            return HttpResponseRedirect(reverse('profile_detail', kwargs={'username': request.user.username}))
        else:
            context = {
                'profile_form': profile_form,
                'user_form': user_form,
                'service_formset': service_formset,
                'link_formset': link_formset
            }
    else:
        profile = Profile.objects.get(user=request.user)
        service_formset = ServiceFormSet(instance=profile)
        link_formset = LinkFormSet(instance=profile)
        context = {
            'profile_form': ProfileForm(instance=profile),
            'user_form': UserForm(instance=request.user),
            'service_formset': service_formset,
            'link_formset': link_formset
        }
    return render_to_response(template_name, context, context_instance=RequestContext(request))
