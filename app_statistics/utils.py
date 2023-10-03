from typing import Dict
import requests


class LocationAPI:

    def get_location(self, ip: str) -> Dict:
        error, city, region, country_name = self.ip_api(ip)
        if error:
            city = region = country_name = "Not recognized"
        location_data = {
            "ip": ip,
            "city": city,
            "region": region,
            "country": country_name
        }
        return location_data

    def ip_api(self, ip):
        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        print(response)
        error = True if response.get("status") == 'fail' else False
        return error, response.get("city"), response.get("regionName"), response.get("country")


location_api = LocationAPI()
