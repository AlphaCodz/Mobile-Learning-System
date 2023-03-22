from rest_framework.decorators import APIView
from rest_framework.response import Response

class BaseView(APIView):
    required_post_fields = set()
    
    def post(self, request, format=None):
        for field in self.required_post_fields:
            if not request.data.get(field):
                res = {
                    "res": 400,
                    "message": f"{field} is required"
                    
                }
                return Response(res, 400)
            
                