from django.forms import forms
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Ticket, Comment
from django.db.models import Q
from .filters import TicketFilter
from django_filters.views import FilterView
from .tables import TicketTable
from django_tables2 import SingleTableView, LazyPaginator
from .forms import TicketCreateForm, CommentCreateForm
from django.shortcuts import redirect


class AddFollowerView(LoginRequiredMixin, View):
    model = Ticket

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('follow')
        ticket = Ticket.objects.get(pk=pk)

        if self.request.user in ticket.ticket_follower.all():
            ticket.ticket_follower.remove(self.request.user)
        else:
            ticket.ticket_follower.add(self.request.user)

        return redirect('/ticket/'+pk)


class TicketDetailView(LoginRequiredMixin, DetailView, CreateView):
    model = Ticket
    template_name = "ticket/comment.html"
    form_class = CommentCreateForm

    # def post(self, request, *args, **kwargs):
    #     print(request)
    #     print(args)
    #     print(kwargs)
    #

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ticket = Ticket.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tickets'
    ordering = ['-date_posted']

    def get_queryset(self):
        qs = super().get_queryset()

        tstatus = self.request.GET.get('status')
        ttype = self.request.GET.get('type')
        tprio = self.request.GET.get('priority')
        tfilter = self.request.GET.get('filter')
        # #filter
        if tstatus and tstatus != '*':
            qs = qs.filter(status__exact=tstatus)
        if ttype and ttype != '*':
            qs = qs.filter(type__exact=ttype)
        if tprio and tprio != '*':
            qs = qs.filter(priority__exact=tprio)
        if tfilter and tfilter != '':
            qs = qs.filter(Q(title__contains=tfilter) | Q(description__contains=tfilter))

        return qs


class FilteredTicketList(LoginRequiredMixin, FilterView, SingleTableView):
    model = Ticket
    template_name = 'ticket/ticket_search.html'
    filterset_class = TicketFilter
    table_class = TicketTable
    table_pagination = {"per_page": 10}


def about(request):
    return render(request, 'ticket/about.html', {'title': 'About'})


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketCreateForm
    # template_name = 'ticket/testgrid.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.instance.date_expire is None:
            form.instance.date_expire = Ticket.objects.get(pk=self.kwargs.get('pk')).date_expire
        return super().form_valid(form)


class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
