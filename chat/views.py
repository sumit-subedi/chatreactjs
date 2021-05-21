from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.models import User

from chat.serializers import *

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from .models import *

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def messages(request):
    if request.method == 'GET':
        messages = message.objects.all()
        serializer = messageSerializer(messages, many = True)
    
        return JsonResponse(serializer.data, safe = False)

@csrf_exempt
@api_view(['POST'])
def user(request):
    
    
        
    name = request.data['username']
    try:
        user = User.objects.create_user(username=name)
        user.set_unusable_password()
        user.save()
        token = Token.objects.create(user=user)
        print(token)
        return JsonResponse({'message':'Sucessful', 'token':token.key}, safe=False, status = 200)
    except Exception as e:
        print(e)
        return JsonResponse('Invalid username try again with new one' + str(e), safe=False, status = 403)


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@csrf_exempt
# @api_view(['POST'])
def loginuser(request):
    
    user = User.objects.get(username = request.POST['username'])
    if user is not None:
        token = Token.objects.get(user = user)
        return JsonResponse({'message':'Successfully logged in', 'token':token.key}, safe=False, status = 200)
    else:
        return JsonResponse({'message':'Invalid username'}, safe=False, status = 403)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
@api_view(['POST'])
def sendmessage(request):
    messagesent = request.data['message']
    user = request.user
    inst = message(message = messagesent, sent = user)
    inst.save()
    return JsonResponse({'message':'message sent successfully'}, safe = False, status = 200)
