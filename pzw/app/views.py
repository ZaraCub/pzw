from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Language, Exchange
from .forms import LanguageForm, UserForm, ExchangeForm

User = get_user_model()  # Koristi prilagođeni model korisnika

# Prikaz svih jezika i mogućnost pretrage
def index(request):
    search_query = request.GET.get('search', '')
    languages = Language.objects.filter(name__icontains=search_query) if search_query else Language.objects.all()

    form = LanguageForm(request.POST or None)
    user_form = UserForm(request.POST or None)
    exchange_form = ExchangeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
        if exchange_form.is_valid():
            exchange_form.save()
            return redirect('index')

    users = User.objects.all()
    exchanges = Exchange.objects.all()

    return render(request, 'index.html', {
        'languages': languages,
        'form': form,
        'user_form': user_form,
        'exchange_form': exchange_form,
        'users': users,
        'exchanges': exchanges
    })

# Uređivanje jezika
@login_required
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
@login_required
def delete_language(request, id):
    language = get_object_or_404(Language, id=id)
    if request.method == 'POST':
        language.delete()
        return redirect('index')

    return render(request, 'confirm_delete.html', {'language': language})

# Dodavanje korisnika
@login_required
@user_passes_test(lambda user: user.is_superuser)
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
@login_required
def add_exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExchangeForm()
    return render(request, 'add_exchange.html', {'form': form})

# Prikaz svih razmjena
@login_required
def exchange_list(request):
    exchanges = Exchange.objects.all()
    return render(request, 'exchange_list.html', {'exchanges': exchanges})

# Registracija korisnika
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'register.html')

# Prikaz administrativnih funkcija
@login_required
@user_passes_test(lambda user: user.is_superuser)
def admin_view(request):
    return render(request, 'admin_view.html')

# Prikaz korisničkih funkcija
@login_required
def user_view(request):
    return render(request, 'user_view.html')

