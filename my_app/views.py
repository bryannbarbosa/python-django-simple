from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class MicroService(View):
    def get(self, request):
        return JsonResponse({"example": "get"})
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MicroService, self).dispatch(request, *args, **kwargs)
    def post(self, request):
        return JsonResponse({"example": '1'}, safe=False)
    