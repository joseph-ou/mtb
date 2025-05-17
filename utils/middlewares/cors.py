from django.middleware.security import SecurityMiddleware
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class CorsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print(request)
        if request.method == "OPTIONS":
            return HttpResponse()


    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response