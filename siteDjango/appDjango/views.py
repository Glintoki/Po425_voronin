from django.shortcuts import render
from django.views import View
from .base import *


class Login(View):
    def get(self, request):
        o_provider = get_provider()

        context = {
            'Providers': o_provider
        }
        return render(request, 'login.html', context=context)