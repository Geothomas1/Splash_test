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
tag=['5030558259263481203', '6112158426937564956', '4700756200397995264', '6799243928407092181', '9154300028955433686', '7518640404124942658', '6493980387780624296', '5641067919817566915', '7082178223243563741', '7950923318709657276', '6026692950321338040', '5492798222698967139', '5959476752388212784', '8282801122991822841', '6075558173358026955', '5190143215990176578', '7987175214570225485', '8387039796197719753', '6619374307879903002', '6771617653662978022', '5020058209838886315', '7158581874180778035', '6330143287333117546', '6989725972739045327', '5109096415192837218', '6244733812040127506', '8529613601131729173', '8099138519625088613', '5623053483787901346', '8397618600444674930', '6183097655149041531', '4733040551178709565']
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
            



