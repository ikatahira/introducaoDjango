from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def result_page(request):
    return render(request, 'result.html')

@csrf_exempt
def sum_numbers(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        print(f'num1: {num1}, num2: {num2}')  # Adicione esta linha para depuração
        
        if num1 is not None and num2 is not None:
            try:
                num1 = int(num1)
                num2 = int(num2)
                result = num1 + num2
                return render(request, 'result.html', {'num1': num1, 'num2': num2, 'result': result})
            except ValueError:
                error_message = 'Os valores informados não são números válidos.'
                return render(request, 'result.html', {'error': error_message})
        else:
            error_message = 'Por favor, forneça dois números.'
            return render(request, 'result.html', {'error': error_message})
    else:
        error_message = 'Método não permitido.'
        return render(request, 'result.html', {'error': error_message})
