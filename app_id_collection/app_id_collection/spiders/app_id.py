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
tag=['4847287205870814203', '5687814163475192536', '7641734230179183647', '7944622021414002168', '4850359466648372081', '7939739396857239876', '9172867825824684881', '5514879361694776422', '6344302991488910620', '6127848492837830833', '6372054041193931643', '5314941715970950066', '4964095130676259253', '7582197300206299385', '8455649790113502728', '6051148015985225543', '8677275286690408911', '5626085713830176937', '8471390726245753387', '8398412349719448013', '9010246831103135704', '4619979661824542530', '5774283050466226623', '7475663123286531484', '5095045684116794711', '5525732264088097441', '4933071823472176244', '5449328974441732295', '5311281200685912211', '8093724670779667147', '5811818229761754306', '5199034236944654802', '8755366808430380300', '8208304854085682857', '7249229138132830858', '5543333861108316504', '6358859332936558903', '6943708159739831995', '7408188148724066086', '8785998570686041469', '8911109639505826094', '5223953656881135476', '4910263493168597875', '6576687495902179461', '5686178314316521916', '5415272214728400872', '6885268735161974635', '8266846013795088174', '8647652420577360349', '7577394967225644948', '6222587985411840707', '6202116406895586041', '8177764803573251740', '4989017747836324536', '8725229887452798242', '8378751803683479501', '5243193811423278578', '6813210081623313883', '5406979096191826319', '5591497668065024461', '6947698453947986172', '7498870463320261030', '8394805635908725036', '8332615318778410018', '8232608788311593872', '4689267517702376328', '6873506025272311897', '7005246395238740201', '4867608459795379320', '7683185531706904227', '7264391215718150486', '8774161517987365051']
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
            



