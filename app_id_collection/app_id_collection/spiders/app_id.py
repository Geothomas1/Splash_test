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
tag=['5454925992285925884', '6034378945926599401', '5374608753593108145', '7366733317637849836', '7022253202210463993', '8795751306910276536', '8843836569947671195', '5655836596785289136', '6601213373289127812', '7130028942974458707', '9194058832058361090', '4638996833280920077', '5844883844554262440', '6070284176229761335', '8172152759233474630', '5385422348746566560', '7035112057115406030', '8653110066422602147', '8231999334644942611', '7859404688570601650', '4888983757836759005', '6849828645906511491', '7125678068875737755', '5129047378608254918', '8085959976691816859', '4996902191836365682', '7200961128639493883', '4621019304630325082', '9086822210784570386', '8624849876051115528', '7376237290037835860', '8802905519543635720', '5625759341548857477', '6950240818345664288', '5905680888302571616', '8468811191165328521', '5107756675233672381', '7712994288003479288', '5584450278493352953', '5915533344107267438', '7344736951136509524', '8975362338365405018', '7908808390989363402', '7748803383090627451', '7597585547007246427', '7245606956955639978', '7913847794688620472', '8382546628989848908', '7692528489497619819', '7779032665725782714', '4823236994945755389', '4961783097982207021', '5946760657192009733', '4733069306827275553', '5738785398247362200', '7655275505059428074', '4997734150311182567', '4762108989375737816', '4826182024925534786', '7596352546733505681', '5698704764435009544', '5522405069148695933', '7866407308043091260', '8013171132272394676']
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
            



