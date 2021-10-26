from .models import *


def get_provider():
    provider = Provider.objects.all()
    return provider