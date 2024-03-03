from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def sum_numbers(request, num1, num2):
    result = int(num1) + int(num2)
    return render(request, 'result.html', {'num1': num1, 'num2': num2, 'result': result})
