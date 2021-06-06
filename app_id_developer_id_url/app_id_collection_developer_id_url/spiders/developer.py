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
        tag=['extraappdevelopers', 'shadrin.software', 'Kite+games', 'AmaroApps', 'The+Bright+Apps', 'Algorerabin', 'SolLabDev', 'katamapps', 'avinash_42', 'The+Mark+Rider', 'Spotify+Ltd.', 'Pampered+Bytes', 'nasolutions', 'Harshel+David', 'Kailash+Dabhi', 'Awesome+App+Developer', 'S.s', 'Charli', 'EasterEgg', 'MANOJ+G', 'DevCoder', 'Bro+code', 'Ask+Your+Android', 'Handroid', 'Muhammad+Sijjeel', 'AppX+Studio', 'Colorfit', 'Mahindra+Apps', 'Photos+Gallery+Studio', 'Bhima+Apps', 'Draw+apps+for+free', 'Image+Crop+n+Wallpaper+Changer', 'Logolab+-+Logo+Maker+%26+Graphic+Studio', 'Laura+P%C3%A1ez', 'Focus+apps', 'Creative+APPS', 'Luffabelle', 'Devkrushna+Infotech', 'Evening+East+Production', 'artsoftech', 'Raed+Mughaus', 'ArtIdeas.io', 'BestTokVideos', 'Jack+Soeharyo', 'NN+Centrex+Solutions', '4Axis+Technologies', 'KDMedia', 'A-one+Studio', 'AppTrends', 'Andro+Tools', 'FreeSharpApps', 'Samsung+R%26D+Institute+Bangladesh', 'Legion+of+Art', 'Marcel+For+Art', 'Trends+App', 'Name+Art', 'Marcin+Lewandowski', 'BSMJ+apps', 'ARPHN', 'devlord', 'DrawAPP', 'Canva', 'Piyush+Patel', 'Islamic+Lectures', 'Milan+Zarecky', 'godwit+studios', 'vegan+lifestyle', 'MK+Embroidery+Design', 'Insitu+Art+Room', 'Pavaha+Lab', 'Tanager+Apps', 'TapNation', 'Andromida+apps', 'anina', 'Little+App+Store', 'Apps+Specials', 'vertido.io', 'regitaapp', 'AppSelect.org', 'Creative+Apps+Factory', 'Cute+Wallpapers+Studio', 'Adobe+Inc', 'Peli+Ngacengan', 'Sitd212', 'Apps+You+Love',
'UlmDesign', 'yulianiAPP', 'One+Stop+Solutions+RK', 'Dwaraka+INC', 'Free+Mobile+Shop+Apps', 'King+Star+Studio', 'fusion+developers', 'ASHAI', 'Design+Art+Studio', 'Utech', 'NPOL+GAME', 'Mobi+App+%26+Thumbnail+Maker+Inc', 'bbsdroid', 'noku.teku+software', 'Artrooms+LLC', 'Jim+Britain', 'Sanketika', 'New+Kids+Games', 'juliusapps', 'Creativity+Unlimited', 'G+Infosoft', 'AI-Team', 'OMG+Girls+Games', 'EJTech', 'Magic+World+Of+Apps', 'Looster', 'B+-+Studio', 'BBuzzArt+Co,+Ltd', 'Technozer+Solution', '%C5%9E%C3%BCkriye+Can', 'wanda+app', 'norsil', 'Blue+Brain+Technologies', 'EasyDIY', 'constructionsolution', 'pictdroid', 'Asian+Paints', 'Z+Mobile+Apps', 'vipapps', 'Topping+Homestyler+%28Shanghai%29+Technology+Co.,+Ltd', 'Video+Play+Songs', 'VinTool+Studio', 'Aslan+Studio', 'SNS+Dev', 'True+Fun+Apps', 'Suit+Photo+Editor+Montage+Maker+%26+Face+Changer', 'HD+Technolabs', 'Prestige+Studio', 'Corel', 'App+Zonee', 'Designs+4+U', 'HRN+Studios', 'Ms.+Beautician', 'Natenai+Ariyatrakool', 'Xtell+Technologies', 'Cruise+Infotech', 'MooAppMaster', 'KU+Tech', 'IRCTC+Official', 'SpiceJet+Limited', 'InterGlobe+Aviation+Limited', 'TechMart', 'Airbus+Group', 'BELAVIA+-+Belarusian+Airlines', 'StaffTraveler+Solutions+B.V.', 'EaseMyTrip:+IRCTC+Official+Booking+Partner', 'Airports+Authority+of+India', 'Tajawal.com', 'Amadeus+IT+Group+SA', 'AirNav+Systems+LLC', 'Tata+SIA+Airlines+Ltd.', 'Jetsmarter', 'Hotel+Booking+by+Traveldealo', 'flydubai+Airline', 'AIRPAZ', 'Low+Fare+Flights', 'RecipesDaily', 'Best+Travel+Store,+Inc.', 'Jet+Airways+%28India%29+Ltd.', 'Last+Minute+One+Travel+GmbH', 'Cheap+Airlines+tickets+%26+Hotel+Booking+App', 'flight%26hotelguru', 'Last+Minute+Booking+Corp.', 'Travel+buddy+experience', 'Last+Minute+Travel+Corp', 'preeminence+lab', 'W+K+travel,+Inc.']
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

        
