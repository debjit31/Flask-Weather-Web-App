from flask import Flask, render_template, request
import requests

app = Flask(__name__)

## "GET" Method corresponds to page reload
## "POST" Method corresponds to api call using submit buttn
@app.route('/', methods=["POST", "GET"])
def index():
    city = "Howrah"
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8e8940d777f4245501bcab9be4153fba'
    if request.method == "POST":
        city = request.form["city"]
        r = requests.get(url.format(city)).json()
        weather = {'city' : city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon']}
    else:
        r = requests.get(url.format(city)).json()
        weather = {'city' : city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon']}
    return render_template("weather.html", weather = weather)

if __name__ == "__main__":
    app.run(debug = True)
