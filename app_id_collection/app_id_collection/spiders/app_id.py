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
tag=['6555538138493147922', '6389679095177998345', '5527787514429874716', '8946436395320639539', '7587330522149747926', '4732780770305529810', '5401488351829628204', '8571468061984996399','7277785332880557957', '6622016126453358044', '6739087264861975340', '9007628073524743938', '7380731153298405358', '6034891875644208868', '8198341866118302642', '6846503728639896811', '7672183261604154828', '6364949389057513748', '9177588281631049763', '8183805129294816382', '7029605560312600226', '7131368833126940466', '7554248041640319901', '8127800996495644173', '7272988879797171610', '8693251563995698001', '7051729202084884545', '5381738668253204936', '8983550861078733583', '5735447750101420287', '9169504509079500539', '4946022439885210717']
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
            



