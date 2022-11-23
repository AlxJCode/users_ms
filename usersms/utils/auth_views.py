from .serializer import CustomAuthTokenLoginSerializer, CustomVerifyTokenSerializer
from rest_framework_simplejwt.views import TokenViewBase
from .token_auth import TokenSimpleJWTAuth
from .resp_tools import Resp
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

class CustomTokenObtainPairView(TokenViewBase):
    serializer_class = CustomAuthTokenLoginSerializer

class ValidateTokenView(TokenViewBase):
    serializer_class = CustomVerifyTokenSerializer
    def get(self, request):

        token = None

        if request.COOKIES.get("token"):
            token = request.COOKIES["token"]
        else:
            token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]

        if token:
            try:
                auth_user_id = TokenSimpleJWTAuth.get_user_id_from_token(token)
                user = User.objects.get(pk=auth_user_id)

                data = {
                    "access": str(CustomVerifyTokenSerializer.get_token(user).access_token),
                    
                } 

                return Resp(data_ =data , msg_="Authentication Successfully", code_=status.HTTP_200_OK).send()
            except :
                return Resp(msg_="Error de token", status_=False, code_=status.HTTP_400_BAD_REQUEST).send()

        return Resp( msg_ = "Error de token", status_ = False, code_ = status.HTTP_400_BAD_REQUEST ).send()
