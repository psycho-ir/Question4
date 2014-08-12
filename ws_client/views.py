from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from ws_client.client import resolve_country_from_ip


class ShowIPView(View):
    def get(self, request):
        print request
        result = resolve_country_from_ip('4.2.2.4')
        render_to_response('ip.html', {'ip_info': result}, RequestContext(request))
