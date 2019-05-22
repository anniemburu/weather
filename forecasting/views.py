import requests
from django.shortcuts import render
from .forms import CityForm


# Create your views here.
def homepage(request):
    # city = input("Please enter your city: ")
    context = {}

    if request.method == 'POST':

        form = CityForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            api_address = 'https://api.openweathermap.org/data/2.5/forecast?appid=1700866c50e769943e984d0ad6ccc033&q' \
                          '='+request.POST.get('city', '')

            json_data = requests.get(api_address).json()

            day1_weather = {
                'Temperature': str(round(float(json_data['list'][3]['main']['temp']))),
                'Pressure': json_data['list'][3]['main']['pressure'],
                'Weather_Description': json_data['list'][3]['weather'][0]['description'],
                'Wind_Speed': json_data['list'][3]['wind']['speed'],
                'Date': json_data['list'][3]['dt_txt'],
                'Icon': json_data['list'][3]['weather'][0]['icon'],
            }

            day2_weather = {
                'Temperature': str(round(float(json_data['list'][11]['main']['temp']))),
                'Pressure': json_data['list'][11]['main']['pressure'],
                'Weather_Description': json_data['list'][11]['weather'][0]['description'],
                'Wind_Speed': json_data['list'][11]['wind']['speed'],
                'Date': json_data['list'][11]['dt_txt'],
                'Icon': json_data['list'][11]['weather'][0]['icon'],
            }

            day3_weather = {
                'Temperature': str(round(float(json_data['list'][19]['main']['temp']))),
                'Pressure': json_data['list'][19]['main']['pressure'],
                'Weather_Description': json_data['list'][19]['weather'][0]['description'],
                'Wind_Speed': json_data['list'][19]['wind']['speed'],
                'Date': json_data['list'][19]['dt_txt'],
                'Icon': json_data['list'][19]['weather'][0]['icon'],
            }

            day4_weather = {
                'Temperature': str(round(float(json_data['list'][27]['main']['temp']))),
                'Pressure': json_data['list'][27]['main']['pressure'],
                'Weather_Description': json_data['list'][27]['weather'][0]['description'],
                'Wind_Speed': json_data['list'][27]['wind']['speed'],
                'Date': json_data['list'][27]['dt_txt'],
                'Icon': json_data['list'][27]['weather'][0]['icon'],
            }

            day5_weather = {
                'Temperature': str(round(float(json_data['list'][35]['main']['temp']))),
                'Pressure': json_data['list'][35]['main']['pressure'],
                'Weather_Description': json_data['list'][35]['weather'][0]['description'],
                'Wind_Speed': json_data['list'][35]['wind']['speed'],
                'Date': json_data['list'][35]['dt_txt'],
                'Icon': json_data['list'][35]['weather'][0]['icon'],
            }

            context = {
                'day1': day1_weather,
                'day2': day2_weather,
                'day3': day3_weather,
                'day4': day4_weather,
                'day5': day5_weather,
                'form': form,
            }

    else:
        form = CityForm()
        context = {
            'form': form,
        }
    return render(request, 'forecasting/homepage.html', context)
