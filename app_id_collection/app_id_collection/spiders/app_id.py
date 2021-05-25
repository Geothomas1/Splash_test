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
tag=['7293891251018750446', '5167591999194596908', '9137662572804271219', '5498699710190561662', '6796980865754218745', '7443526081535165213', '6737241057528456990', '4798430930326144815', '8733143810835050473', '5994775652714806911', '7008428324634535219', '7733259938468169053', '5271621021233800396', '6550639289090948133', '7683077181322248442', '5549044713487227941', '6665738483785114935', '5673659703053489019', '6492950143587136424', '6130399632031116561', '4776583492334133195', '6760444657267083024', '6025039303235685120', '8438385968429708292', '4996803442305230782', '6102680812234123116', '5596888974159450345', '6794131756288939983', '4996140693365022946', '6979777129606795877', '8809754564869974395', '7630298851185956443', '7065383379018117661', '7445731176067724327', '8671750602643018872', '8530921706286616309', '7174603090746362742', '9157205395609753148', '5408556930627476046', '8460043579802291611', '6169396258432401971', '7288352431580733219', '5601864764450877469', '4724861739547699077', '8770861462686537324', '4837874412965097235', '8275639371954610297', '8765485938159587021', '5455509314201354024', '8786368612559277498', '6509747124848411824', '5356555106019779737', '4946944220533206711', '6838177523226583809', '5156874239403628404', '7420910338744452125']
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
            



