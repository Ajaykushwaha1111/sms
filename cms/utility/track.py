from sms.models import Location_track

def location():
    try:
        import geocoder
        import urllib.request
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        data1 =geocoder.ip(external_ip)
        data =data1.json

    except:
        data={
            'address':"No Address",
            'ip':"localhost",
        }
    return data

def track_location(request,user):
    print(request,user[0])
    data = location()
    location_save =Location_track.objects.create(user=user[0],ip=data['ip'],location=data['address'])
    if location_save:
        return location_save
