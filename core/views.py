from django.views import View
from django.shortcuts import render


class DashBoardView(View):
    def get(self, request):
        return render(request, "core/dashboard.html")

    def post(self, request):
        pass
