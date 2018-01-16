import json
import requests

class railinfobot_api():
    def get_pnrstatus(self, pnr):
        pnr_status=""
        pnrstatus_response = requests.get('https://api.railwayapi.com/v2/pnr-status/pnr/4653246678/apikey/5yx13p9zc3/')
        data = json.loads(pnrstatus_response.text)
        if data['response_code'] == 200:
            for ticket in data['passengers']:
                pnr_status=pnr_status+"BOOKING STATUS: "+ticket['booking_status']+"CURRENT STATUS: "+ticket['current_status']
        else:
            #print("error:cant find pnr")
            pnr_status="Sorry....I am Afraid PNR info not found"

        return pnr_status
    def get_route(self, train_num):
            pass

if __name__=="__main__":
    r=railinfobot_api()
    x=r.get_pnrstatus(4653246678)
    print(x)