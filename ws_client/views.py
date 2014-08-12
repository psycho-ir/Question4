from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from geoip2.errors import AddressNotFoundError
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
        import geo_reader

        try:
            country_name = geo_reader.get_info(ip_address).name

        except Exception as e:
            return HttpResponse('{"name":"%s"}' % str(e), mimetype='application/json')
        return HttpResponse('{"name":"%s"}' % country_name, mimetype='application/json')

