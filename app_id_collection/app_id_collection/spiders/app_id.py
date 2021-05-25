import scrapy
from scrapy.http.request import Request
from ..items import AppIdCollectionItem
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
tag=['6985403505057651878', '4705424265105465328', '8839325962476453954', '9173056416112092057', '7518811492672851185', '5938076137530065045', '4796874939624651007', '6620318304467674670', '8539290840812404671', '5531585752430905331', '5008996811053111916', '7416123543703374161', '6818158347903315126', '5326374158913917006', '5226077824291973204', '9199566505992537160', '7429167052309537219', '7923322729985684144', '7100236098431821643', '6009168787154827558', '6237216560208436979', '8224081953044592484', '4882575830957872641', '7049348108305522338', '4629548824296547330', '5967572405200525390', '6351213219702625990', '6433721451746091708', '5724536145482691675', '8691250750863996664', '6990671124277762878', '5656437925259438538', '6278063915435122178', '6094228618053143344', '6133955275329314641', '8759329978782207880', '5068259210636929122', '5829200481094039491', '4724408783534569859', '8116283642168527192', '5674140061570326218', '5402281950510287787', '8196632901699712832', '6803739530592690026', '6239766606478987531', '8450616447014525535', '5948144461300778005', '6115615018010073039', '7469949316305141719', '6965716525887448941', '5989297588699821304', '8978277599595366986', '5200842528701346036', '7018337685370488404', '7577672865703546131', '5271041721352958726', '8454869713871668206', '6071653399714923628', '5786051240365897907', '4726011077574154807', '5025475328194808096', '5395775558123530438', '5916793707449251762', '7281777735470173283']
url=['https://play.google.com/store/apps/dev?id='+i
for i in tag]

class AppidSpider(scrapy.Spider):
    name='app_id'
    allowed_domain=["play.google.com"]

    def start_requests(self):
        for u in url:
            yield SplashRequest(url=u, callback=self.parse)            

    def parse(self,response):
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
        more=response.css('div.W9yFB a::attr(href)').get()
        if more is not None:
            more=response.urljoin(more) 
            yield SplashRequest(more, self.parse,  endpoint='execute', args={'lua_source': script, 'url': more})   
            



