import http.client
import urllib
import time

key = "S14H8SNRPP3OLY9H"

def thermometer():
	while True:
		temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
		params = urllib.parse.urlencode({'field1':temp,'key':key})
		headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
		conn = http.client.HTTPConnection("api.thingspeak.com:80")

		try:
			conn.request("POST", "/update", params, headers)
			response = conn.getresponse()
			print(temp)
			print(response.status, response.reason)
			data = response.read()
			conn.close()
		except:
			print("connection failed")
			#since program is being run remotely must exit otherwise cannot stop script without task kill in other session
			exit()
		break

if __name__ == "__main__":
	while True:
		thermometer()
