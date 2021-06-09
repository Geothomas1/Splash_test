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
        tag=[]
        for i in tag:
            url='https://play.google.com/store/apps/developer?id='+i
            yield SplashRequest(url, self.parse,  endpoint='execute', args={'lua_source': script, 'url': url})
        

    def parse(self, response):
        app_id_list=[]'Damoware', 'wz+game', 'Gamepool+Studio', 'Agents+of+Tech', 'Magic+Puzzle+Games', 'Gemego+Ltd', 'manbenapps', 'LazyDog+Game', 'Guid+Labs', 'ZenLife+Games', 'PUZZLE+WORD+GAMES', 'Game-Juice', 'Fugo+Games', 'GujaratiLexicon.com', 'Word+Game+Trivia', 'Fanatee,+Inc.', 'eXparity+Apps', 'Berni+Mobile', '404+-+dev+not+found', 'freelive+appstore', 'Jabir+Ali', 'Hoyt+Games', 'BINGGOU+Games', 'Wordfun+Games', 'Harmonic+Solutions', 'Magics+Game', 'Word+Search+crossword', 'fatphoenix', 'TAMob', 'Yogesh+Sonani', 'MJ+App', 'Ova+Soft', 'Spring+Wild+Studio', 'MrBrown', 'Android.Soft', 'Galsen+Studios', 'Bizzy+Bee+Games', 'Christian+Games', 'The+Angry+Kraken', 'touchfield', 'Nusantaras+Studio', 'Giantix+Studios', 'Free+Fire+Studio', 'Simple+Puzzle+games', 'Content+Arcade+Games', 'BkrApps', 'Famobi', 'KMLBUY', 'Think+Game', 'CodesWithChandan', 'FreeTime+Pass+Games', 'Orange+Void', 'Apps_Book', 'Word+Search+Puzzles', 'The+Bag+Of+Words+Games', 'jeremiah-dev', 'WPS+SOFTWARE+PTE.+LTD.', 'Word+Games+Dev', 'Cometdocs.com+Inc.', 'Estrong+Business+Office+.%E4%B8%8A%E6%B5%B7', 'TangramGames', 'Solo+Tech+Apps', 'Three+Card+Games', 'LegendOffice+MS+File+Store', 'Poder+Studio', 'hongthuanjsc', 'WordWeb+Software', 'Matholution', 'Puzzle+Word+Games', 'Ulilab', 'Office+Document+Reader', 'Worzzle+Games', 'FTKG', 'Aiyi+Mobi', 'Marul+Games', 'Smart+Puffin', 'LOTUM+GmbH', 'OneDocument+-+Office+Reader+%26+Edit', 'Word+Calm', 'APNAX+Games', 'IsCool+Entertainment', 'Weeny+Software', 'PDFConverter.com', 'Mobile+Apps+Smart+Ultility+Online', 'Document+Viewer+2021', 'GameLoX', 'Pic+Frame+Photo+Collage+Maker+%26+Picture+Editor', 'Advance+Clock', 'OffiDocs+Mobile+Apps', 'GNL+Rn', 'Emblic+Infosoft+%28OPC%29+Pvt.+Ltd.', 'Sentab', 'LazyMasters', 'Soft+Towel+Games', 'Puzzzle+Games+Free', 'Diao+Da+LLC', 'megasoft78', 'Transpondian+Studios', 'Mini+Joy+Official', 'Rolling+ABC', 'com2wordsgame', 'Word+Puzzle+Studio', 'Free+Block+Blast+Games', 'CanaryDroid', 'LeSon', 'Randierinc', 'BKSON', 'Myor', 'Oogway+Apps', 'Face+up', 'AFKSoft', 'All+Document+Reader+App', 'Vmobify', 'Block+Puzzle+Classic+Free', 'C+Whyte', 'Stylish+Photo+Apps', 'VOZGA', 'puzzle+game+for+free', 'Nazmain+Apps', 'Dream+Word+Games', 'SKB+Studio', 'Mount+Games', 'Utility+Apps+by+XSDev', 'Ahihi+Studio+GameVN', 'Skyhighapps1', 'Function+9+Apps', 'SmartApps38', 'PASofts+Inc', 'Viral+Studio', 'Codecell', 'Craig+Hart+%7C+Funqai+Ltd', 'Smart+Photo+Editor+2021', 'Lead24', 'AppDevlo', 'AppsManju', 'neefaism', 'BennyApp', 'Sai+Info', 'Socketwire', 'Owais+Meethani', 'hashim+Alizai', 'FAMOUS+ENT.', 'NajmCV', 'Mongelakir', 'Tangram3D', 'NAWIA+GAMES', 'Twintip+Games', 'ALPHA+SOFT', 'Sievlar', 'Session+Games', 'pixel+soft', 'freeemojikeyboard', 'PolarisRicco', 'Code+This+Lab+S.r.l.', 'Dana+APPS', 'IOC', 'Make-up+Inc', 'Prism+apps+and+Games', 'Chakor+Studios', 'UKi+Media+%26+Events', 'Dead+Drop+Games+Inc.', 'Prathed+Sangwongvanit', 'Polyester+Studio', 'KitApps,+Inc.', 'bergfex+GmbH', 'Ideenkreise', 'AT2+game+studio', 'Incredible+free+games', 'Racing+Shooting+Action+Free+Games', 'FunVR', 'Ikon+S.r.l.', 'Svey+Development', 'SayGames', 'GARY+JONAS+COMPUTING', 'Gamers+Joyland', 'Sleepy+Z+Studios', 'Torque+Gamers', 'Frenzy+Tech+Studio', 'fireslave', 'Laboratory+Apps+And+Games', 'Mountain+News+Corporation', 'HDHB', 'Featherweight', 'Integer+Best+Free+Games', 'Trillion+Games', 'Core+Coders+Ltd', 'MySwitzerland.com', 'SummitGames', '3D+Games+Here', 'Creeng', 'FIS+IT+Department', 'Sparrow+Publishing', 'DPIdev', 'Crown+Art+Studios', 'eriegel', 'Ice+Beauty', 'Beauty+Games', 'Free+Games+to+Play', 'Clanified', 'Mr.KIP', 'RightSpot+Ltd', '8-bit+Games+memories', 'Owgun+Entertainment'
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

        
