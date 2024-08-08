from django.shortcuts import render, redirect
from .models import FirstTable, Commentaries
from .forms import FirstTableForm, CommentariesForm
# Create your views here.


def news_home(request):
    news = FirstTable.objects.all()
    if request.method == 'POST':
        form = CommentariesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')


    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = FirstTableForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/news')

        else:
            error = "Неверная форма заполнения"
    form = FirstTableForm()
    data = {'form': form,
            'error': error}

    return render(request, 'news/create.html', data)


def result_anime(request):
    return render(request,'news/result_anime.html')

