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
        tag=['GameChanger+Media', 'Olivier+Roger', 'LockDev', 'Free+Sport+Apps', 'Shaggy+Games', 'HD+Droid+Wallpapers', 'Hayava,+Inc', 'korokoro', 'Advance+Software', 'publicvoid', 'CalculatorsApps', 'SAJID+QAYYUM', 'MTV+studio', 'Sleeping+Rabbit+Studio', 'rezadev', 'Braven.net', 'TnTGameWorks', 'JackFoolery', 'New+Casual+Games', 'TeamFans', 'dIPM', 'Deftouch+Interactive+Art', 'minsunsoft', 'sportingapps', 'BetPalz+Corp', 'RusMakMon', 'Mahesh+Prajapati', 'Silver-Games', 'Computational+Imaging', 'Ryan+Blume', 'Brazius+Productions', 'Owwen', 'furuApplications', 'Hi-Five+Gaming+Studio', 'SpeedyMarks', 'GNTechnolab', 'Honeycommb', 'WestRiver', 'Modux+Apps', 'Umpires+Media', 'xamrine+studio', 'Dirty+Luck+Games', 'Real+TV+Remote', 'SKYAPPS', 'JingleTek+Co.,+Ltd.', 'Kari%27s+Studios', '%E3%82%A8%E3%82%A4%E3%82%A8%E3%83%8C%E3%82%BD%E3%83%95%E3%83%88%E6%B0%B8%E7%94%B0%E6%B0%8F%28ANSoft%29', 'Apollo+Journey', 'Tio+Atum', 'In+Sequence+Software', 'The+IT+Pioneer', 'Baseball+Australia', 'Back+To+Baseball,+LLC', 'Valcom+IT+Services', 'Jared+Parker', 'Fanalyze', 'Volt+Games', 'Dream+world', 'Digital+Game+Studio', '1UP+Match+3+Games', 'Nikita+Dang', 'Casual+Games+For+Fun', 'Quiauto.', 'Your+VR+Experience', 'DVS+Baseball', 'Goofster+Games', 'PLAYTOUCH', 'qnguyen', 'VR-tainment', 'Cleveni+Inc.', 'pqjs237', 'Rianon+s.r.o.', 'GFuentesDev', 'AppLock@DoMobile', 'Studio+H2O', 'Wallpaperjoko99', 'ahmed+alrifay', 'Jan+Soukup', 'koji%28%E6%A0%84%E5%86%A0%E3%81%AB%E3%82%83%E3%81%84%E3%82%93%E3%81%AE%E4%BA%BA%29', 'Robert+Hellestrae', 'Tyler+Fossett+Independent+Video+Game+Developer', 'JavaBS', 'Carolina+Wolf+Software', 'nevishs', 'Ateia+lafi', 'Luxury+Personalization+Designs', 'Kids+Games+Factory', 'ZXing+Team', 'QR+Simple', 'QR+Scanner+%26+QR+Code+Generator+%26+Radio+%26+Notes', 'marks+duan', 'Altrigit+S.L', 'Cognex+Corporation', 'TeaCapps', 'TrustedApp', 'Infinity+App', 'Geeks.Lab.2015', 'InShot+Inc.', 'Apps+Wing', 'MartinsV.dev', 'Scandit+Inc.', 'Simple+Design+Ltd.', 'Mobile_V9', 'AndroidRock', 'Patel+Om+Developers', 'Apps360+Team', 'Cambridge+App+Lab', 'UpTree+Developer', 'Hi-Shot+Inc', 'Aeiou', 'Ez+Team+Barcode+%26+QR+code+Scanner', 'Generic+Co', 'Barcode+Reader', 'Dream+Edge+Technologies', 'Entertaining+Logix+Apps', 'GentleMan+Dev+Studio', 'Barcode+Scanner', 'EZ+to+Use', 'Reader+and+Scanner', 'Sunny+cc+inc', 'Bun+Scan', 'Social+Media+Apps+Studio', 'Tobias+Reinhardt', 'velsof', 'Easy+To+Use+%28OnMobi%29', 'Skycore,+LLC', 'SRK+Games', 'fttx', 'Duy+Pham+%28MMLab%29', 'CUROSOFT', 'Leap+Fitness+Group', 'XConnected+Apps', 'Dors+Studio', 'DeepThought+Industries', 'Mobile_V5', 'AapniApps', 'BertinCode', 'Peter+Bikshanov', 'MeiHillMan', 'Scanbuy,+Inc', 'REPS', 'Simon+Boylen', 'Sean+Owen+%28of+ZXing+Team%29', 'Felix+Huneburg', 'reallyouttaworld', 'KP+Devs', 'Apps+Brain', 'DNB.apps13', 'Marcos+Redondo', 'NoWi+Apps', 'Rajshah5599', 'maheiapp', 'Phaneronsoft', 'dimai', 'Innovative+beat', '7th+Generation', 'Shine+Apps+Solution', 'SukronMoh', 'Status+Saver+apps', 'Royal+Fitness+Apps', 'Short+Video+Status+n+Slideshow+Maker+Appsolution', 'Tiffany+Apps', 'Barcode+Lookup', 'TOH+Talent+Team', 'EasyAppDevTeam', 'CodeCoy+Apps', 'Donut+Pond', 'KW+2019', 'QR+Scanner+%26+Barcode+Reader', 'Scan+Mobile', 'Kkrinsi+Apps', 'Fr+developers', 'Scan+PRO', 'pickwick+santa', 'QR+Code+Scanner+%26+Languages+Translator+Developer', '1+Bit', 'Simple+Echo+Limited', 'Evaevacorp', 'TWMobile', 'TPCreative', '5+Star+Apps+World', 'Macland+Group', 'Price+Checker+Laser+Pro', 'AppsTechZones', 'Smart+Scanner', 'ToprShop.LTD', 'Next+Generation+Apps+Developers', 'AVIRISE', 'Application4u', 'Olyfox+Webbrowser+Inc.', 'G.00b', 'MaryErre', 'KTW+Apps', 'appspro26', 'SR+system', 'QR+Scanner+Team', 'Sumy+Applications', 'Cyrax+Global+Apps', 'Codesoft+Developer', 'NextAPP', 'Free+Apps+%26+Tools+Studio', '4+Tech+Solutions', 'MobMatrix+Apps', 'The+Fastest+QR+Code+Scanner', 'Jad+Afif', 'Accusoft+Corp', 'QR+Code', 'App+Only', 'Blue+Mobile+Inc.', 'MobilMinds+Studios', 'Big+Ocean+Studio', 'MobilePowerTool+Inc', 'Android+Does+Team', 'WHATS+WEB', 'Nikola+Antonov', 'Dmytro+Korobko', 'Longint', 'Mobile+Apps+Dunia', 'Robince+Studio', 'ali+LIM', 'malam', 'Lineris+LLC', 'All+Mobile+Languages+Translators+Free+Apps', 'Flow+Apps+Tech', 'ITech+Inc', 'Red+Reader', 'Dronax+Studio+Inc.', 'EXA+Tools', 'barcode+scanner+qr+code+reader+qr+scanner+%26+reader', 'lilule', 'Incognisys+Solutions', 'Flamingo+Mobi', 'MiniTools', 'App+Studio+Lab', 'Dual+Design+Studio', 'TKR+mobi', 'Logic+Utility+%26+Tools+App', 'S.K+DEVLOPERS', 'Netpeak+Mobile', 'Qr+Code+Scanner+and+Qr+Generator+Company', 'hauyu', 'bestdeveloperteam', 'AndroDeveloper+Inc.', 'EasyTechMobile', 'Alpa+Bhanushali', 'glory+app+studio', 'User+Guider', 'Softo+Logicx+Solutions', 'NetQ+Technologies', 'Guitar+Tabs+X', 'PixoVIN', 'SamiDroid', 'YovoGames', 'Beansprites+LLC', 'kukipukie', 'bmapps', 'Crazyplex+LLC', 'Happy+Apps+Media', 'Breet.Jia', 'Fabulous+Fun', 'Taprix', 'Minors+Games+Studio', 'HAPPY+TAPPY+STUDIO', 'GameiFun+-+Educational+games', 'bweb+media', 'Girls+Games+Studios', 'Coco+Play+By+TabTale', 'Indian+Pregnancy+Parenting+tips,+Baby+products+app', 'kids+GamesOn', 'PRT+Game+Studio', 'gkgame', '999%2B+Games', 'GameiMake', 'Girl+Games+Academy', 'Chic+World', 'Mobi+Fun+games', 'Tap+Happy', 'Shivank+Patel', 'Ginchu+Games', 'ShishuPoshan', 'Versita+Ptyltd', 'Level+Zone+Games', 'Vigorous+Glory', 'Pi+Games+Studio', 'ALAA+Apps', 'BIMOGAMES', 'Family+Games+-+Free', 'Girls+Fashion+Entertainment', 'chiecgiaythan', 'NutGenix+Games', 'Baby+Care+Games', 'DevGameApp', 'Baby+Care+Stores', 'uGoGo+Entertainment', 'Fun+Galaxy+Media', 'IAP+Games', 'Procter+%26+Gamble+Productions', 'Cute+Girls+App+Studio', 'FirstCry.com', 'Parentune+-+Parenting,+Child+care+Growth+Tracker', 'Tec+Games', 'risekg', 'TinyBit', 'Level+Zone+Apps', 'Cliq+Education+App', 'Babygogo', 'Baby+Hub', 'Kids+Fun+Land']
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

        
