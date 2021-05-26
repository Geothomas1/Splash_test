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
tag=['8052857718479767130', '8288262907859162718', '6871333323804023406', '8144560920157160997', '8840275148517916185', '5160763757107307799', '7564250809195931612', '4899229968192994879', '7780011900367662392', '6941105890231522296', '5128480142319974805', '8091370783080636082', '8948310341520683798', '6712533027504459666', '5215172046080669868', '7996423184792507522', '7709362894858980437', '7720251761301594831', '6402406619451360547', '5380728554997621414', '6558247216676845129', '5097326509064501503', '8618995061425218469', '6017800222101031429', '5045508959348955284', '5032127892134861949', '6562506502134777861', '6464165062797778250', '5500450383537402080', '7271654417927588971', '5868342254102788529', '6548192679381869603', '5800144487620285777', '8386891944232233548', '8051992276947048001', '7316137962324369721', '5669903845012617708', '7409182767575593474', '5971021115117449546', '8784513066436316151', '9190674693874246066', '7791776099225258043', '6365513327125891458', '5183518088931537411', '8480785146242893448', '6859713867874290897', '4635242855942916199', '6960447674535343883', '6105397173469570331', '5633654513268850863', '6032270301651614018', '5766113960745724007', '6398522159274672667', '6548637148975336625', '8375803120194789677', '8656752538531470117']
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
            



