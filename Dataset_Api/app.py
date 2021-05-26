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

mylist=['com.eniseistudio.logistics_management', 'com.eniseistudio.news.estados_unidos', 'com.eniseistudio.dental_assistant', 'com.eniseistudio.course.medical_assistant', 'com.eniseistudio.majors.course.business_administration', 'com.eniseistudio.economics', 'com.eniseistudio.course.cosmetology', 'com.jquiz.python', 'com.eniseistudio.quality_management', 'com.eniseistudio.tourism_management', 'education.kids.learning', 'earlylearn.kidslearningworld', 'desert.runner.boy', 'preschool.kids.abc.tracing', 'kids.word.games', 'earlylearn.kidslearningworld.pro', 'word.link.connect.puzzle', 'earlylearn.math.game', 'best.time.to.get.pregnant.ttf', 'com.communication.in.relationships.ttf', 'smooth.pick.up.lines.ttf', 'types.of.martial.arts.ttf', 'dating.questions.ttf', 'date.ideas.ttf', 'age.gap.relationships.ttf', 'how.to.conceive.a.girl.ttf', 'early.childhood.education.ttf', 'benefits.of.hot.yoga.ttf']
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
    recentChanges=result['recentChanges']
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
    version,
    recentChanges]]
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

    
    