import scrapy
from scrapy_splash import SplashRequest

main_list=[]
script = """
                    function main(splash,args)
                        splash:set_viewport_size(1028, 10000)
                        splash:go(args.url)
                        local scroll_to = splash:jsfunc("window.scrollTo")
                        scroll_to(0, 2900)
                        splash:wait(8)
                        return {
                            html = splash:html()
                        }
                    end
                  """

#url=['https://play.google.com/store/apps/developer?id='+i for i in tag]
class DeveloperSpider(scrapy.Spider):
    name = 'developer'
    allowed_domains = ['x']
    def start_requests(self):
        tag=['%C2%AB%D0%AD%D0%B9%D1%80%D0%BB%D0%B0%D0%B9%D0%BD%D1%81+%D0%90%D1%8D%D1%80%D0%BE%C2%BB', 'Tisdao+-+Destination', 'Adam+McNulty', 'Last+Minute+Booking+Deals+LLP', 'Last+minute+deals+-+Flights+ticket+%26+hotel+booking', 'orbitz.com', 'Dopetech+Ltd.', 'KRBSoft', 'Vols+Pas+Chers+ltd', 'Appay+Limited', 'Universal+Travel+%26+Tour%27s', 'vishnukharate', 'Flights+And+Hotels+by+Webuybooking.com', 'idealo+internet+GmbH', 'Arik+air+limited', 'AGRSoft', 'Low+Cost+Booking+By+Traveldigo.com', 'Sastaticket.pk', 'CoolMaterial', 'FastTreck+Networks', 'Best+Travel+Tools+App', 'Hi-Class+Apps:+Gps+Route+Finder,+Maps+%26+Navigation', 'Go+Voyages', 'Tracking+Hub', 'Direct+Collection', 'MyA2zTrip', 'Faceballs', 'CodingRealLife', 'Justfly+Corp.', 'Digitalaya+Technologies', 'Mohamed+Allauun', 'Temar+Apps', 'ATPL+App+Team', 'OAG+Aviation+Worldwide+Limited', 'Travel+Tickets+Ltd', '4G+Entertainment+Apps', 'App+Media+%26+Entertainment', 'Slidescope+Digital+Marketing', 'Rising+TechLabs', 'CBDASH+INFOTECH+LLP.', 'Headway+Labs', 'RP+Apps', 'Sumit+Koul', 'aNiApps', 'Suresh+Kheni', 'Educom+Apps', 'Code20', 'BHARAT+PATIL', 'Goncharov+Mikhail', 'NAMASTE', 'Webster+Province', 'BeeTravl', 'Mobtech.RMMB', 'N.Shanmugasundaram', 'mjapps', 'EK+Studio', 'FlightAware', 'Bits%26Coffee', 'WELLY+GROUP+PTE.+LTD.', 'Strava+Inc.', 'Zeopoxa', 'Fitbit,+Inc.', 'MotiFIT+Fitness+Inc.', 'Huami+Inc.', 'Redlio+Designs', 'TheFabulous', 'Tom+Tietze', 'Cardiogram,+Inc.', 'HealthifyMe+%28Calorie+Counter,+Weight+Loss+Coach%29', 'ITO+Technologies,+Inc.', 'Smart+Wearable+Devices', 'MyFitnessPal,+Inc.', 'wellcrafted', 'Stridekick', 'B-Walter+Software+Engineering', 'btwb', 'Walkingspree+USA,+LTD', 'Aditya+Birla+Health', 'Divine+Fitness+Group', 'Micro+Technology', 'Pacer+Health', 'Codoon+Inc.', 'Activy', 'ASICS+Digital,+Inc.', 'appyhapps.nl', 'BestFit+-+Fitness+App', 'Huawei+Internet++Service', 'StepSetGo+-+SSG', 'Wombat+Apps+LLC', 'BodyFast+GmbH', 'Abvio+Inc.', 'Tinderhouse+Ltd', 'Wahoo+Fitness', 'Nukefuelled', 'Actxa,+Pte+Ltd', 'furo.fit', 'MyKronoz', 'Michiel+Janssen', 'Healthathon+Tech+Pvt.+Ltd.', 'Workout+for+a+cause', 'Wagr', 'MapMyFitness,+Inc.', 'Lifesum', 'GOQii+Inc', 'Sweat', 'Lifetrons+Software+Pvt.+Ltd.', 'CT+App+Team', 'StepsApp', 'FitTrack', 'StepUp+Labs', 'Nutritionix', 'ACTIVE+Network,+LLC', 'Sweatco+Ltd', 'Daily+Strength', 'RaceRunner+Inc.', '3PLUS+international+Inc.', 'Fossil+Group,+Inc.', 'MacroFit+Inc', 'Imagine+Marketing+Private+Limited', 'LIVESTRONG', 'Public+Health+England+Digital', 'OneZeroBit', 'by+Worldofplay', 'Vimo+Labs', '0x7a69+Inc.', 'AnkovoDev', 'fitzeee.com', 'homeworkout', 'mCube+Inc.', 'Smart+Wear', 'InUmbra+Hubert+Wilczy%C5%84ski', 'Pineapple+infotech', 'Health+and+Fitness+Apps+Group', 'Fitzeee+Fitness', 'SelahSoft', 'Andrii+Kudriavtsev', 'Keep+Walking+Health+Group', 'Deniss+Kaibagarovs', 'Easy+Health+Group', 'AppFlo', 'Zulumaniya', 'Elia+Marzia', 'Vitaliy+Bilov', 'Tracker+Pro', 'Portronics+Digital+Pvt+Ltd', 'Stuart++Lee+Scott', 'OnePlus+Spain', 'TOH+Fitness+Team', 'sdgcode', 'Divine+Mobile+Applications', 'NJ_YueXun', 'Adsmart+Baolun+Technology+Ltd.', 'Super+Fitness+APP', 'Tempo+Fitness', 'AX+Technologies', 'Sakar+International,+Inc.', 'apps+4+life', 'Russell+Arms', 'Mobile+Action', 'M.+J.+Stam', 'The+App+Company+INC', 'MUSHTRIP+LTD', 'David+Hruby', 'W5', 'CloudSport+Inc.', 'Simple+Apps+Studios', 'Himanshu+Shekher+Jha', 'SoulApps', 'appscell', 'Dynamo+Sports', 'Million+Concept+Electronic+Shenzhen+Co.,ltd', 'Beijing+Kangshuo+Information+Technology+Co.,Ltd', 'kino2718', 'Omicron+Studio', 'AGI+Applications', 'Greateck', 'Enhance+Studio', 'Desco+Zone', 'ATracker', 'Jung+Woo+Moon', 'Fitness+%26+Pedometer', 'Craig+Electronics+Inc.', 'Media+Marketing+365+Inc.', 'Tow+Kay+Wong', 'Soft+Team+Production', 'NeoTurath+Media', 'Cool+Apps+Creation', 'Primis+Digital', 'GB7+Apps', 'FarBug', 'Latitude+Limited', 'Crick+Sports+Developer', 'Pijus+Chanda', 'Mindfulness+Development', 'ImmortalAK', '313+Apps', 'BGCI', 'Svekolka', 'App+Holdings', 'Healthquad', 'Strong+Fitness+PTE.+LTD.', 'AllTrails,+LLC', 'Brad+Erkkila', 'Game+Expo', 'Skisoft+Games+Studio', 'Final+Punch', 'Playtime+Gaming', 'Fighting+Gamerz', 'Dandio+Games', 'MK+Games+Studio', 'Mind+Craft', 'Candy+Mobile', 'Tappy+Sports+Games', 'Checkmate+Creative+LLC', 'Mini+Sports', 'Fighting+Arena', 'World+Sports+Arena', 'Playsoft+Studios', 'Dragon+Code', 'Fighting+Sports', 'Top+Fun+Sports', 'Siyal+Gamers', 'MiniClub+Studio', 'Webcapacity+Incorporated', '3D+Fun+Games+For+Free', 'Game+Factory+2020', 'RVG+Software+ltd']
        for i in tag:
            url='https://play.google.com/store/apps/developer?id='+i
            yield SplashRequest(url, self.parse,  endpoint='execute', args={'lua_source': script, 'url': url})
        

    def parse(self, response):
        app_id_list=[]
        app_id=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract() 
        for link in app_id:
            app_id_list.append(link.split('=')[-1])
        for x in app_id_list:
            main_list.append(x)
        #print(main_list)
        temp_list = []
        for i in main_list:
            if i not in temp_list:
                temp_list.append(i)
        print(len(temp_list))
        print(temp_list)  

        
