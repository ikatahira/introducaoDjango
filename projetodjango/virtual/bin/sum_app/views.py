from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sum_numbers(request, num1, num2):
    result = int(num1) + int(num2)
    return HttpResponse(f'A soma de {num1} e {num2} é {result}.')
    