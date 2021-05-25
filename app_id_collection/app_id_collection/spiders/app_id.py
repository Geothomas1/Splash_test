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
tag=['5039460286196969118', '5128208987758558553', '5517637428189447271', '7574154127287404965', '8774459497508445789', '5573120919391396634', '6101232578384138524', '5883418072138171104', '8369606426111529570', '7772384100649578210', '9009912429300450251', '7780059519186224309', '4911276338977614693', '5359655127638739732', '7127626510594655099', '7679626135834422628', '5547585148058878849', '7444902431834496088', '7733650642632751043', '7270614203070989193', '6443788179149742661', '7588171583000921399', '5184621975708307040', '6575683316809605197', '8031400223935131125', '7809513148356916735', '6020733115124892845', '5932596189313949745', '9026500999365264960', '7831221183805516905', '6758225821733601085', '4995601504388994075', '8369152021837099096', '7230317575519619924', '8765977911568979203', '7825006445752690835', '6387245920606023423', '6142415895972817481', '6884684684333433655', '8642171094960393557', '8338172865073011815', '6847836412372290994', '7453591930180720827', '6650160508920219065', '7666959983519077592', '7759993111842582242', '8958521326688714613', '4679576420591606773', '6454292281679440503', '7691570595892880392', '4989740559356104293', '5178008107606187625', '6952287125999380194', '5562046520478176808', '8089005076453014627', '8928737614974754628', '8884976003639169217', '6604760358650103724', '8256976189097320048', '8995013110722610686']
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
            



