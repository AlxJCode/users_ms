import traceback
from .token_auth import TokenSimpleJWTAuth
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status

from .resp_tools import Resp

class CustomAuthTokenLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        
        # ...
        return token

    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            refresh = super().get_token(self.user)
            data["refresh"] = str(refresh)
            try:
                """ auth_user_id = TokenSimpleJWTAuth.get_user_id_from_token(data['access'])
                systemuser = SystemUser.objects.get(auth_user = auth_user_id)
                if not systemuser.is_active:
                    return Resp(msg_="Cuenta inactiva",status_=False , code_=status.HTTP_400_BAD_REQUEST).result()
                
                data["user"] =  {
                    "id": systemuser.pk,
                    "name": systemuser.name,
                    "type": systemuser.type
                } """

                return Resp(data_ =data , msg_="Authenticación exitosa").result()
            except:
                return Resp(msg_="Cuenta de Uusario no Activada", status_=False, code_=status.HTTP_400_BAD_REQUEST).result()

        except:
            tb = traceback.format_exc()
            print(tb)
            return Resp(msg_="Usuario y Contraseña Incorrecta",status_=False , code_=status.HTTP_400_BAD_REQUEST).result()

class CustomVerifyTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        
        # ...
        return token

