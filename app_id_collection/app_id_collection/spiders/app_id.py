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
tag=['6443412597262225303', '5092489278969419453', '8766882775416758528', '9194365566590149373', '8927578178800480570', '9099568062209413784', '7448136641819372624', '9213374184565087355', '6468448009844256886', '6592543518245052099', '8519316346026653389', '5491963132555144993', '5634953787459217343', '8575989915079616959', '7835810567632300442', '7687027239252953100', '5527922306813521702', '7528289262603156947', '5326185432315494464', '5341877486369493848', '7661111826513259000', '5093519374571024344', '9047916102574510533', '5336419054352826821', '7974885382983319843', '8661635803193428456', '4971167427705968870', '6585296647535761811', '5696323743535622294', '5819088965110992860', '8823650727625885259', '5731754896454505070', '8062922552328347561', '4931084188406124932', '4752478276916206857', '7133304247214104051', '6365251617849781346', '7531380661925692871', '8032556025519242082', '6629301397797241104', '6961599176046611679', '8235847276298875340', '6926575025651311904', '5941908837406018479', '5793980904747267349', '7814188751031376182', '6887243231199955537', '8801158803664614119', '5817729045804332618', '8957107062136112050', '8258359126933873328', '8187972632072819500']
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
            



