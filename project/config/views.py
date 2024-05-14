from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render


def fecha_hora(request):
    from datetime import datetime

    ahora = datetime.now()
    return HttpResponse(f"<h1>⌛ Fecha y hora: {ahora:%d/%m/%Y %H:%M:%S.%f} </h1>")


