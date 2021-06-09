from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    return JsonResponse({'info': 'Django React Course', 'name': "Sharat"})
