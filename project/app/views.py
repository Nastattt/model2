from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewsForm
from .models import News


def get_news(request):
    news = News.objects.all()
    return render(request, 'app/news.html', context={'news': news})


def news_add(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            is_published = form.cleaned_data['is_published']
            category = form.cleaned_data['category']
            News.objects.create(title=title, content=content,
                                is_published=is_published, category=category)
            return redirect("news_list")

    else:
        form = NewsForm()
    return render(request, 'app/news_list.html', context={'form': form})


def edit_news(request, news_id=None):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news.title = form.cleaned_data['title']
            news.content = form.cleaned_data['content']
            news.is_published = form.cleaned_data['is_published']
            news.category = form.cleaned_data['category']
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()

    return render(request, 'app/edit_news.html', {'form': form, 'news': news})


def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        news.delete()
        return redirect('news_list')

    return render(request, 'app/delete_news.html', {'news': news})
