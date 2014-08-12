from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from ws_client.client import resolve_country_from_ip


class ShowIPView(View):
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        result = resolve_country_from_ip(ip)
        return render_to_response('ip.html', {'ip_info': result}, RequestContext(request))


class LoginView(View):
    def post(self, request, username, password):
        pass


class IPServiceView(View):
    def get(self, request, ip_address):
        pass
