# This is a sample Python script.
import requests, json


def request_data():
	city = 'bordeaux'
	unit = 'metric
	request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={unit}"
	r = requests.get(request)
	return r.json()


def parse_data(data_to):
	data = {}
	data_temp = data_to['weather'][0]
	data['weather'] = data_temp['main']
	data['description'] = data_temp['description']
	data_temp = data_to['main']
	data['temp'] = data_temp['temp']
	data['pressure'] = data_temp['pressure']
	data['humidity'] = data_temp['humidity']
	data['wind'] = data_to['wind']['speed']
	return data


def main():
	data = parse_data(request_data())
	beauty_string = f"The weather is {data['weather']} with a {data['description']}. It will be {data['temp']}°C with a pressure of {data['pressure']}bar and a humidity of {data['humidity']}%. The wind is blowing at {data['wind']}Km/H"
	return beauty_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	print(main())
