from django.shortcuts import render
from django.views import generic
from mainapp.models import Student
from django.http import HttpResponse
from django.db.utils import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
import re

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'mainapp/index.html'

def Submit(request):
    try:
        sid = request.GET['sid']
        if not re.match("^\d{8,10}$",sid):
            raise Exception("錯誤的學號: %s" % sid)
        s = Student(sid = sid);
        s.save();
    except MultiValueDictKeyError as e:
        return HttpResponse("請輸入學號");
    except IntegrityError as e:
        return HttpResponse("這個學號 %s 已經領過選票了" % sid)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("學號 %s 領票成功！" % sid)
