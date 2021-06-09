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
        tag=['Grand+Game+Studio', 'OUTFIT+TB', 'PlayNow+Media', 'Free+to+Play+Games', 'Champ+App', '2+Wheels+Studio', 'Blue+Fire+Gamers', 'Heulwen+Imelda', 'Simulators+Gear,+LLC', 'High+School+Game', 'Ellic+Sone', 'Dartfish+Ltd', 'Futuristic+Game+Studio', '5+Storms+Studio', 'Over+The+Top+Wrestling', 'Wrestling-Online', 'Fighting+World', 'Last+Round', 'Mobitech+Games', 'Migane', 'World+Wrestling+Network', 'Zeer+Apps', 'Legion+Apps+Studio', 'SoftHealth', 'Sifo-Dyas', 'Interlock+Pty+Ltd', 'Lont+Action+Games+Inc', 'TheParodyNetwork', 'Anthem+Sports+%26+Entertainment+Inc.', 'Flip+Flop', 'news4ufree', 'Ayd%C4%B1n+Developer+Game+Studio', 'Iconic+Mobile+Games', 'Mexmy+Designs', 'Ricetime', 'AyaR+Dreams', 'Highspots+Wrestling+Network', 'Nit%27X++Games', 'honeythemes', 'WWE,+Inc.', '%E6%96%B0%E6%97%A5%E6%9C%AC%E3%83%97%E3%83%AD%E3%83%AC%E3%82%B9%E3%83%AA%E3%83%B3%E3%82%B0%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE', 'All+Elite+Wrestling,+LLC', 'Phillip+Daniels', 'Acquaintance+Apps', 'Playme+Games+Studio', 'RHM+Interactive+O%C3%9C', 'Sublime+3D+Game+Studio', 'Tap+By+Tap,+LLC', 'Sinclair+Digital+Interactive+Solutions', 'Wrestle+Square', 'Soft+games', 'CoolFreeApps', 'GBL+Studio', 'MS+Software+Incorporates', 'Insane+Championship+Wrestling+LTD', 'SenseAppsPile', 'HexaBit+Games', 'IKOZ+LTD', 'Axel+LEFEVRE', 'Gruffazilla', 'Busy+Gamers+LLP', 'Games+Park:+Action+and+Racing+Games', 'Oh+Helper', 'MarketJS', 'Kushti+Ke+Deewane', 'Enclave_Field', 'PULLOVER', 'Irsa+Studio', 'Major+League+Wrestling', 'Free+Fun+Games+Zone', 'Appsolute+LLC', 'i3oomz', 'CM3+Solutions', 'VENTURE', 'Pivotshare,+Inc.', 'FWZ+Games', 'Sport+Free+Game+Online', 'Black+Cell+Studio', 'Eagle+Studio+007', 'Appstoogood', 'FW+AppStudio', 'Free+sports+games', 'Creative+Ventures+Inc.', 'Dinhkasey', 'Game+Finale', 'WWF+Old+School', 'Zooroo', 'Game+Zone+Studio', 'Any+Can+Be', 'EpicApp7', 'Mayhem+Studio', 'Ask+Sports', 'Rocking+Chair+Labs', 'bradd', 'Ample+Games', 'GamesDot+Studios', 'Thake+Halina', 'Playvalve', 'Mini+Joy+HK+Limited', 'Blackout+Lab', 'Teewee+Games', 'Brainit+Games', 'Wordloco', 'Melimots', 'WORD+GAMES+LLC', 'Top+Rated+Word+Games', 'Long+Time+No+See+Game+Studio', 'Word+Search+Puzzle+Games', 'TerranDroid', 'Magic+Word+Games', 'Words+and+Maps', 'Uysal+Mehmet', 'PuzzleWorks', 'Varasol+Technologies+Private+Limited', 'AAlearning', 'Moca', 'Razzle+Puzzles', 'Fantasy+Word+Games', 'WePlay+Word+Games', 'Word+Connect+Games', 'Dawid+Wnukowski', 'EveryDay-Apps', 'Connect+Word+Games', 'MS-Games', 'Vigilante+Games,+LLC', 'Aleksey+Taranov', 'Bubble+Shooter+-+Bubble+Pop', 'Love+Puzzles+Studio', 'Robus+free+and+fun+games', 'Innovation+Puzzle+Games', 'DGameZone', 'Cool+Word+Puzzle+Games', 'Justinas+Mek%C5%A1%C4%97nas', 'DotFinger+Games', 'SevenLynx', 'Easy+Game+-+Brain+Test', 'RBGA+Canvas', 'Silver+Moon+Apps', 'HappyDream', 'bindas', 'NEW+BABY+FUN+GAMES']
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

        
