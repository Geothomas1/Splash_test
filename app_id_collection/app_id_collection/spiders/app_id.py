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
tag=['8943180154849889737', '7142288342533411136', '5649746626100204509', '6173615700887545814', '4917470758157102247', '6346418215346268866', '7918090238771879535', '8508112453254000796', '4750606678404618729', '8742305635385563307', '8427637182851887164', '7155628101827021124', '7197581759429692032', '6734942708062016803', '5126808648358756703', '6283447483380480042', '6573778536352984398', '5853456955487459105', '8667639847732959886', '8858357917831713418', '6058522034374956843', '8268163890866913014', '7402056523486813805', '8784617207395002683', '6225315284672069550', '8567208651956451175', '7281255057135066191', '8276009643201482025', '8752109862665474706', '6638887914776883120', '5105500876429605010', '5216019409700161101']
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
            



