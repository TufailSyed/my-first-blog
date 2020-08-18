from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import CV, TestModel

def cv(request):
    if request.method == 'POST':
        TestModel.objects.create(text=request.POST['TestModel_text'])
        return redirect('/cv/')
        
    TestModels = TestModel.objects.all()
    return render(request, 'cv/cv.html', {'TestModels' : TestModels})