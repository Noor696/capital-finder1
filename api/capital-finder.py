from http.server import BaseHTTPRequestHandler
import requests # like axios
from urllib import parse
from webbrowser import get


class handler(BaseHTTPRequestHandler): ## versal name function, don't change it

    def do_GET(self):

        
        self.send_response(200)  #200 means ok
        self.send_header('Content-type','text/plain')
        self.end_headers()

        api_path=self.path  
        url_components=parse.urlsplit(api_path)
        query_list=parse.parse_qsl(url_components.query)
        dictionary=dict(query_list)
        country=dictionary.get('country')
        capital=dictionary.get('capital')

        if not country and not capital:
            self.send_response(404)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(str('Invalid entry, please try again').encode())

            return 
        if country:  #country=dictionary.get('country')

            url='https://restcountries.com/v3.1/name/'
            country=dictionary['country']

            r = requests.get(url + country) #will take the url and add country name in the last url
            data = r.json()  #save data in json file
            
            capital=data[0]['capital'][0]

            display=f"The capital of {country} is {capital}"
            self.wfile.write(str(display).encode())

        elif capital:
            url='https://restcountries.com/v3.1/capital/'
            capital=dictionary['capital']
            r = requests.get(url + capital)
            data = r.json()
            country= data[0]['name']['common']
            display=f"{capital} is the capital of {country}."
            self.wfile.write(str(display).encode())
        

        return

