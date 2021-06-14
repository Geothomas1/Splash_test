import time
import urllib
import google_play_scraper
import play_scraper
import requests
from google_play_scraper import app
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID a sample spreadsheet.
SPREADSHEET_ID = '1r1ifW642gcbAxDN6NbktgFhxUMhqRCKJx3CK8E82UsA'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

mylist=[]
print(len(mylist))
c=1
data = []
for i in mylist:
    try:
        result = app(i, lang='en', country='us')
        res=play_scraper.details(i)
        data.append([
            result['title'] if result['title'] != None else  'N/A' if 'title' in result.keys() else  'N/A',
            result['appId'] if result['appId'] != None else  'N/A' if 'appId' in result.keys() else  'N/A',
            result['genre'] if result['genre'] != None else  'N/A' if 'genre' in result.keys() else  'N/A',
            result['score'] if result['score'] != None else  'N/A' if 'score' in result.keys() else  'N/A',
            result['ratings'] if result['ratings'] != None else  'N/A' if 'ratings' in result.keys() else  'N/A',
            result['installs'] if result['installs'] != None else  'N/A' if 'installs' in result.keys() else  'N/A',
            result['minInstalls'] if result['minInstalls'] != None else  'N/A' if 'minInstalls' in result.keys() else  'N/A',
            result['free'] if result['free'] != None else  'N/A' if 'free' in result.keys() else  'N/A',
            result['price'] if result['price'] != None else  'N/A' if 'price' in result.keys() else  'N/A',
            result['currency'] if result['currency'] != None else  'N/A' if 'currency' in result.keys() else  'N/A',
            result['size'] if result['size'] != None else  'N/A' if 'size' in result.keys() else  'N/A',
            result['androidVersion'] if result['androidVersion'] != None else  'N/A' if 'androidVersion' in result.keys() else  'N/A',
            result['developerId'] if result['developerId'] != None else  'N/A' if 'developerId' in result.keys() else  'N/A',
            result['developerWebsite'] if result['developerWebsite'] != None else  'N/A' if 'developerWebsite' in result.keys() else  'N/A',
            result['developerEmail'] if result['developerEmail'] != None else  'N/A' if 'developerEmail' in result.keys() else  'N/A',
            result['released'] if result['released'] != None else  'N/A' if 'released' in result.keys() else  'N/A',
            res['updated'] if res['updated'] != None else  'N/A' if 'updated' in res.keys() else  'N/A',
            result['privacyPolicy'] if result['privacyPolicy'] != None else  'N/A' if 'privacyPolicy' in result.keys() else  'N/A',
            result['contentRating'] if result['contentRating'] != None else  'N/A' if 'contentRating' in result.keys() else  'N/A',
            result['adSupported'] if result['adSupported'] != None else  'N/A' if 'adSupported' in result.keys() else  'N/A',
            result['offersIAP'] if result['offersIAP'] != None else  'N/A' if 'offersIAP' in result.keys() else  'N/A',
            result['editorsChoice'] if result['editorsChoice'] != None else  'N/A' if 'editorsChoice' in result.keys() else  'N/A',
            result['summary'] if result['summary'] != None else  'N/A' if 'summary' in result.keys() else  'N/A',
            result['reviews'] if result['reviews'] != None else  'N/A' if 'reviews' in result.keys() else  'N/A',
            result['androidVersionText'] if result['androidVersionText'] != None else  'N/A' if 'androidVersionText' in result.keys() else  'N/A',
            result['developer'] if result['developer'] != None else  'N/A' if 'developer' in result.keys() else  'N/A',
            result['developerAddress'] if result['developerAddress'] != None else  'N/A' if 'developerAddress' in result.keys() else  'N/A',
            result['developerInternalID'] if result['developerInternalID'] != None else  'N/A' if 'developerInternalID' in result.keys() else  'N/A',
            result['version'] if result['version'] != None else  'N/A' if 'version' in result.keys() else  'N/A'])
        print(c)
        print(result['appId'])
        c=c+1
        # if 40 and (c % 40) == 0:
        #     print("On Sleep 62 sec")
        #     time.sleep(62)
        # print(data)
    
    except urllib.error.HTTPError:
        print('Urllib Error HttpError Skip 1')
        continue
    except google_play_scraper.exceptions.NotFoundError:
        print('google play scraper exception Skip 2')
        continue
    except AttributeError:
        print("Attribute Error Exception Skip 3")
        continue
    except ValueError:
        print('Value Exception Skip 3')
        continue
    except requests.exceptions.HTTPError:
        print('Request Exception Skip 4')
        continue
    except google_play_scraper.exceptions.ExtraHTTPError:
        print("google_play_scraper.exceptions.ExtraHTTPError Skip 5")
        continue
    
result1 = sheet.values().append(spreadsheetId=SPREADSHEET_ID,range="Sheet2!A1:AC1", valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS",body={"values":data}).execute()

    