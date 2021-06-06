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
        tag=['Lassoo', 'Kate+Simmons', 'Enterprise+Leaders+Worldwide', 'Stirling+Corp', 'Enima', 'CD8x', 'Ap+Developer', 'ShunBoi', 'brkbjk', 'Disco+Bandit', 'Developer+Downy', 'vouge+devcelopers', 'chonbaihat', 'Dmitriy.Ponomarenko', 'Dairy+App+%26+Notes+%26+Audio+Editor+%26+Voice+Recorder', 'SmartMob', 'Dje073', 'Dolby+Laboratories+Inc.', 'j+labs', 'Alpha.20', 'Dema121', 'AC+SmartStudio', 'Appntox', 'Newkline+Co.,+Ltd.', 'Audiophile', 'Raytechnoto', 'C+Mobile', 'coolncoolapps', 'Triveous+Technologies+Private+Limited', 'Beunity+Development', 'lovekara', 'Sachin+Gorade', 'AppixiStudio', 'Waqar+Shakeel', 'Speech+Processing+Solutions+GmbH', 'iApp+Inc.', 'Gritstone+Studios+Ltd.', 'GK+Technologies', 'VAPP+SOSO', 'Appliqato', 'ELG+APP', 'Softlookup.com', 'Calendar+Date', 'Audio+Visual+Media+Apps', 'agent-hp', 'pamsys', 'eXtream+Software+Development', 'Tools+Dev', 'Vault+Micro,+Inc.', 'IT+Adapter+Corp.+Inc.', 'WIREHALL', 'Bikram+Pandit', 'Grows', 'R/W+Softwares', '0alex', 'Recorder+%26+Music+%28recorder,+weather,+forecast%29', 'Shubham+Mourya', 'Wachi.Apps', 'Innody,+co.', 'Rev.com,+Inc', 'Otter.ai', 'AppzCloud+Technologies', 'Productivity+Inc.', 'Ayago+Dev', 'shinshow', 'Tasty+Blueberry+PI', 'Ronil+Shah', 'Bhrigu+Apps', 'Super+Voice+App', 'Mega+Sticker+Maker', 'Mobi+Softech', 'CamTechBy', 'Video+%26+Photo+Gallery', 'Elgamal', 'Searing+Media+Inc.', 'CV+Infotech+Apps', 'Secure+Private+Browser+Productivity+Apps', 'Canomapp', 'HubPro', 'EHT+ECO', 'Andi+Unpam', 'Soon+Kyung', 'Markus+Dr%C3%B6sser', 'ideaxa', 'Cogi+%E2%80%93+Note+Taking,+Call+Recorder,+Transcription', 'Tarnica+Developers', 'Notes+App', 'SN+Tech+-+Mix+Player+%26+Editors', 'America+System', 'N-Droid+Development', 'Hash+Tag+Xtudio', 'CinixSoft', 'extra+soft+inc', 'Music+mp3', 'Audiosdroid+OU', 'Sociu', 'Technitab+Solutions', 'xursisoftware', 'John+Li', 'Rudy+Huang', 'Marble+Apps', 'Offline+Tools++%26+Art+Applications', 'Islam.ms', 'DeltaAppsStudio', 'MojoRocket+Studios+LLC', 'Appdhaba+Technologies', 'SmartSolutions~Tech', 'Blue+Wave', 'Recorder+Apps+%28music,+recorder,+weather%29', 'Irishin', 'Cooling+team', 'Home+of+free+tools', 'Carsten+Dr%C3%B6sser', 'PopularAppsHub', 'Catchy+Tools', 'S.M.+SHAHi', 'wapZan+inc.', 'soft+apps+center', 'CALLER.LIVE', 'Kristina+Skachkova', 'Octagon+Technologies', 'BejBej+Apps', 'SpyWire+Tech', 'gallery+ad+free', 'Dmks+Apps', 'Reactive+Source', 'krdstudio.g', 'Pasindu+Weerakoon', 'Gomaleta.co', 'VuviGame', 'ArtistSoft', 'KnotCode', 'Muditage', 'SoomSoft', 'Social+Play+Apps', 'MisiTeam', 'Adrosoft+Infotech', 'AutoStop', 'extraappdevelopers', 'shadrin.software', 'Kite+games', 'AmaroApps', 'The+Bright+Apps', 'Algorerabin', 'SolLabDev', 'katamapps', 'avinash_42', 'The+Mark+Rider', 'Spotify+Ltd.', 'Pampered+Bytes', 'nasolutions', 'Harshel+David', 'Kailash+Dabhi', 'Awesome+App+Developer', 'S.s', 'Charli', 'EasterEgg', 'MANOJ+G', 'DevCoder', 'Bro+code', 'Ask+Your+Android', 'Handroid', 'Muhammad+Sijjeel', 'AppX+Studio', 'Colorfit', 'Mahindra+Apps', 'Photos+Gallery+Studio', 'Bhima+Apps', 'Draw+apps+for+free', 'Image+Crop+n+Wallpaper+Changer', 'Logolab+-+Logo+Maker+%26+Graphic+Studio', 'Laura+P%C3%A1ez', 'Focus+apps', 'Creative+APPS', 'Luffabelle', 'Devkrushna+Infotech', 'Evening+East+Production', 'artsoftech', 'Raed+Mughaus', 'ArtIdeas.io', 'BestTokVideos', 'Jack+Soeharyo', 'NN+Centrex+Solutions', '4Axis+Technologies', 'KDMedia', 'A-one+Studio', 'AppTrends', 'Andro+Tools', 'FreeSharpApps', 'Samsung+R%26D+Institute+Bangladesh', 'Legion+of+Art', 'Marcel+For+Art', 'Trends+App', 'Name+Art', 'Marcin+Lewandowski', 'BSMJ+apps', 'ARPHN', 'devlord', 'DrawAPP', 'Canva', 'Piyush+Patel', 'Islamic+Lectures', 'Milan+Zarecky', 'godwit+studios', 'vegan+lifestyle', 'MK+Embroidery+Design', 'Insitu+Art+Room', 'Pavaha+Lab', 'Tanager+Apps', 'TapNation', 'Andromida+apps', 'anina', 'Little+App+Store', 'Apps+Specials', 'vertido.io', 'regitaapp', 'AppSelect.org', 'Creative+Apps+Factory', 'Cute+Wallpapers+Studio', 'Adobe+Inc', 'Peli+Ngacengan', 'Sitd212', 'Apps+You+Love']
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

        
