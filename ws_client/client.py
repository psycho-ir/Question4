__author__ = 'soroosh'
from suds.client import Client

client = Client('http://www.webservicex.net/geoipservice.asmx?wsdl')


def resolve_country_from_ip(ip_address):
    return client.service.GetGeoIP(ip_address)


if __name__ == '__main__':
    a = resolve_country_from_ip('192.168.101.20')
    print a.CountryCode
    print a.CountryName
    print a.IP
    print a.ReturnCode
    print a.ReturnCodeDetails




