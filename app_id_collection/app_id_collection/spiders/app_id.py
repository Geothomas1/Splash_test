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
tag=['5576682681572099383', '7748205786842398960', '6575769455756101427', '8717916819135898879', '6229739699120304713', '5907239636793424422', '4843900089693546737', '5075392050690657822', '8734356468512982273', '7227918126582259427', '5847989090736408005', '8900723080013644079', '8662942823952493047', '5496592682158177981', '6439791427420750650', '6276050894261583409', '5378460267336438167', '7207190132769406561', '6508553873090680206', '7808063932653629385', '4793319186785605932', '7099963475049345214', '5001195408893639003', '5046803102897321007', '8602142153566836353', '7842996855899014066', '8736719675219682339', '7690092173980578394', '4982815164057088648', '8421401517674642163', '7990966668160238472', '7571822124663361774', '5818413742592962651', '7665793249382334654', '6727532920148979538', '8390864336866649723']
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
            



