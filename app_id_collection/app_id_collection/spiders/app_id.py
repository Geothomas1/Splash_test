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
tag=['8511233121945021706', '4919594609020723282', '6532362423920659842', '7480546189398586667', '6367901761320314739', '4681079823742166073', '8022783081923446757', '7683027438655020608', '8439696984165862320', '9164452242719817477', '6166101841868167516', '5801011190684159526', '9129620811308376831', '7729503051138227560', '5333313022014442464', '7000798087410429620', '6598925264789215622', '6246778507065623918', '6350669391660629382', '5327716026561405577', '5142041840723457606', '7014085520072233084', '8788858875415345331', '5538646943499039881', '8375257734492435347', '5187416878277049717', '8252153021639297713', '4887120586948009446', '4632290146912595245', '7642621079877036795', '9116667499785315575', '7986035664752008740', '5093524227521470983', '4808744895997591112', '6893486166112527112', '6001089462750320586', '6330760760534114817', '6572622508474611452', '6623673247047616240', '6728276441633336300', '8662897888391640028', '6654598976892185391', '6648802986441531007', '4992030870609250669', '8724793107773513951', '8270619631307981029', '7354965985138233118', '5271199381549403266', '8983613559340316525', '6169333749249604352', '8019378777591138434', '4714478480563240331', '5979465799302472201', '6620987035265026854', '5829283664866033439', '5629340268753502293']
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
            



