from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from polls.models import Question

# Create your views here.
def index(request):
    return HttpResponse(f"{Question.objects.get(pk=1)}")

def question_asked(request):
    questions = Question.objects.all()
    serialized_data = serialize('json', questions)
    return HttpResponse(serialized_data, content_type='application/json')