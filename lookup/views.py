from django.shortcuts import render

# Create your views here.
import json
import requests
def home(request):
    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=AFB3DEE2-A999-4A1F-8173-3580856E2E99
#      http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=AFB3DEE2-A999-4A1F-8173-3580856E2E99   

    
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=AFB3DEE2-A999-4A1F-8173-3580856E2E99")
    
    if request.method == "POST":
            zipcode=request.POST['zipcode']
            api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=25&API_KEY=AFB3DEE2-A999-4A1F-8173-3580856E2E99")
            

            try:
                api=json.loads(api_request.content)
            except Exception as e:
                api="Error.."
                print(api)
            if len(api)==0:
                return render(request,'home.html')       
            if api[0]['Category']['Name'] == "Good": 
                category_description="Air quality is considered satisfactory, and air pollution poses little or no risk."
                category_color="good"
            elif api[0]['Category']['Name'] == "Unhealthy": 
                category_description="Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                category_color="unhealthy"
            elif api[0]['Category']['Name'] == "Moderate": 
                category_description="Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                category_color="moderate"
            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
                category_description="Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                category_color="usg"
            elif api[0]['Category']['Name'] == "Very Unhealthy": 
                category_description="Health alert: everyone may experience more serious health effects."
                category_color="veryunhealthy"
            elif api[0]['Category']['Name'] == "Hazardous": 
                category_description="Health warnings of emergency conditions. The entire population is more likely to be affected."                   
                category_color="hazardous"
        #     else:
        #             print(api)  
            return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color})

    else:
        try:
                api=json.loads(api_request.content)
        except Exception as e:
                api="Error.."
                print(api)
        if len(api)==0:
                print("Error please try again")        
        if api[0]['Category']['Name'] == "Good": 
                category_description="Air quality is considered satisfactory, and air pollution poses little or no risk."
                category_color="good"
        elif api[0]['Category']['Name'] == "Unhealthy": 
                category_description="Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                category_color="unhealthy"
        elif api[0]['Category']['Name'] == "Moderate": 
                category_description="Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                category_color="moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
                category_description="Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                category_color="usg"
        elif api[0]['Category']['Name'] == "Very Unhealthy": 
                category_description="Health alert: everyone may experience more serious health effects."
                category_color="veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous": 
                category_description="Health warnings of emergency conditions. The entire population is more likely to be affected."                   
                category_color="hazardous"
        #     else:
        #             print(api)  
        return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color}) 

def about(request):
    return render(request,'about.html',{})
        