import requests
import json


url = "https://community-open-weather-map.p.rapidapi.com/forecast"
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "7ff2db9df5msh7c41674b7408448p10ab7bjsnf12b86c8aff1"
    }


def req_api():
    my_cities = ["Tbilisi", "Rustavi", "Batumi"]
    data = []
   
    j= 1
    for i in my_cities:
        querystring = {"q":"","units":"metric"}
        querystring["q"] = i
        response = requests.request("GET", url, headers=headers, params=querystring).text

        dict_responce = json.loads(response)  
       
        for item in dict_responce["list"]:
            
            append_data = (
                j,
                dict_responce["city"]["name"],
                item["main"]["temp"],
                item["dt_txt"],
                item["weather"][0]["description"]
            )
            data.append(append_data)
            j+=1
       
    return data


