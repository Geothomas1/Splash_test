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
        tag=['%F0%9F%92%96%F0%9F%92%96%F0%9F%92%96%F0%9F%92%96%F0%9F%92%96Trinh+Hang', 'SermonAudio.com', 'AKApplications', 'Jack+Rehan', 'Victor+Axelsson', 'uniqueappsforyou', 'Storytel+Sweden+AB', 'GPS+Route+Tracking,Map+Navigation+%26+Street+View', 'Aviation+Theory+Centre', 'O5appStudio', 'KaruniaDev', 'Lion%27s+Den', '99+Dictionaries:+The+world+of+terms', 'BoiBazar.com+Ltd', 'FREEBOOKS+Editora', 'Mukesh+Kaushik', 'OverDrive,+Inc.', 'Grace+Ministries+and+Dusty+Sandals', 'BlackHole+Machine+Tech', 'Van+Solutions', 'Tamago+Labs', 'Gospel+Publications', 'Ellen+G.+White+Estate,+Inc.', 'Grace+Bible+Apps', 'And+Bible+Open+Source+Project', 'Dictionary.com,+LLC', 'Aimer+Media', 'Easyelife', 'G%C3%A9rald+Gounot', 'Luiz+Antonio+de+Andrade+Junior', 'Study+Bible', 'Faithlife', 'Vibrant+Solutions', 'Denys+Dolganenko', 'danik', 'Legendary+Quotes', 'Citationsy', 'Matej+Nos%C3%A1%C4%BE', 'Holy+BIBLE', 'Trellisys.net', 'UNSH', 'Jehovah%27s+Witnesses', 'Rstream+Labs', 'SUPERCOP', 'inoventory+world+apps', 'DAVID+RAUDALES+LLC', 'Alif+Innovative+Solution', 'Lastwoods+Technologies', 'TopTechBox', 'WCOI', 'CogniLore+Inc.', 'Laridian,+Inc.', 'granthalay.devs', 'LLC+Applications', 'Books+Mountain', 'Mjobs+Co', 'Mirt+apps', 'SR+ECOMMERCE+FACTORY+PRIVATE+LIMITED', 'Free+App+4+All', 'JG', 'MADE+EASY', 'Stud+Zone', 'Best+Dictionary+Apps', 'F.+Permadi', 'S.Chand', 'Exam360%E2%84%A2+%28INDIA%29', '%F0%9F%93%96+Your+Smart+Apps', 'The+BIBLE', 'eMedia+Services', 'Thakur+Publication', 'Charles+Elisha+Williams', 'IQRA+THE+TRUTH', 'Sunnsoft', 'Void+Goel', 'Digibook+Technologies+Developers', 'Navyug+Infosolutions', 'Doctor+Micro', 'Freeebooks+TARA', 'GJOneStudio+Language+Tutors', 'KingdomNomics,+Inc.', '%23DEVS', 'Aryaa+Infotech', 'audio+stories+books+and+songs', 'Bash+Overflow', 'Smart+Mob+Solution', 'Miraj+Patel', 'Sahajanand+Sanskar+Dham,+Fareni+%28+Swaminarayan+%29', 'Creative+Utility+Apps', 'My+Site+Creations', 'Spayee+:+Online+Course+Selling+Platform', 'JOSDEV', 'DITS+Pvt.+Ltd.', 'ARTE+TATTOO', 'Appstoreahm', 'Schoolshop.in', 'GK+App+Store', 'LitCharts+LLC', 'BookPool', 'Swamy+Publishers+%28P%29+Ltd', 'Words+Worth+ELT+Pvt.+Ltd.', 'Adolo', 'MHR-LAB', 'AlleyDog.com', 'ISC+Developer', 'American+Heart+Association,+Inc', 'Hafeez+Publishers+PVT+LTD', 'The+Young+Developers', 'MS+Development', 'superaplicacionex', 'George+Kennedy', 'Susthita+Softax+Solutions', 'Algento+Cloud+Computing+Limited', 'Navionics+Srl', 'Gps+Nautical+Charts', 'MarineTraffic', 'Tap+-+Free+Games', 'Navico+Norway+AS', 'Euminia+GMBH', 'W%C3%A4rtsil%C3%A4+Voyage+Limited', 'Dock+Here+LLC', 'andromede+oceanologie', 'theotherhat.biz', 'Sergey+Zarochentsev', 'Cribster', 'Kei_Nakazawa', 'APPCOM+CANADA', 'Borrow+A+Boat+Ltd', 'tinygarage', 'RCMSAR', 'Park+The+Boat,+Inc.', 'Nautics+Oy', 'Ayomi', 'Mobibress', 'Forsefield+Inc.', 'Nano+Code+Ltd.', 'Powered+by+IN4MA+Platform', 'IBT+Games', 'Garmin', 'Sports+Learning+Tips', 'Bonnier+Corp', 'Imperial+Arts+Pty+Ltd', 'Apps+Enterprises', 'SailTimer+Inc.', 'Boater.pro', 'Yachtino+GmbH', 'picture+polly', 'Dockwa', 'New+Logic+Technology', 'Nebo+Global', 'Aploft', 'CA+State+Parks+Division+of+Boating+%26+Waterways', 'BellApps', 'Vroom+-+Apps+%26+Games', 'AMFAPPS', 'V.Mark.', 'Push+Logic', 'Individual+Android+Developer', 'New+Game+Ventures', 'Bajake+Studios', 'Broken+Heart+Beat', 'Doodle+Mobile+Ltd.', 'nicktz', 'Gala+Games+Studio', 'Extreme+Simulator', 'Ticker92', 'Navigational+Algorithms']
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

        
