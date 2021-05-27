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

mylist=['com.BestMp3RingtonesCSA', 'com.MostPopularRingtones2017CSA', 'com.ChristmasRingtonesCSA', 'com.Latest2017RingtonesCSA','com.facebook.katana']
c=1
for i in mylist:
    result = app(i,
    lang='en',
    country='us')
    app_name=result['title']
    appId=result['appId']
    category=result['genre']
    rating=result['score']
    count_rated=result['ratings']
    installs=result['installs']
    minInstalls=result['minInstalls']
    free=result['free']
    price=result['price']
    currency=result['currency']
    size=result['size']
    androidVersion=result['androidVersion']
    developerId=result['developerId']
    developerWebsite=result['developerWebsite']
    developerEmail=result['developerEmail']
    released=result['released']
    privacyPolicy=result['privacyPolicy']
    contentRating=result['contentRating']
    adSupported=result['adSupported']
    offersIAP=result['offersIAP']
    editorsChoice=result['editorsChoice']
    summary=result['summary']
    reviews=result['reviews']
    androidVersionText=result['androidVersionText']
    developer=result['developer']
    developerAddress=result['developerAddress']
    developerInternalID=result['developerInternalID']
    version=result['version']

    if(category==None):
        category='N/A'
    if(rating==None):
        rating='N/A'
    if(count_rated==None):
        count_rated='N/A'
    if(installs==None):
        installs='N/A'
    if(minInstalls==None):
        minInstalls='N/A'
    if(free==None):
        free='N/A'
    if(price==None):
        price='N/A'
    if(currency==None):
        currency='N/A'
    if(size==None):
        size='N/A'
    if(developerEmail==None):
        developerEmail='N/A'
    if(androidVersion==None):
        androidVersion='N/A'
    if(privacyPolicy==None):
        privacyPolicy='N/A'
    if(developerWebsite==None):
        developerWebsite='N/A'
    if(developerAddress==None):
        developerAddress='N/A'
    if(released==None):
        released='N/A'
    if(contentRating==None):
        contentRating='N/A'
    if(adSupported==None):
        adSupported='N/A'
    if(offersIAP==None):
        offersIAP='N/A'
    if(editorsChoice==None):
        editorsChoice='N/A'
    if(summary==None):
        summary='N/A'
    if(reviews==None):
        reviews='N/A'
    if(androidVersionText==None):
        androidVersionText='N/A'
    if(developer==None):
        developer='N/A'
    if(developerInternalID==None):
        developerInternalID='N/A'
    if(version==None):
        version='N/A'

    data = [[app_name,
    appId,
    category,
    rating,
    count_rated,
    installs,
    minInstalls,
    free,
    price,
    currency,
    size,
    androidVersion,
    developerId,
    developerWebsite,
    developerEmail,
    released,
    privacyPolicy,
    contentRating,
    adSupported,
    offersIAP,
    editorsChoice,
    summary,
    reviews,
    androidVersionText,
    developer,
    developerAddress,
    developerInternalID,
    version]]
    result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:Y1", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":data}).execute()
    print(result)
    print(c)
    c=c+1
    print(app_name)

    #description=result['description']
    
    #genreId=result['genreId']
    #contentRatingDescription=result['contentRatingDescription']
    #updated=result['updated']
    
    # sale=result['sale']
    # saleText=result['saleText']
    # saleTime=result['saleTime']
    # histogram=result['histogram']
    
  
    #print('description',description)
    # print('summary',summary)
    # print('reviews',reviews)
    # print('originalPrice',originalPrice)
    # print('sale',sale)
    # print('saleText',saleText)
    # print('histogram',histogram)
    # print('offersIAP',offersIAP)
    # print('editorsChoice',editorsChoice)
    # print('androidVersionText',androidVersionText)
    # print('developer',developer)
    # print('developerAddress',developerAddress)
    # print('developerInternalID',developerInternalID)
    # # print('genreId',genreId)
    # # print('contentRatingDescription',contentRatingDescription)
    # #print('updated',updated)
    # print('version',version)
    # print('recentChanges',recentChanges)
    # print('category',category)
    # print('relesed',released)
    # print('content rating',contentRating)
    # print('sale',sale)
    # print('sale text',saleText)
    # print('sale time',saleTime)

    
    