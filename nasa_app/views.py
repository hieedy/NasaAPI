from django.shortcuts import render
import requests
from pprint import PrettyPrinter
from datetime import date

# Create your views here. 

def fetchAPOD(date_input = None):
    api_key = ''
    url = 'https://api.nasa.gov/planetary/apod'
    pp = PrettyPrinter()

    if  date_input == None:
        params = {
            'api_key' : api_key
        }
    else:
        params = {
            'api_key' : api_key,
            'date' : date_input,
        }

    response = requests.get(url, params).json()
    return response

def apod(request):
 
    if request.method == 'POST':
        print('searching')
        date_in = request.POST.get('date_of_apod')
        data = fetchAPOD(date_in) 
       
      
    else:    
        data = fetchAPOD()
    
    return render(request, 'apod.html', {'data' : data})


########EPIC##############
def fetchEpic(date_input = None):
    api_key = ''
    url = 'https://api.nasa.gov/EPIC/api/natural/date'

    print(date_input)
    params = {
            'api_key' : api_key,
        }
      
    if date_input == None:
       
        response_date = requests.get('https://api.nasa.gov/EPIC/api/natural/available', params).json()[-1]
      
    else:
     
        url += date_input

        response_date = date_input

    
    response1 = requests.get(url, params).json()
    return response1,response_date
    # for item in response:
    #     print(item['image'])



def epic(request):

    result, response_date = None, None
    if request.method == 'POST':
        date_input  = request.POST.get('date')
        result,response_date = fetchEpic(date_input)

    else:
        result,response_date = fetchEpic()
        
    
    response_date = response_date.split('-')
    
    images = []
    print(response_date)

    for item in result:
        images.append(
                {
                'time': item['date'].split(" ")[-1], 
                'img' : item['image'], 
                'caption' : item['caption']
                }
            )
      
    return render(request, 'EPIC.html',{'images':images, 'date': response_date})



