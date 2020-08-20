from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import CV, TestModel
from .forms import CVForm
from django.contrib.auth.decorators import login_required

def cv(request):
    cvs = CV.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'cv/cv.html', {'cvs' : cvs})

@login_required
def cv_new(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.published_date = timezone.now()
            cv.save()
            return redirect('cv_edit', pk=cv.pk)
    else:
        form = CVForm()
    return render(request, 'cv/cv_edit.html', {'form': form})

@login_required
def cv_edit(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == "POST":
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.published_date = timezone.now()
            cv.save()
            return redirect('cv')
    else:
        form = CVForm(instance=cv)
    return render(request, 'cv/cv_edit.html', {'form': form})

@login_required
def cv_remove(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    cv.delete()
    return redirect('cv')