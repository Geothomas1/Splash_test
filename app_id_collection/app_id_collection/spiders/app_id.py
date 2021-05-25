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
tag=['5894562685247515328', '9218032395852841923', '4851747018805076305', '8124115014787066448', '6775790002853394694', '7461459483352050656', '7557278021909701318', '6507382248331967843', '5697797339354704801', '4802823940310575420', '7594107253300563723', '9092911368589621824', '7182051801686781933', '8317518138458453107', '8399102968121737189', '6296818603726842619', '7691566363878910652', '9027768096867510143', '7910849032733790671', '6797030799392970719', '6193080421213965865', '9027624324456106283', '5453033126642634422', '6033443741999759446', '8510423619052023222', '4746622660500196871', '7713536791355984753', '6702827967347306297', '7593030124437647552', '8157688580611035818', '7647923447214702510', '8777231616861579446', '6419234961105920523', '6850687027727076644', '8910259174907448467', '7221230625429953918', '5735683794776533269', '7229798272352696433', '7097204531737495732', '8734202223933377364']
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
            



