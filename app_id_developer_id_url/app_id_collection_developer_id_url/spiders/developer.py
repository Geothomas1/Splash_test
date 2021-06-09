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
        tag=['IGORLINSGAMES', 'Everyone+Learning+Apps', '172+Games', 'Dedalord', 'Cougario', 'Fullstack', 'Turbo+Chilli', 'Majaka+Corporation', 'Fine+Glass+Digital', 'NymeriaGames', 'baklabs', 'inPocket+Games', 'Chop+Games', 'Ski+Tracker', 'WOC', 'Four+Pixels+Games', 'Evil++Indie++Games', 'Action+Portal,+LLC', 'DZMITRY', 'PeekJoy+Interactive', 'Alexander+Kowalczyk', 'RINGGAME', 'RSI+Radiotelevisione+Svizzera', 'yuni_game', 'Hi-Sum+Games', 'Pak+Appz', 'FIE', 'Nitro+Kings', 'Centre+Fun+Games', 'Kuku', 'Smartmove', 'Maker+Labs+Inc', 'Mystic+Media', 'Games+Bracket', 'Oreo+Studio+-+Best+Shooting+Games+For+Free', 'Primea+Systems+Oy', 'Sportsencyclo', 'Free+War+Games', 'TapSwift', 'Wacky+Studios+-Parking,+Racing+%26+Talking+3D+Games', 'Extreme+Game+Tap', 'let%27s+play', 'N-Dream', 'Fun+Hive+Studios', 'SoftSquare+InfoSoft', 'Girl+Games!', 'Gigago', 'Fun+Bytes+Studio', 'glulen+games', 'Game+Booster+Studio', 'Eriksen+Software', 'StrategyGame', 'Lance+Craner', 'Michel+Guenin', 'DK+Simulations', 'HexWar+Games+Ltd', 'KIXEYE', 'Travian+Games+GmbH', 'CMON', 'Arieshgs', 'AndroidWargames.com', 'WISJOY+ENTERTAINMENT+HK', 'Jon+Taylor', 'LuGus+Studios', 'OasisGames', 'Burning+Sand+Studio', 'boudour', 'Felix+Ungman', 'Lars+Klevan', 'Gamesvision', 'World+War+Game', 'appdev', 'Fastone+Games+HK', 'Fun+Games+For+Free', 'PINUPGAMES', 'Gagale+Games', 'JiroLabs', 'spiritapps', 'Berdnyk+Games', 'Joy+Crit', 'Nicu+Pavel', 'PANGU+GAME+GLOBAL+LIMITED', 'star+wings', 'Nauw+Studio', 'Camel+Games+Limited', 'PopReach+Incorporated', 'Special+Gamez', 'Machine+Zone,+Inc.', 'Evgenii+Bryl%27', 'tap4fun', 'Funny+Tap+Studio', 'Free+Games+Hub', 'simiyaworld', 'JoinForce+Tech', 'SunShine+Free+Games+Studio', 'Wargaming+Global+IT', 'John+Tiller+Software', 'Sengin+Technologies,+Inc.', 'War+and+Strategy+games', 'Oliver+Hummel', 'Ball+Game+team', 'naiadgames', 'Dev.Assembly', 'Cool+Gray', 'Chyo+Tech+Network+Ltd.', 'Educ+LECOMTE', 'Pilav+Prod%C3%BCksiyon', 'Sylvia', 'Gangster+Mafia+Games+Grand+Crime+City+Free+Action', 'Offline+Battleground+Games', 'Action+Hive', 'Flathead+Studios', 'The+Moj+Games', 'InnerLoop+Studios', 'Legion+Games', 'Artik+Games', 'Wesley+H.+Fung', 'ESPtech', 'FireBite+Games', '%D0%9D%D0%B0%D1%83%D0%BC%D0%BE%D0%B2+%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9', 'History+Games+by+Bernd+Noetscher', 'World+War+Strategy', 'Geel+Orion', 'DH+Games', 'Trenzy', 'MadDuck+Games', 'SW+by+Arieshgs', 'Vinci+Games', 'Rigbak', 'XavieraTech', 'ATM+Games', 'Stardust+Gaming+Studios', 'Spearhead:+Popular+Action+%26+Offline+Survival+Games', 'Agile+Games+Studio', 'KHAN+LI', 'Scandiacus+LLC', 'WillPlus', 'Moonlit+Works', 'Comfy+Company', 'Scarlet+String+Studios', 'Kinenjin', 'Visual+Novel+Developers', 'ninedux', 'Two+and+a+Half+Studios', 'Synthic', 'Graven+Visual+Novels', 'RedFoc', 'Five+Web+App', 'Visualnovels.nl', 'WCU+Create', 'LetiGame', 'ESC-APE+by+SEEC', 'KohiDev', 'Sugoi+Studio', 'Attic+Salt+Visual+Novel', '%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%A2%E3%83%BC%E3%83%84', 'Akeno+Monkey', 'Axelerum+S.L.', 'Zero+Zone+Mark', 'Sensuality+Games', 'Prandy+Game', 'Cherry+Kiss+Games', 'Megaloot', 'Beemoov+Games', 'Kyuppin', 'Soviet+Games', 'SilverTabbyCat+-+Visual+Novel+Games', 'Modern+Visual+Arts+Laboratory', 'Crystal+Game+Works', 'Nochi+Studios', 'Salangan_games', 'Handoko+/+iihigate', '%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BEMAGES.', '%E8%B5%A4%E7%87%AD%E9%81%8A%E6%88%B2', 'Tortuga+Ltd', 'LAYER+Tech', 'birdbread.', 'Cheritz+Co.,+Ltd', '%E6%B7%B1%E5%9C%B3%E5%85%AB%E7%8F%AD%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8', 'DMM.com', 'Ciberman', 'Lemon+Curd+Games', 'Nativi+Digitali+Edizioni', 'Gleb+Kovalev', 'Achromia+Games', 'Mushi', 'Stringent+Tech', 'Fantashminapps', 'Sky+Sabotenn', 'YoYoYoMi', 'Institut+Informatika+Indonesia+%28IKADO%29+Surabaya', 'Feature+Games', 'J-Novel+Club', 'Cyanmob', 'Top+Hat+Studios,+Inc.', 'FirtsTime', '%E8%90%8C%E3%81%88APP', 'Alex+Cerge', 'Alexandrite%27s+Lab', 'CatCap+Studio', 'Chaos+Cute+Soft', '751Games+Co.,+Ltd.', 'novel.tl', 'CINAMON+GAMES', 'Odencat', 'Viatcheslav+Ehrmann', 'IDHAS+Studios/Ithaqua+Labs', 'Ayush+Raj', 'YOUGO.GAMES', 'HUNEX+CO.,LTD.', 'Anpin', 'EbonSoft', 'AXgamesoft', 'Dualcarbon', 'Games2win.com', 'BigBeep', 'Better+Games+Studio+Pty+Ltd', 'Ruslan+Chetverikov+-+Driving+%26+Police+Games', 'Offroad+Games+2020', 'Falcon+Gamerz', 'Words+Mobile', 'MN+Prototype', 'TW+Games+Studios', 'Reaction+Game+Studio', 'Spark+Game+Studios', 'Oppana+Games', 'BoneCracker+Games', 'Gaming+League', 'Gaming+Stars+Inc', 'Billion+Gaming+Studio', 'Keybet+Studios', 'IDBS+International', 'Dynamic+Games+Ltda', 'Racing+Games+Android+-+Appsoleut+Games', 'OB+Games', 'Gamers+Tribe', 'Mobimi+Games', 'Sky+Unlimited', 'Vine+Gamers+Inc.', 'Bar%C4%B1%C5%9F+Kaplan', 'Mega+Creation', 'Gamotronix', 'IND+SOFTWAFE', 'SM+Games+%26+Apps', 'Nexon+Studio']
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

        
