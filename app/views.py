from django.shortcuts import render, redirect, get_object_or_404
from .models import Language, User, Exchange
from .forms import LanguageForm, UserForm, ExchangeForm

# Prikaz svih jezika i mogućnost pretrage
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


    # Dobijanje svih korisnika i razmjena
    users = User.objects.all()
    exchanges = Exchange.objects.all()

    return render(request, 'index.html', {
        'languages': languages, 
        'form': form,
        'users': users,
        'exchanges': exchanges
    })

    s
# Uređivanje jezika
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

# Brisanje jezika
def delete_language(request, id):
    language = get_object_or_404(Language, id=id)
    if request.method == 'POST':
        language.delete()
        return redirect('index')

    return render(request, 'confirm_delete.html', {'language': language})

# Dodavanje korisnika
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

# Dodavanje razmjene jezika
def add_exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExchangeForm()
    return render(request, 'add_exchange.html', {'form': form})

# Prikaz svih razmjenas
def exchange_list(request):
    exchanges = Exchange.objects.all()
    return render(request, 'exchange_list.html', {'exchanges': exchanges})



from django.views.generic import ListView, DetailView
from .models import Language, User, Exchange

# Generički ListView za Language model
class LanguageListView(ListView):
    model = Language
    template_name = 'language_list.html'
    context_object_name = 'languages'
    paginate_by = 10

    # Filtriranje po imenu jezika
    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Language.objects.filter(name__icontains=query) if query else Language.objects.all()

# Generički DetailView za Language model
class LanguageDetailView(DetailView):
    model = Language
    template_name = 'language_detail.html'
    context_object_name = 'language'
    
    
    # Dodaj relacije u context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exchanges'] = self.object.exchanges.all()  # Pristupa svim razmjenama za jezik
        return context

# Generički ListView za User model
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    # Filtriranje po korisničkom imenu
    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return User.objects.filter(username__icontains=query) if query else User.objects.all()

# Generički DetailView za User model
class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

# Generički ListView za Exchange model
class ExchangeListView(ListView):
    model = Exchange
    template_name = 'exchange_list.html'
    context_object_name = 'exchanges'
    paginate_by = 10

    # Filtriranje po datumu
    def get_queryset(self):
        query = self.request.GET.get('search', '')
        return Exchange.objects.filter(language__name__icontains=query) if query else Exchange.objects.all()

# Generički DetailView za Exchange model
class ExchangeDetailView(DetailView):
    model = Exchange
    template_name = 'exchange_detail.html'
    context_object_name = 'exchange'
