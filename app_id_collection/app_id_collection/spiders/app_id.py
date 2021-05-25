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
tag=['8360896942431181195', '5608956329061482342', '6434255648460618635', '7538781077315144320', '7246671864279448362', '6056688440439515186', '4838747547790416769', '6953512990229178388', '8433962063330964923', '6809958859683289607', '8571114931111931997', '8640640119251035352', '8898484184862676254', '6301433348761296574', '8045430550902323355', '6900076921334958304', '9177161936038442527', '4757778733768552132', '4722725367028242162', '4788520536104815826', '5313314117424352644', '8035469396420417176', '6726214521466300746', '8041942960973525488', '6141822560324008098', '5498003471817844893', '6529535447744118858', '5218286818115018278', '7848220853008457885', '5215138302300986636', '8727156928745342001', '7099069567967593756', '5471113979821841219', '8223591372369919986', '5088700216884305259', '8214387226544464743', '5037356001657364132', '6090565911491356656', '4657234256890252226', '6773510280946221606', '8870380362830297451', '4769784715501513873', '6385595102514627403', '5128247043278195630', '8129104754623123928', '6795455582360343572', '7414572194241764758', '4964033419274518632', '6675318340245338110', '4910317167788867349', '5579086278019851339', '8349252292748478776']
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
            



