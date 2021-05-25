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
tag=['8709344651191763031', '6152949195244037426', '8817236383700323055', '6213872326476172507', '8962563669957239740', '6107092709638492733', '7275653654606627196', '6580291353723787110', '7695967450850785128', '8201622235916682415', '5963965522434307775', '8825024862841600641', '4755087643347583553', '8017603995115202893', '6095685828291570471', '6044655329300031845', '9003735812430854306', '8483587772816822023', '6010647798148725841', '6712375327540776407', '6109950647441247547', '7195136660648752018', '8481738770013492665', '6853299925783926997', '9105012402214460158', '5103173010884337435', '7928658162170743765', '4653793284141226364', '5229457361184977321', '8432085252662320894', '8039883297156106572', '6788597056868513100', '9178808402024357731', '8117239212302166287', '7074450904720558835', '7212802900417352934']
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
            



