from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    title = 'Лев Толстой - зеркало русской революции'
    context = {
        'slug': slug,
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
