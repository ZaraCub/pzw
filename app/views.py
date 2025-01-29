from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Language, User, Exchange
from .forms import LanguageForm, UserForm, ExchangeForm

from rest_framework import generics, permissions
from .serializers import LanguageSerializer, UserSerializer, ExchangeSerializer



# 1. Funkcijski prikazi
def index(request):
    search_query = request.GET.get('search', '')
    if search_query:
        languages = Language.objects.filter(name__icontains=search_query)
    else:
        languages = Language.objects.all()

    form = LanguageForm(request.POST or None)

    # Dodavanje novog jezika
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    users = User.objects.all()
    exchanges = Exchange.objects.all()

    return render(request, 'index.html', {
        'languages': languages,
        'form': form,
        'users': users,
        'exchanges': exchanges
    })


def edit_language(request, id):
    language = get_object_or_404(Language, id=id)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LanguageForm(instance=language)

    return render(request, 'edit_language.html', {'form': form})


def delete_language(request, id):
    language = get_object_or_404(Language, id=id)
    if request.method == 'POST':
        language.delete()
        return redirect('index')

    return render(request, 'confirm_delete.html', {'language': language})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def add_exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExchangeForm()
    return render(request, 'add_exchange.html', {'form': form})


# 2. Generički prikazi

# ListView za jezike
class LanguageListView(ListView):
    model = Language
    template_name = 'language_list.html'
    context_object_name = 'languages'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Language.objects.filter(name__icontains=query) if query else Language.objects.all()


class LanguageDetailView(DetailView):
    model = Language
    template_name = 'language_detail.html'
    context_object_name = 'language'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exchanges'] = self.object.exchanges.all()
        return context


# ListView i DetailView za korisnike
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return User.objects.filter(username__icontains=query) if query else User.objects.all()


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


# ListView i DetailView za razmjene
class ExchangeListView(ListView):
    model = Exchange
    template_name = 'exchange_list.html'
    context_object_name = 'exchanges'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Exchange.objects.filter(language__name__icontains=query) if query else Exchange.objects.all()


class ExchangeDetailView(DetailView):
    model = Exchange
    template_name = 'exchange_detail.html'
    context_object_name = 'exchange'


# 3. Generički CRUD prikazi za jezike

class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'language_form.html'
    success_url = reverse_lazy('language_list')


class LanguageUpdateView(UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'language_form.html'
    success_url = reverse_lazy('language_list')


class LanguageDeleteView(DeleteView):
    model = Language
    template_name = 'language_confirm_delete.html'
    success_url = reverse_lazy('language_list')


# API za Language model
class LanguageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]  # API je dostupan samo prijavljenim korisnicima


class LanguageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]  # API je dostupan samo prijavljenim korisnicima

# API za User model
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# API za Exchange model
class ExchangeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExchangeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = [permissions.IsAuthenticated]

