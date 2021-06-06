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
        tag=['Lysdrang', 'Kids+Land+Studio', 'Baby+Indian-+Health+Tips+By+Dr.Chandra+Lakshmi', 'netgames834', 'girlyapps', 'Baby+Aadhya+Games', 'moogames', 'bach+games', 'Best+Dress+Up+Games+For+Girls', 'bonbongame.com', 'Sweet+Baby+Girl', 'Vehicle+Info+App', 'Learn+English+In+Hindi+-+Translator+%26+Dictionary', 'Vihas', 'carVertical+O%C3%9C', 'Next+Billion+Apps', 'CARS24+Services+Private+Limited', 'SkyTouch+InfoSoft', 'Poonam+AppsZone', 'Mobifolio', 'AUTO+AID', 'HP+Developers', 'kineapps', 'Extras+Studeio', 'Autovehicles', 'Joseph+Miller%28tamil%29', 'Rufous+Solutions+Inc.', 'Resilient+Lab', 'Vehicle+Owner+Details', 'LilyInc', 'RTO+App+King', 'Avengers+Academy', 'Ketan+Gupta', 'InBill+Solutions', 'JewelStore', 'Indian+RTO', 'IshuInfoTech', 'Shiva+Apps+Studio+2020', 'Gaming+Affliction', 'Ofir+Miron', 'TechDot+Apps', 'MobileCafe', 'Gypsee+Automotive', 'Midas+Apps', 'Game+Pickle', 'RMADE', 'Top+Sm+Apps', 'android+App', 'Mobile+Software+Success', 'Infokombinat', 'Ultra+Video+Player', 'SenSight+Technologies', 'NEELKANTH+ELECTRONICS', 'Blue+Sky+Studio+App', 'Hyperlink+Infosystem', 'binakapps', 'CLEVERBIT', 'SHANKAR+UPPULURI', 'Mantra+Meditation+Music', 'Grand+Robot+Fight', 'Car++Code', 'N.R.C', 'SRC+Infotech', 'Rich+Universe', 'Apps+World+Technologies', 'Vive', 'IMP+Tools', 'ieye', 'I+Best+Apps', 'Naksh+Infotech', 'Best+Car+Wallpapers', 'Era+Fun+Studio+-+Games+for+Boys+and+Girls', 'True+Axis', 'Mustard+Games+Studios', 'MM+Creations', 'Azon+Games', 'Maxamtech+Digital+Ventures+Pvt.+Ltd', 'Freday+AI', 'Trends+Games+Production', 'Tushar+Pingale', 'Gumdrop+Games', 'GT+Action+Games', 'Play+With+Games', 'AussieMan+Gamers', 'CreativeStarApps', 'Maritime+Simulation+Games', 'Mouse+Games', 'Golden+Guns+Studio', 'PuPlus', 'Cradley+Creations', 'Cut-Cutting+Tools', 'Games+Wing', 'GoBumpr', 'Gamez.io', 'Play+10', 'Tok+Tik+Player+Apps', 'LocoNav', 'Brilliant+Gamez', 'Dildar+Photo+Studio', 'ROMOKU+GROUP+PVT.LTd', 'Smart+Steps+Technologies', 'Game+Passport', 'RiseUp+Media+Group', 'Sylvie', 'Play+Street', 'Rto+vehical+information', 'InterBolt+Games', 'Million+games', 'Good+Job+Games', 'Creative+Webmedia+Pvt.+Ltd.', 'Play+Paradigm', 'Awesome+Games+Studios', 'Keemut.com', 'Mr.+A', 'Gamleo+Studio', 'Gaming+Legends', 'Singhuniverseglobal', 'Vinions', 'Glory+Photo+Studio', 'Jima+Apps', 'Ahyan+Apps', 'Zee+Vision+Games', 'GamePod', 'Peak+App', 'Audible,+Inc', 'Sanity+Audio+Apps', 'RB+Audiobooks+USA,+LLC.', 'GIGL+Summaries+-+Best+Hindi+Audiobook+App.', 'Patter+Team', 'Kuku+FM', 'Pratilipi', 'Free+Books+Studio', 'Alex+Kravchenko', 'Oodles', 'Parsida+AB', 'Pocket+FM', 'Open+Free+Books+and+Audiobooks', 'Kahani+Audiobooks', 'Scribd,+Inc.', 'Audiobook+Jungle', 'Dasubhashitam+-+Telugu+Audio+Books', 'Nextory+AB', 'Pinna+LLC', 'Ubook+-+Audiobooks+Revistas+e+Podcasts', 'Paul+Woitaschek', 'AudiobookStore.com', '12min', 'Skeelo', 'Gurukula.com+Sriram+Raghavan', 'Audiobooks', 'Joy+Reading+Culture+Media+Co+Ltd', 'WAKA+CORPORATION', 'Audibook', 'Audiobook+Converter', 'Technocrats.io', 'English+For+EveryOne', 'MyBook', 'Big+Finish', 'Semu+Audiobooks', 'Libro.fm', 'Twist+Idea+LLC', 'Blackstone+Audio+Books', 'rif', 'Iqraaly', 'AudiobooksNow.com', 'Anyreads', 'eMusic.com+Inc.', 'hieulele', 'All+You+Can+Books', 'Audiolibrix', 'E.+B.+Solutions+Pte.+Ltd.', 'Instaread,+Inc.', 'TimeKillers', 'Urdu+Audio+Books', 'galpowala', 'bichitraKo+Inc.', 'Chilling,+LLC', 'mdmt', 'Empik+S.A.', 'upday+GmbH+%26+Co.+KG', 'christianaudio', 'Catholic+Vault+LLC', 'ARITALIT', 'GraphicAudio', 'Pustaka+Digital+Media+Pvt.+Ltd.', 'offBEAT', 'EBSCO+Information+Services', 'UPpack', 'Fonos', 'Golpokotha', 'Auti+Books', 'Gerald+Geiger', 'Yuzhong+Huang', 'Soft+Universe', 'VRG', 'Audioteka+S.A.', 'Studio+71', 'Aneko+Press', '%D0%91%D1%83%D0%BA%D0%BB%D0%B8%D1%81,+%D0%9E%D0%9E%D0%9E', 'BookBeat', 'Audio+Religious+Book', 'Idiomus', 'Sonic+Octaves+Pvt.+Ltd.', 'Tocalivros', 'o16i+Apps', '%EC%9C%8C%EB%9D%BC%28welaaa%29', 'oCoder+App', 'Arena+Developer', 'Kingdom+of+Jesus+Christ,+TNAEN,+Inc.', 'Classy+eBooks', 'tobik%28a%29+-+Tobias+Kausch', 'HB+Developer', 'Rohit+Kanade', 'Audiobooks+NZ', 'Grit+Innovation', 'Madiva', 'Learning+English+Free', 'Speakhub', 'PT+EDIFIKASI+MEDIA+INDONESIA', 'Profound+Mentors', 'auboo.de', 'Sunokitaab+Private+Limited', 'musa+t%C3%BCt%C3%BCn', 'Marcin+Simonides', 'audiotales+org', 'Yelyashev+studio', 'LeanEnglish', 'Team+KBS', 'Suparno+Bose', 'Yolosoft', 'GTAD+Solutions', 'YeuLam', 'Audasy', 'Berhan+Apps', 'VNMSM-GROUP', 'PGA+Apps', 'Gorje+Apps', 'Wiltech', 'dev.audicts', 'FELIPE+CHAVARRO+POLANIA+INC', 'charLog+Games', 'Best+Caption', '4India', 'Fredrik+Markstr%C3%B6m', 'Free+Audiobook+%26+Ebook', 'Elitech+Systems+Pvt+Ltd', 'AppLab01', 'Rising+Entrepreneurs', 'Developing+Perspective,+LLC', 'Cezar+books', 'JOHN+SMITH', 'Apps+Studio+Inc.', 'archiG%C3%A9nie+Fran%C3%A7ais', 'fab*23', 'IronServices.com', 'Kobo+Books', 'acme-android.com', 'Hanzy', 'Jaroslav', 'Marathi+Techworld', 'Onnuva+Inc.', 'Meditate,+Sleep,+Calm;+Inc', 'ADS+SOFT', 'tricksgum', 'TAH+apps']
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

        
