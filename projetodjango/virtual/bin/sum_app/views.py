from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

def result_page(request):
    return render(request, 'result.html')


def sum_numbers(request):
    num1 = request.POST.get('num1')
    num2 = request.POST.get('num2')
    print(f'num1: {num1}, num2: {num2}')  # Adicione esta linha para depuração
    result = None
    
    if num1 is not None and num2 is not None:
        result = int(num1) + int(num2)
    
    return HttpResponse(f'A soma de {num1} e {num2} é {result}.')
from django.http import JsonResponse

@csrf_exempt
def sum_numbers(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        print(f'num1: {num1}, num2: {num2}')  # Adicione esta linha para depuração
        
        if num1 is not None and num2 is not None:
            try:
                result = int(num1) + int(num2)
                return JsonResponse({'result': result})
            except ValueError:
                return JsonResponse({'error': 'Os valores informados não são números válidos.'}, status=400)
        else:
            return JsonResponse({'error': 'Por favor, forneça dois números.'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)
