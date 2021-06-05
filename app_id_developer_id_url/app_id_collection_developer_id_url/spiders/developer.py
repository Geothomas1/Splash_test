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
        tag=['MTS+Free+Games', 'Marco+Palaferri', 'Archant+Community+Media', 'Halfzone+Games', 'SUERA+LLC', 'ostrich+games+studio', 'Kaoslp+Jaiso', 'Tahoe+Regional+Planning+Agency', 'Deckee', 'Sentinel+Marine+solutions', 'Candela+Creative+Group', 'Your+Boating+Buddy', 'Axondev+Games', 'Electric+Pocket', 'NV+CHARTS', 'RTS+AppDevelopment', '2nd+Phone+Number+%26+Free+VPN+Ltd', 'FLYTOMAP+INC', 'JustLiquidity', 'ImOK', 'America%27s+Boating+Channel', 'Boating', 'Jimbl', 'Beekeeper+Group', 'Social+Knowledge,+LLC', 'Zinio+Pro', 'Imagine+Marketing+pvt+ltd', 'Flat+World+Communication+LLC', 'Seapilot', 'Southern+Boating+%26+Yachting,+Inc.', 'savvy+navvy', 'Myriel+Aviation', 'Gamelounge', 'Marine+tracker+studio', 'FredB', 'PinPrick+Gamers', 'magMaker+Editions+LLC', 'sfinx-it+GmbH', 'Action+Sports+Team', 'Kaushik+Dutta', 'Windyty+SE', 'United+Racing+and+Simulation+Games', 'Digibusiness+srl', 'Greg+Albritton', 'River+Map', 'PierShare,+LLC', 'Rulex', 'w%2Bh+GmbH', 'MapsApps', 'Dream+Yacht', 'Hans+Joachim+Herbertz', 'Tek+Wizards+Designs', 'Extreme+Games+Production', 'myharbors,+LLC', 'Biggerworks', 'Zoy+Studios', 'Stag+Gamers', 'Happy+Bytes+LLC', 'Hideaway+Boating+Ventures,+LLC', 'Modeling+Labs+Experiments+Studio', 'Gig+Big+Games', 'B.+Stickler', 'Kubitz+Inc.', 'iMobile+Solutions,+Inc.', 'Onedaygame24', 'Martin+Koubek', 'IngSM', 'Chesapeake+Bay+Magazine', 'Train+And+Car+Games', 'MarfaGames', 'FunSun', 'Kriworld+Itech+Private+LTD.', 'SeawellSoft', 'Ronald+Koenig', 'A.+Fischer', 'Frenzy+Games+Studio', 'Westapps', 'Bagani-Studio', 'Stallion+Games', 'WS+net', 'Doral+Av', 'wellenvogel', 'AfterGames+365', 'Tommy%27s+Lock+%26+Alarms', 'Fun+Blocky+Games', 'MAPITECH+LTD', 'Virtual+-+Apps+%26+Games', 'MT+Free+Games', 'Phil+Burgess', '%5Bmarina%7Cmap%5D', 'Cover+Shoot+Studio', 'Escape+Simulation+Games', 'Navionics+compatible', 'Games+Link+Studio', 'SM+Gaming+Academy', 'Whooosh+Games', 'RajaTech', 'SB+Gallery+Studio', 'SNOW,+Inc.', 'SweetShanghai%E7%BE%8E%E5%A5%B3', 'recode', 'Appwallet+Technologies', 'DB+Video+Zone', 'Yu+Apps', 'Photo+Editors+%26+Games', 'Brain+Vault', 'KX+Camera+Team', 'Ogden+Camera+Studio', 'Desire+Apps+Studio', 'XT+Apps', 'Fast+Video+Downloader+n+Photo+Video+Slideshow', 'GameSticky', 'BigBigApp', 'Phdpan', 'Perfect365,+Inc.', 'PhotoArt+Inc.', 'RatiBeauty.com', 'TudaSoft', 'GameCrush', 'Coocent', 'Outdoing+Apps', 'iJoysoft', 'Burbuja+Games', 'SUGAR+Cosmetics', 'Photo+Videos+Editor+Apps', 'Beauty+Face+Makeup', 'Pixel+Force+Pvt+Ltd', 'cRealSolutions', 'Lyrebird+Studios', 'barsa', 'sync+infotech', 'YubituSoft', 'Perfect+Studio+Labs', 'Pixels+Dev+Studio', 'Beauty+Makeup+Saloon+Inc.', 'Magical.ly+-+lyrical+video', 'LMAppsTech', 'Blush+Beauty', 'Analog+Film+%26+Palette+Filter', 'Remove+Dragon+Apps', 'Black+Infotech', 'Galaxy+Launcher', 'FunKidStudio', 'MGS+Games+Studios', 'AppLogic+Solutions', 'Make-up+Masters', 'Hamsoft', 'Beauty+Camera+Studio', 'Selfie+Pink+Group', 'Power+Video', 'Kiwi+Go', 'Foxy+:+Beauty+%26+Grooming+shopping', 'Antonia+Solution+Pvt.+Ltd', 'lemonbab', 'Makeup+%26+Project+Pan', 'AndroAppDevelopers', 'Purplle.com', 'Nail+Art+%26+Photo+Lab+%26Game+Studio', 'Super+Diva', 'Pacemaker', 'CFIDEAS+TEHC+LLC', 'AlphApps', 'PSTIME', 'House+Of+Beauty', 'MyGlamm', 'Ganesh+Baraiya', 'Adeline%E2%80%99s+World', 'Amino+Apps', 'Ila+Gautam', 'BK+Global', 'AMA+Apps+Inc.', 'INCI+Beauty', 'Photo+And+Video+Villa', 'bofca.inc', 'Beauty+Apps+Studio', 'AppDreams+photo+lab+editor+%26+frames+video+maker', 'Opeslink', 'PIE+Co.,Ltd.', 'ENDLEZ+APPS', 'SR+Infotech', 'musicoccean', 'KV+Fun+Games', 'Blauer+Stein', 'DSmart212', 'Photo+Frame+Edit', 'RS+App+Group', 'game+fun20', 'Elixir+Editors', 'DroidApp+Ventures', 'S%26V+Infosoft', 'Editorchoice', 'New+apps+zone', 'beautyqueen', 'Sanjit+Kumar+Singh', 'Only+Mobile+App', 'Iyrus+Inc', 'Pasha,s+App', 'HalfDevices', 'Building+Maintenance+Management', 'Phila+AppStore', 'Midelo+apps+studio', 'Kadam+Apps+Studio+2019', 'Noxa+Apps+Inc', 'forzens+infotech', 'Oshihar+Apps', 'Unysyegor', 'Tri+Core', 'MINIMAL.HUB', 'LKBL', 'eewee+production,+Inc.', 'Suhi+Apps', 'Tool+LLC', 'RRStudio', 'Nookiewow', 'Photo+Editor+%26+Collage+Maker', 'DK+Technologies', 'MusicPic+Art', 'Goshiapps', 'Dreams+Room', 'AI+Helps', 'Best+Pearl+Studio', 'Dream+App+Store', 'MINT+LLC', 'GelGo', 'Tukunu+Apps+Developer', 'Video+Maker+%26+Photo+Editor+Apps', 'Mitpi+Image+Editor,+Games+Studio', 'Beauty+Art+Inc.', 'Photo+Video+Zone+App', 'Italic+Games', 'ForestKing+Studio', 'LIGENSOFT', 'Car+Real+Racing+Studio', 'Ace+Project+Inc.', 'MLB+Advanced+Media,+L.P.', 'Baseball+24', 'Five+Aces+Publishing+Ltd.', 'VOODOO', 'CBS+Interactive,+Inc.', 'Football+WorldCup+2018', 'infinitypocket', 'Augmented+Reality+Games', 'TeamMEW', 'AppOn+Fungames', 'Game+Sniper', 'Hrvatin', 'OGames+Studio', 'Puzzle+Cats', 'Durianese+Game', 'Design+Depot', 'Air2000', 'Brady+Software+LLC', 'techno+shot', 'CussDev+Inc.', 'AbuShobakApps', 'FantasyPros', 'Make+It+So+Studios', 'Anhui+Huami+Information+Technology+Co.,Ltd.', 'MLB-NADIKA.LTD-Play+Game', 'Tontorina+mobile', 'Sport+BASIQs+LLC', 'msall', 'Knowledge+Spot', 'United+States+Baseball+Federation', 'Elite+Sports+Training', 'RotoBaller', 'Cimba+Solutions,+LLC', 'Baseball+Rules+in+Black+and+White,+LLC', 'Thinking+Baseball', 'Jaeyoung+Chu', 'EE+SYNC+Games+Studio+I.n.c', 'Best+Free+Application', 'VR+Entertainment+Ltd', 'iScore+Sports,+Inc.', 'Zappitize+LLC', 'St.+Louis+Post-Dispatch', 'Scoutee+Ltd', 'KHK+Soft.', 'Archie+McQuaid', 'BlueFrame+Technology', 'Postage+Saver+Software', 'gregstoll', 'Digital+Oppression', 'LTL+Games', 'Zhafira+Humaira','Fe_Andro_Yuya', 'Blabs+Ventures', 'Softwood+Apps', 'Ra+Wallpaper', 'Bekenyem', 'Telen', 'deploe', 'Baseball+America', 'Appness,+LLC']
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

        
