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
        tag=['Black+Pyramid+3D+Games+Studio', 'Hello+World+Inc.', 'Gaming+Genesis', 'Haxinator', 'VVGames', 'Universal+Arts', 'Millennium+Star', '55+Best+Games', 'Fazbro', 'GlobalAppStudioss', 'Collider+Game+Studio', 'Pulsar+GameSoft', 'Pulsar+Gamesoft', 'Redstone+Creatives', 'Offroad+Games+Inc', 'ESproject', 'DEHA', 'GameFirst+Mobile', 'Riinventas', 'The+Giant+Games+Studio', 'smSoft', 'Phosphenes+Games', 'InfinityPlus.op', 'RunRush+Race+Studio', 'Yes+Games+Studio', 'Simulator+Soft.+Inc', 'HariHara+Games+Studio', 'FUN+GAMES+FREE', 'mx+games', 'Top+Simulations+Studio', 'Marvel+Labs', 'Blue+Sky+Games+Studio', 'Mahadev+info', 'HMgamestudio', 'NativeGaming', 'Krazy+Studio+07', 'Games+Pack', 'Simulation+Freak', 'Game+Fun+Inc', 'IHTIAR', 'HSZ+Games', 'PlaypoolMobile', 'Netropat+Game', 'Mini+Build', 'ayabakan', 'nrlt+studio', 'Ceo+World+App', 'Tribal+Games+Studio', 'PabloGame', 'The100Games', 'EUPHMED+INC.', 'Shake+Simulator+Games', 'Gameboost+Studio+Inc.', 'Game+Nest+Studios', 'Hyper+Tech+Apps', 'Mud+Runner', 'gamesoultech', 'Just+Funy+Games', 'J-force+tech.+Inc', 'SCAPPSC', 'Free+Games+2018', 'Blasters+Cosplay+Gamer', 'Logic+Rack', 'Dotline+Production', 'Games+Rumble+3D', 'Baiza+Game+Studio', 'Submarine+Apps', 'Smart+Owl+Apps', 'Hope+Software+Services', 'Scimob', 'Sony+Pictures+Television', 'Mari+Apps', 'Poptacular', 'RD+Games+Inc', 'Trivial+%26+Quiz+-+DiabloApps', '4Enjoy+Casual', 'Trivia+Games+ApS', 'Head+Solutions+Group+%28US%29+Inc.', 'the+binary+family', 'Xinora+Technologies', '3K+Mobile', '8SEC+Games', 'Logos+Box', 'ARTADIAN+GAMING+LLP', 'TXT+Games,+LLC', 'TrivNow+LLC', 'Trivia+Box', 'Words+Logos+FreePuzzleGames', 'Quiz+%26+Trivia+Games+-+BrainApps', 'bubble+quiz+games', 'World+of+Quiz', 'Walkme+Mobile', 'Jeux+de+quiz', 'On+Point+Holdings+Pty+Ltd', 'Quiz+%26+Trivia+Games', 'Stefano+Solinas', 'Redwood+Pro+Media', 'ACA+Developers', 'Guess+It+Apps', 'Nicergame+Studio', 'CarbonCode+Solutions', 'SMILE+AND+LEARN+DIGITAL+CREATIONS', 'LB+ART+-+Music+Games+%26+Trivia+Games', 'Smart+Quiz+Apps', 'Everyday+Quiz+Master', 'Cadev+Games', 'DH3+Games', 'Gerwin+Software', 'Valery+Bodak', 'QuizMan', 'THX+Games+Zrt.', 'NEXON.', 'Techxstar', 'Logo+Games', 'Quiz+Corner', 'GameBase+Studios', 'General+Knowledge+Trivia+Quiz+Game', 'Moonlight+Gaming', 'Tymedia', 'Kingim+Studio', 'Cerebellium+Apps', 'Guessland+studio', 'Monkey+Taps', 'Corvus+Apps', 'Cool+Duck+Games', 'Goxal+Studios', 'Yso+Corp', 'Volley+Inc.', 'The+Universal+Gamers', 'Playdox+Games', 'Quokka+apps', 'Trivia+And+Quiz+-+Trivia+y+Adivina', 'TITANWARE+SL', 'CustomPlay+LLC', 'Random+Trivia+Generator', 'Smilie+Ideas', 'fighter388', 'agroundapps', '10Pixel3D', 'Quiz-Trivia+Apps', 'mChamp+Entertainment+Pvt.+Ltd', 'soufian+hachimi', 'Apero+Games', 'DodsonEng', 'ET+Game+Developers', '3dinteger', 'GemGames', 'Zhenya', 'Studio+134', 'Team+Hikers', 'Simulators+Live', 'PT+Game+Studio', 'Gaming+experts', 'sagaapps', 'Jeminie', 'iGames+Entertainment', 'Panda+Gamerz+Studios', 'Enjoy+Land+Games', 'Door+to+games', 'Mobi+Games', 'VR+FUSION', 'Game+Educators', 'iPlay+Studio', 'Knock+Knock+Studio', 'UDevLemon+Studio', 'GameRon', 'Unicorn+Games+Store', 'Elixir+New+Games+2021+3D', 'Topaz+Consult', 'Deutsche+Bahn', 'Takahiro+Ito', 'Mortal+Games', 'Fun+Games+for+All', 'Amazing+Super+Fun+Games', 'SB+2k+Apps', 'kinggames', 'Private+Kara+Studio', 'HAKOT', 'Zippy+Games', 'Free+Games+2020', 'Portal+Esports', 'Dream+APPs%EF%BC%88%E3%83%89%E3%83%AA%E3%83%BC%E3%83%A0%E3%82%A2%E3%83%97%E3%82%B9%EF%BC%89', 'Tap+Bike+Racing+Games', 'Pompano', 'Royal+King+Games', 'igames+apps', 'Roboticsapp', 'Pixells', 'OKORIE+PRIMUS', 'liudingjun', 'GiantClip+Games', 'wapp.cz', 'Sunshine+Games+3D', 'Speed+Rush+Studio', 'PlayPops', 'Train+Simulator+and+Driving+Games', 'Verx+Labs', 'igames+saga', 'Glad+Games', 'monois+Inc.', 'Hyperfame+Games+Studio', 'Ammli+Studio', 'Sebastian+Weidenbach', 'Red+Lite+Games', 'NEXA+GAME+STUDIO', 'Gameology', '3BeesStudio', 'PalmGames', 'Fun+Free+3d+Games', 'Best+Simulation+5mb+Games', 'SG+-+Mobile+Games', 'Drounken+Monkey+Games', 'X-Land', 'stereo7+games', 'Smartpix+Games', 'RAON+GAMES', 'Valsar', 'Babeltime+US', 'ArgonGames', 'NGMOB+GAME', 'Mugshot+Games+Pty+Ltd', 'ChimpWorks', 'PIXELCUBE+STUDIOS', 'Booblyc+TD', 'easygame7', 'TOO+DreamGate', 'ZonmidStudio', 'Lupis+Labs+Software', 'Element+Studios', 'Crazy+Panda+Limited', 'Skizze+Games', 'Bamgru', 'Enjoy+mobile+game+limited', '69+Studio', 'AMT+Games+Ltd.', 'Robin+Blood', 'GreySharkApps', 'Jewel+-+Lazy+Chick', 'TopGameCenter', 'Bear+Play', 'Black+Hammer', 'Mugshot+Games', 'Ishaq0000', 'magic+tower+defense+company', 'Mksys+Technologies', 'relicware', 'Dmitsoft', 'Tower+Defense', 'Twilight+Castle+Productions', 'GameMushrooM', 'Polat+Studio', 'Nils+Asejevs', 'Nice+Arts', 'MacPlayGame', 'HawkBro', 'Angry+Rock+Games', 'ACE+GAME+INTERNATIONAL+LIMITED', 'GSoftStudio', 'Ess+Games', 'mw-systems.com', 'Free+Games+for+Everyone', 'Glitter+Fun+Studio', 'LiftApp+LLC', 'Tiger+30+Studio', 'mogame', 'Lion+Cube+Studio', 'TechArts+Games', 'Board+Fun', 'RP+Apps+and+Games', 'Mint+Games', 'Upland', 'Yomob+Games', 'FlinkStudio', 'Mentha+Games', 'Hyperix+Studio', 'Futoo+Family+Casual+Games', 'Funmotion+Casual+Games+for+kids', 'JK+StudioGroup', 'Soul+App+Studio', 'Game+Empire+Studio', 'SUNSOFT']
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

        
