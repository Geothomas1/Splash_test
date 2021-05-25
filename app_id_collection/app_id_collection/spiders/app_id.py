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
tag=['8633921029894576093', '6850516909323484758', '8370361226290054499', '8817065164862761736', '6895527317645107928', '7094451509111429462', '8047061331915382779', '7982814415950435553', '5095490389686529219', '4831866344484454872', '7972143603605848622', '8456069187984922570', '5458548859211830428', '6787175416888052145', '4766574597652047234', '7474025739963323294', '6690081412016968981', '5704432803722128320', '4659533078121388193', '7053489442733482298', '6555596897387781530', '7022877692755888196', '8566893026053814727', '6622272058937040810', '7710637777904825280', '9073701198403467753', '8126350006038100181', '7264733197211807975', '6393726995712000550', '8899065730202222152', '6955115985723070470', '7171874514561735692', '6795016536230462530', '9202514608479563950', '4663602814184701637', '7918410002185658908', '5010178121124448173', '7299713048019662385', '7131760170112331818', '4702977435323678823']
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
            



