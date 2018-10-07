from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from .settings import BUS_STATION_CSV
from django.conf import settings


csvfile = BUS_STATION_CSV
# with open(csvfile, newline='', encoding='utf-8') as f:
#     reader = csvfile.DictReader(f)
#     for row in reader:
#         print(row)

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
        'current_page': 1,
        'prev_page_url': None,
        'next_page_url': 'bus_stations/?page=2',
    })

