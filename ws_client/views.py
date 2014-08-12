import uuid
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from ws_client.client import resolve_country_from_ip
import json
import geo_reader
from datetime import datetime, timedelta

# A fake user pass dict for Login API
registered_users = {'soroosh': 'sarabadani', 'sajjad': 'koochooloo', 'user1': 'pass1'}

# A dict from session_id -> registered_date
sessions = {}



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
    def _get_login_result(self, username, password):
        if registered_users.has_key(username):
            if registered_users[username] == password:
                session_id = str(uuid.uuid4())
                sessions[session_id] = datetime.now()
                return json.dumps({'result': 'OK', 'session_id': session_id})
            return json.dumps({'result': 'ERROR', 'reason': 'wrong password'})
        return json.dumps({'result': 'ERROR', 'reason': 'user does not exist'})

    def get(self, request, username, password):
        return HttpResponse(self._get_login_result(username,password))


def serve(ip_address):
    try:
        country_name = geo_reader.get_info(ip_address).name

    except Exception as e:
        return HttpResponse(json.dumps({'result': 'ERROR', 'reason': str(e)}), mimetype='application/json')
    return HttpResponse(json.dumps({'result': 'OK', 'country_name': country_name}), mimetype='application/json')


class IPServiceView(View):
    def get(self, request, session_id, ip_address):
        if sessions.has_key(session_id):
            threshold_date = datetime.now() - timedelta(minutes=10)
            session_time = sessions[session_id]
            if session_time >= threshold_date:
                sessions[session_id] = datetime.now()
                return serve(ip_address)
            del sessions[session_id]

        return HttpResponse(json.dumps({'result': 'ERROR', 'reason': 'Session is expired'}), mimetype='application/json')


