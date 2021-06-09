import email
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import get_user_model

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

@csrf_exempt
def add(request):
  print("comes in the add method backend----", request)
  if request.method == "POST":
        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST.get('userObj','')
        print("userObject---------", email)
        # user_id = id
        # transaction_id = request.POST['transaction_id']
        # amount = request.POST['amount']
        # products = request.POST['products']

        # total_pro = len(products.split(',')[:-1])

        # # UserModel = get_user_model()

        # # try:
        # #     user = UserModel.objects.get(pk=user_id)
        # # except UserModel.DoesNotExist:
        # #     return JsonResponse({'error': 'User does not exist'})

        # usr = User(user=user, product_names=products, total_products=total_pro,
        #              transaction_id=transaction_id, total_amount=amount)
        # usr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order placed Successfully'})
