import requests
import datetime

from pushbullet import Pushbullet

MANUEL_API_KEY = "o.ljGBVC4ULs1AKVz4jOmsJvFN5HACerdA"
GEO_API_KEY = "o.hr2EppbiOJvH8aRBRBoV5bUf4iPpXwtn"

state = '17'
district = '307'
pincode = '686681'

today = datetime.datetime.now().strftime("%d-%m-%Y:%I  %I:%M:%S %p")
date_1 = (datetime.date.today() +
          datetime.timedelta(days=1)).strftime("%d-%m-%Y")
# date_2 = (datetime.date.today() +
#           datetime.timedelta(days=2)).strftime("%d-%m-%Y")
# date_3 = (datetime.date.today() +
#           datetime.timedelta(days=3)).strftime("%d-%m-%Y")

print('*********************************************************************')
print('STARTS : '+ today)
print('*********************************************************************')

print('Execution started at ' + today)
print('Requesting to the API for the date : ' + date_1 + ' in district : ' + district)
# print(date_2)
# print(date_3)

# api = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
# api = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/'+ state
# api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode='+ pincode +'&date=' + date_1
# api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+ pincode +'&date=' + today
api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + district + '&date=' + date_1

res = requests.get(
    api, headers={'content-type': 'application/json', 'User-Agent': ''})

print('Response fetched')
print('Processing Response')

if res.status_code == 200:
    if 'sessions' in res.json().keys():
        print(res.json()['sessions'])
    elif 'centers' in res.json().keys():
        for center in res.json()['centers']:
            if center['name'] in ['Punnekkad PHC', 'Kuttampuzha FHC', 'Neriamangalam FHC']:
                print(center['name'])
                for session in center['sessions']:
                    print(session)
                    if session['available_capacity'] > 0 and session['min_age_limit'] == 18 and session['available_capacity_dose1'] > 0:
                        pb = Pushbullet(MANUEL_API_KEY)
                        push = pb.push_note('There is VACCANT SLOTS in center' + center['name'], 'Poi Vaccine edukkado!')
                        print('There is vacant slots, notification pushed')
        print('Processing Completed')
    else:
        print('Keys not found : sessions, centers in the response')
else:
    print('Something wrong, responded with status :  ' + res.status_code)



district = '304'
pincode = '686546'

print('Requesting to the API for the date : ' + date_1 + ' in district : ' + district)
# print(date_2)
# print(date_3)

# api = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
# api = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/'+ state
# api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode='+ pincode +'&date=' + date_1
# api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+ pincode +'&date=' + today
api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + district + '&date=' + date_1

print('Response fetched')
print('Processing Response')

if res.status_code == 200:
    if 'sessions' in res.json().keys():
        print(res.json()['sessions'])
    elif 'centers' in res.json().keys():
        for center in res.json()['centers']:
            if center['name'] in ['Thrikodithanam PHC', 'Paippadu FHC']:
                print(center['name'])
                for session in center['sessions']:
                    print(session)
                    if session['available_capacity'] > 0 and session['available_capacity_dose1'] > 0:
                        if session['min_age_limit'] == 45 or session['min_age_limit'] == 18:
                            pb = Pushbullet(GEO_API_KEY)
                            push = pb.push_note('There is VACCANT SLOTS in center' + center['name'], 'Poi Vaccine edukkado!')
                            print('There is vacant slots, notification pushed')
        print('Processing Completed')
    else:
        print('Keys not found : sessions, centers in the response')
else:
    print('Something wrong, responded with status :  ' + res.status_code)


today = datetime.datetime.now().strftime("%d-%m-%Y  %I:%M:%S %p")
print('*********************************************************************')
print('ENDS : '+ today)
print('*********************************************************************')