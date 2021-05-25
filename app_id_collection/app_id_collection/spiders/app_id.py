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
tag=['4897634459422003616', '6791370992126495627', '5518892591601808833', '8091938452965664876', '6049889613192419895', '6892584399368201951', '9006998512451312735', '7009574438581835606', '7047883767346950958', '8064703926782987819', '4774993626400559308', '5627259507274857358',
'4900203843250105409', '8994122329528362387', '7692881620622944595', '6768585019053361914', '7597677812618449332', '8915398935794008697', '8462302905001548574', '8932186067746602374', '9048814734066486056', '8951910663104444856', '8844718586817142787', '7773643867779322564', '6221061492868898564', '7741169523487646502', '4847793641155972715', '9033209436076085797', '6106258411210493129', '6342866084855152305', '7080667429745331946', '4993659143112833839', '7564129100383742934', '8865586574070611450', '6294890931413869237', '6602005817237148276', '8447410866328691299', '6944889935549986731', '4895393381068725503', '8077917001173877323', '8473203491921584386', '6122063522863476958', '7391230837653976881', '4854989187091847670', '6509207742114318673', '6570343943680071013', '9133974485850383965', '8267492131525144101', '7824800856503386487', '8907822443510016672', '6328925782641286521', '6741037186991684298', '8094726331638033084', '6535041452612989625', '9055704443716780353', '4927475277388535854']
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
            



