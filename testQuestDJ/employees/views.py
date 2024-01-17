import json
from typing import Any

from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Employees, Positions



def index(request):
    start_employees = Employees.objects.filter(position__weight = 0)
    data = {
        "title": "Головна сторінка",
        "employees" : start_employees,
    }
    return render(request, "employees/index.html", context=data)


class IndexPage(ListView):
    model = Employees
    template_name = "employees/index.html"
    context_object_name = 'employees'
    extra_context = {
        "title": "Головна сторінка"
    }

    def get_queryset(self) -> QuerySet[Any]:
        return Employees.objects.filter(position__weight = 0)
    

@csrf_exempt
def get_employees_by_manager_id(request):
    if request.method == "POST" and "id" in request.POST:
        employees = Employees.objects.filter(manager__pk=request.POST["id"])
        employees_json = json.loads(serialize('json', employees))
        
        for e in employees_json:
            position_id = e['fields']['position']
            position_name = Positions.objects.get(pk=position_id).name if Positions.objects.filter(pk=position_id).exists() else None
            e['fields']['position'] = position_name

        return JsonResponse(employees_json, safe=False)

    return JsonResponse({"error": "Invalid request"}, status=400)