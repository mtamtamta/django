from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Avg, Min, Max, StdDev
from .models import ProgramEntry
from .forms import ProgramEntryForm

def entry_create(request):
    if request.method == 'POST':
        form = ProgramEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:entry_list')
    else:
        form = ProgramEntryForm()
    return render(request, 'edu/entry_form.html', {'form': form})

def entry_list(request):
    qs = ProgramEntry.objects.all()

    # фильтр по названию программы
    program_filter = request.GET.get('program_name', '').strip()
    if program_filter:
        qs = qs.filter(program_name__icontains=program_filter)

    # сортировка
    order_by = request.GET.get('order_by')
    allowed = ['full_name', '-full_name',
               'program_name', '-program_name',
               'year_of_admission', '-year_of_admission',
               'gpa', '-gpa']
    if order_by in allowed:
        qs = qs.order_by(order_by)

    # статистика по GPA
    stats = qs.aggregate(
        total=Count('gpa'),
        sum_gpa=Sum('gpa'),
        avg_gpa=Avg('gpa'),
        min_gpa=Min('gpa'),
        max_gpa=Max('gpa'),
        stddev_gpa=StdDev('gpa'),
    )

    return render(request, 'edu/entry_list.html', {
        'entries': qs,
        'program_filter': program_filter,
        'order_by': order_by,
        'stats': stats,
    })
