__author__ = 'soroosh'

from geoip2.database import Reader

r = Reader('../GeoLite2-Country.mmdb')


def get_info(ip_address):
    return r.country(ip_address).country