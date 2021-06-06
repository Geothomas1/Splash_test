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
        tag=['LNRS+Data+Services+Limited', 'Rates+n%27+Deals+:+Cheap+Flights+-+Cheap+Hotels', 'Deutsche+Lufthansa+AG', 'KLM+Koninklijke+Luchtvaart+Maatschappij+N.V.', 'Travel+Booking+Apps+LLC+-+Flights+%26+HOtels', 'Jetcost', 'ebookers', 'Akbar+Travels', 'Cheap+Flights+Bookings', 'Any.Travel', 'upCurve+Business+Services+Pvt+Ltd', 'Resumetravel.com', 'Air+India', 'EmiratesGroup', 'AIR365', 'Flight+Booking+App+by+FareFirst', 'SkyGuru+Inc.', 'Cheap+Flight+Booking+Company+Private+Limited.', 'tripbuk', 'Qatar+Airways', 'FlightConnections.com', 'Eros+Tours+and+Travel', 'Weather+or+Not+Apps', 'Hitlist', 'ibuybooking.com', 'easyJet+Airline+Company+Limited', 'Flyin', 'Cheap+Flights+Developers', 'Etihad+Airways+P.J.S.C', 'Cheap+Flights+Tickets+App', 'CHEAP+FLIGHTS', 'EGYPTAIR+Airlines', 'Ryanair+Limited', 'Go+Airlines+%28India%29+Limited', 'rehlat.com', 'LunaJets+SA', 'Brussels+Airlines+NV/SA', 'Singapore+Airlines+Limited', 'Flights+%26+Hotels+Inc', 'Travelin+Holdings+LLC+-Cheap+Flights+%26+Hotels', 'Air+Arabia', 'Caribbean+Airlines+Limited', 'Flio+Ltd', 'Travelscompare', 'Flight+Booking+App+by+SkyFly', 'Cheap+Flights+Finder:+airfare,+cheap+hotel+booking', 'Cheap+Travel+Deals+by+Traveloji.com', 'Travel+Booking+Holding+LLC+-+Flights+%26+Hotels', 'eDreams+Mobile', 'Pegasus+Airlines', 'TripIt,+Inc.', 'Travel+Booking+ltd.', 'VUELING+AIRLINES+SA', 'TrackingTopia','PlaneEnglish', 'Bookingautos+SL', 'Gulf+Air+B.S.C.+%28C%29', 'Oman+Air', 'Travel+Huge', 'British+Airways+plc', 'Travelstart', 'Last+minute+deals+on+Hotels+%26+All+Airline+bookings', 'Cheap+Tickets+Finder+ltd.', 'Naquadria+Apps', 'Bookinglo+Travels', 'Traavel', 'Jazeera+Airways+K.S.C', 'Airline+Tickets+%E2%80%94+AgentGo+LTD.', 'Last+Minute+Booking+Deals+LLC', 'Cheap+Plane+Tickets+Ltd', 'Norwegian+Air+Shuttle+ASA', 'Avia+Tickets', 'Turkish+Airlines', 'Flight+Apps', 'AIRFRANCE+S.A.', 'Air+India+Express', 'Pakistan+International+Airlines', 'Gobooking+LLC', 'Discover+Ukraine+LLC', 'Flift', 'FareHawker.com', 'GoFlights+%2B+Hotels', 'Booking+Company+LLP+-+Flights+%26+Hotels', 'Flowapps', 'Airtravel', 'HotelsCity.Net', 'Zenmer', 'F%26Y+Group', 'South+African+Airways+%28SOC%29+Ltd', 'Jiyasha+Tour+and+Travel+Pvt+Ltd.', 'SriLankan+Airlines', 'FlightsHunter', 'Hopper+Inc.', 'Cheap+Flights+apps', 'AirTickets+Avia', 'Al+Tayyar+Group', 'La+Compagnie+Nationale+Royal+Air+Maroc+S.A.', 'The+Holy+Bible', 'GMA+Apps', 'Hotel+Booking', 'Hotelekart.com', 'pinkfroot+limited', 'Sky+Mania', 'Flight+booking+best.', 'Delta+Air+Lines,+Inc.', 'CRSCAWP', 'Best+Travel+Tools', 'American+Airlines,+Inc.', 'United+Airlines', 'Hotel+Booking+by+Hotelard', 'Philippine+Airlines,+Inc.', 'Airline+Tickets+Scanner', 'wcifly', 'SolutionOn', 'Airline+Flight+Status+Tracking', 'grandcastor']
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

        
