import traceback

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from usersms.utils.resp_tools import Resp
from rest_framework.pagination import PageNumberPagination

class DataView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Resp(
                
        ).send()