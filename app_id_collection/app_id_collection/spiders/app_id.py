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
tag=['7455852383111396385', '5565617953710659343', '6223728622950716820', '4654955870103314230', '6623148093237657342', '8836267653634536076', '6810187386336246100', '5664051143872288924', '5813942451248631393', '6318820151512716326', '4628325420478223872', '6673401939984117113', '8453616620446981002', '7346334396824986990', '5629896104853744671', '5032150853772724025', '9033994160232668935', '8572513904409655270', '5164203443329909781', '7190673763242476318', '8113837962193343132', '6678595307987024591', '4634047496794859154', '8955738419362599046', '8932616818955220046', '6481056423040910605', '5121638969115946617', '5497235455163804958', '8058674947275408212', '8420210619522248974', '5648891177850034767', '7184966901370602920', '8924830907973699961', '4765600568941111638', '7979507058952385263', '8277403336581387825', '5691986325462198179', '7257657370093547812', '6266623049044259342', '6002203065877076379', '7864841952957174243', '6284374824436038177', '7185298486273712617', '5159036338926925133', '7627256279594342940', '5358161454286856463', '7525659131653245105', '8256827956657829668', '7627766590271461089', '7048100251501568241', '5846632246178772267', '6197543456908830701']
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
            



