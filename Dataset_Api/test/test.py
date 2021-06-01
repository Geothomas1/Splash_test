from google_play_scraper import app
import urllib
import google_play_scraper
import play_scraper
import requests
# import play_scraper
# import scraper
# res=play_scraper.details('com.kinedu.appkinedu')
# print(res['updated'])

# res2 = scraper.app(appId='com.kinedu.appkinedu')
# print(res2['minInstalls'])

# res3=result = app('com.kinedu.appkinedu', lang='en', country='us')
#print(res3['minInstalls'])
mylist=['ml.quickemail.a2048', 'ml.quickemail.miazpro']
c=1
for i in mylist:
    print(i)
    try:
        result = app(i, lang='en', country='in')
        res=play_scraper.details(i)

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
        originalPrice=result['originalPrice']
        androidVersionText=result['androidVersionText']
        developer=result['developer']
        developerAddress=result['developerAddress']
        developerInternalID=result['developerInternalID']
        version=result['version']
        recentChanges=result['recentChanges']
        updated=result['updated']
        last_update=res['updated']
        if(privacyPolicy==None):
            privacyPolicy='N/A'
        if(developerWebsite==None):
            developerWebsite='N/A'
        if(developerAddress==None):
            developerAddress='N/A'
        if(released==None):
            released='N/A'
        print(c)
        c=c+1
        print(app_name)
        print(updated)
        print(size)
        print('orginal price',originalPrice)
        print('adsupport',adSupported)
        print('relesed',released)
        print(privacyPolicy)
        print(developerId)
        print(developer)
        print(developerWebsite)
        print(developerAddress)
        print(released)
        print(currency)
        print(last_update)
        
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




    
    #description=result['description']
    
    #genreId=result['genreId']
    #contentRatingDescription=result['contentRatingDescription']
    
    
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

    
    