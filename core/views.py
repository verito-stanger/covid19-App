from django.shortcuts import render
import requests
import pprint

url = "https://covid-193.p.rapidapi.com/statistics"
#headers: user and rapidapi-key given by rapidapi
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f08d68db60msha478ddb6499576fp13ad6ajsnc74d4783af5c"
    }

response = requests.request("GET", url, headers=headers).json()
response = response["response"]

countries =[dato['country'] for dato in response] #Lista por compresion
countries.sort()

def home(request):
    if request.method=='POST':
        pais = request.POST['selectedcountry']
        for i in response:
            if pais == i['country']:
                #pprint.pprint(i)
                new = i['cases']['active']
                active = i['cases']['active']
                critical = i['cases']['critical']
                recovered = i['cases']['recovered']
                total = i['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
                
        context = {
            'new': new,
            'active': active,
            'critical': critical,
            'recovered': recovered,
            'total': total,
            'deaths': deaths,
            'pais': pais,
            'countries': countries
        }
        return render (request,'core/index.html', context=context )
    return render(request, 'core/index.html', {'countries': countries})