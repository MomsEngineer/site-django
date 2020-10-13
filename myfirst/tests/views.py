from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Test, Comment

def index(request):
    latest_tests_list = Test.objects.order_by('-pub_date')[:5]
    return render(request, 'tests/list.html', {'latest': latest_tests_list})


def detail(request, test_id):
    try:
        a = Test.objects.get(id = test_id)
    except:
        raise Http404("Test not found")

    latest_comments = a.comment_set.order_by('-id')[:10]
    return render(request, 'tests/detail.html', {'test': a, 'latest_comments': latest_comments})


def comment(request, test_id):
    try:
        a = Test.objects.get(id = test_id)
    except:
        raise Http404("Test not found")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('tests:detail', args = (a.id,)))
