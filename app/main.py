import requests

def get_weather(city):
    API_KEY = "demo"
    url = f"http://wttr.in/{city}?format=3"
    res = requests.get(url)
    print(res.text)

if __name__ == "__main__":
    get_weather("Aracaju")
