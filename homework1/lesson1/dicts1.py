from pprint import pprint

weather = {
    "city": "Москва", 
    "temperature": 20
}
print(weather["city"])
weather["temperature"] = weather["temperature"] - 5

pprint(weather)
print(weather.get("country"))
print(weather.get("country", "Russia"))
weather["date"] = "27.05.2019"
print(weather)
print(len(weather))