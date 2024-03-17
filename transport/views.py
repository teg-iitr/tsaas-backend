from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from openpyxl import load_workbook
import os


class ReactAppView(View):

    def get(self, request, slug=None):
        try:
            if slug:
                print(slug)
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())
        except:
            return HttpResponse(
                """
                index.html not found !!
                """,
                status=501,
            )


class FaviconView(View):

    def get(self, request, slug=None):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'favicon.ico')) as file:
                return HttpResponse(file.read(), content_type="image/x-icon")
        except:
            return HttpResponse(
                """
                favicon not found !!
                """,
                status=501,
            )


class ManifestView(View):

    def get(self, request, slug=None):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'manifest.json')) as file:
                return HttpResponse(file.read())
        except:
            return HttpResponse(
                """
                manifest.json not found !!
                """,
                status=501,
            )


class ServiceWorkerView(View):

    def get(self, request, slug=None):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'service-worker.js')) as file:
                return HttpResponse(file.read(), content_type='text/javascript')
        except:
            return HttpResponse(
                """
                service-worker.js not found !!
                """,
                status=501,
            )

 # return render(request, 'excel_data.html', {'excel_data': excel_data})
