# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Child, DiaperChange, Feeding, Note, Sleep, Timer, TummyTime
from .forms import (ChildForm, DiaperChangeForm, FeedingForm, SleepForm,
                    TimerForm, TummyTimeForm)


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'


class ChildList(PermissionRequiredMixin, ListView):
    model = Child
    permission_required = ('core.view_child',)


class ChildAdd(PermissionRequiredMixin, CreateView):
    model = Child
    permission_required = ('core.add_child',)
    form_class = ChildForm
    success_url = '/children'


class ChildUpdate(PermissionRequiredMixin, UpdateView):
    model = Child
    permission_required = ('core.change_child',)
    form_class = ChildForm
    success_url = '/children'


class ChildDelete(PermissionRequiredMixin, DeleteView):
    model = Child
    permission_required = ('core.delete_child',)
    success_url = '/children'


class DiaperChangeList(PermissionRequiredMixin, ListView):
    model = DiaperChange
    permission_required = ('core.view_diaperchange',)


class DiaperChangeAdd(PermissionRequiredMixin, CreateView):
    model = DiaperChange
    permission_required = ('core.add_diaperchange',)
    form_class = DiaperChangeForm
    success_url = '/changes'


class DiaperChangeUpdate(PermissionRequiredMixin, UpdateView):
    model = DiaperChange
    permission_required = ('core.change_diaperchange',)
    form_class = DiaperChangeForm
    success_url = '/changes'


class DiaperChangeDelete(PermissionRequiredMixin, DeleteView):
    model = DiaperChange
    permission_required = ('core.delete_diaperchange',)
    success_url = '/changes'


class FeedingList(PermissionRequiredMixin, ListView):
    model = Feeding
    permission_required = ('core.view_feeding',)


class FeedingAdd(PermissionRequiredMixin, CreateView):
    model = Feeding
    permission_required = ('core.add_feeding',)
    form_class = FeedingForm
    success_url = '/feedings'


class FeedingUpdate(PermissionRequiredMixin, UpdateView):
    model = Feeding
    permission_required = ('core.change_feeding',)
    form_class = FeedingForm
    success_url = '/feedings'


class FeedingDelete(PermissionRequiredMixin, DeleteView):
    model = Feeding
    permission_required = ('core.delete_feeding',)
    success_url = '/feedings'


class NoteList(PermissionRequiredMixin, ListView):
    model = Note
    permission_required = ('core.view_note',)


class NoteAdd(PermissionRequiredMixin, CreateView):
    model = Note
    permission_required = ('core.add_note',)
    fields = ['child', 'note']
    success_url = '/notes'


class NoteUpdate(PermissionRequiredMixin, UpdateView):
    model = Note
    permission_required = ('core.change_note',)
    fields = ['child', 'note']
    success_url = '/notes'


class NoteDelete(PermissionRequiredMixin, DeleteView):
    model = Note
    permission_required = ('core.delete_note',)
    success_url = '/notes'


class SleepList(PermissionRequiredMixin, ListView):
    model = Sleep
    permission_required = ('core.view_sleep',)


class SleepAdd(PermissionRequiredMixin, CreateView):
    model = Sleep
    permission_required = ('core.add_sleep',)
    form_class = SleepForm
    success_url = '/sleep'


class SleepUpdate(PermissionRequiredMixin, UpdateView):
    model = Sleep
    permission_required = ('core.change_sleep',)
    form_class = SleepForm
    success_url = '/sleep'


class SleepDelete(PermissionRequiredMixin, DeleteView):
    model = Sleep
    permission_required = ('core.delete_sleep',)
    success_url = '/sleep'


class TimerAdd(PermissionRequiredMixin, CreateView):
    model = Timer
    permission_required = ('core.add_timer',)
    form_class = TimerForm

    def get_form_kwargs(self):
        kwargs = super(TimerAdd, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        if resolve(self.request.POST['success_url']).url_name:
            url = self.request.POST['success_url']
        else:
            url = '/'
        return url


class TummyTimeList(PermissionRequiredMixin, ListView):
    model = TummyTime
    permission_required = ('core.view_tummytime',)


class TummyTimeAdd(PermissionRequiredMixin, CreateView):
    model = TummyTime
    permission_required = ('core.add_tummytime',)
    form_class = TummyTimeForm
    success_url = '/tummy-time'


class TummyTimeUpdate(PermissionRequiredMixin, UpdateView):
    model = TummyTime
    form_class = TummyTimeForm
    success_url = '/tummy-time'


class TummyTimeDelete(PermissionRequiredMixin, DeleteView):
    model = TummyTime
    success_url = '/tummy-time'
