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
tag=['5000307027490568933', '5002593037730106752', '8349232061000500898', '5002455033013217816', '4777856481218581718', '9115557028609815718', '6667366980407626999', '7315871763609983366', '8684502731112464883', '5890018970979485285', '7543064849642768907', '9079752828853170727', '6576060097627578736', '5509190841173705883', '7734830694736534397', '5316747288696116828', '9043404866040791120', '6490540235565334154', '6775832922103090311', '4770415058479586286', '7164132871186129488', '6268808053666203087', '5826002811394195906', '7057283445019212911', '5882407778764149433', '8673424912729904038', '8207072281355006974', '6840951696003009673', '5890015954082696461', '6266607152549785498', '7554671338110666641', '5738204444872784095', '8633276600546047418', '6032977018699554090', '7652983166712939610', '8403078360560227983', '6897806182062372919', '5454698704753485212', '5892841245660927044', '7403510959879597368', '5375354644779620212', '7345548967311590120', '5596175828828287744', '8399679545807573826', '4759811742219113753', '8389723122134420156', '7986275276826158442', '6751356956094091876', '7787963815078835476', '7562205847084179468', '6593142508637677912', '5527786497421104075']
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
            



