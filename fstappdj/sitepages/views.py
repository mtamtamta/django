from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Me, Program, Supervisor, Manager, Classmate
from .forms import MeForm, ProgramForm, SupervisorForm, ManagerForm, ClassmateForm

# ------------- «Я» -------------
def me_list(request):
    qs = Me.objects.all()
    # Фильтрация по ФИО или email
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(Q(full_name__icontains=q) | Q(email__icontains=q))
    # Сортировка
    order = request.GET.get('order_by', 'full_name')
    allowed = ['full_name', '-full_name', 'email', '-email']
    if order in allowed:
        qs = qs.order_by(order)
    return render(request, 'sitepages/me_list.html', {
        'items': qs, 'q': q, 'order': order
    })

def me_create(request):
    if request.method == 'POST':
        form = MeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sitepages:me_list')
    else:
        form = MeForm()
    return render(request, 'sitepages/me_form.html', {'form': form})

# ------------- «ОП» -------------
def program_list(request):
    qs = Program.objects.all()
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(name__icontains=q)
    order = request.GET.get('order_by', 'name')
    allowed = ['name', '-name']
    if order in allowed:
        qs = qs.order_by(order)
    return render(request, 'sitepages/program_list.html', {
        'items': qs, 'q': q, 'order': order
    })

def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitepages:program_list')
    else:
        form = ProgramForm()
    return render(request, 'sitepages/program_form.html', {'form': form})

# ------------- «Менеджмент» -------------
def management_list(request):
    sup = Supervisor.objects.all()
    mgr = Manager.objects.all()
    return render(request, 'sitepages/management_list.html', {
        'supervisors': sup,
        'managers': mgr
    })

def supervisor_create(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sitepages:management_list')
    else:
        form = SupervisorForm()
    return render(request, 'sitepages/supervisor_form.html', {'form': form})

def manager_create(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sitepages:management_list')
    else:
        form = ManagerForm()
    return render(request, 'sitepages/manager_form.html', {'form': form})

# ------------- «Сокурсники» -------------
def classmates_list(request):
    qs = Classmate.objects.all()
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(Q(full_name__icontains=q) | Q(email__icontains=q))
    order = request.GET.get('order_by', 'full_name')
    allowed = ['full_name', '-full_name']
    if order in allowed:
        qs = qs.order_by(order)
    return render(request, 'sitepages/classmates_list.html', {
        'items': qs, 'q': q, 'order': order
    })

def classmate_create(request):
    if request.method == 'POST':
        form = ClassmateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sitepages:classmates_list')
    else:
        form = ClassmateForm()
    return render(request, 'sitepages/classmate_form.html', {'form': form})
