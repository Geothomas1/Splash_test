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
tag=['4854011182793806084', '5299003850631260582', '4699392667110365378', '5434749203337393219', '7280705290472613668', '8994722130248488542', '5301050295725269906', '4908996284279772437', '6728283773024671059', '5045715064689189151', '5087694153723898446', '7458738730851072316', '5518163122360625226', '5279028808921739697', '8308626920110310494', '8163392986512007340', '6103668297586979839', '4714436667283840468', '8749176906064522792', '6499189485789876195', '8186450013190957358', '8811278869775156893', '6908176202931592122', '6102668335549035427', '6812684529346551020', '4625711489846318480', '6881602746295386341', '9029878674450814329', '7745531991038565664', '6999218735152925636', '6678606332493748807', '5829263291154071702', '4766186280224708712', '9187235250482922929', '6974647022817710100', '8129089824265331731', '6569818037481967429', '8808585362607488006', '8321223047702517551', '7690513577357037429', '5063979571844785386', '8097565524164483108', '6551811748895540876', '7148680220855906998', '7478868556793548501', '8426977977500255132', '5461911460315957350', '5437027421754529800', '5415633757696906248', '7798711536202797318', '4672619178412368194', '7805280595637029855', '8505327165061518862', '4828013592739609218', '6036841353934681166', '5293622991198540990', '5266198448768244871', '7582351583795105682', '8530475575054247753', '9133171358375876632', '5642888644503198548', '8559932296277718300', '7770085775784068097', '6289932201800189302', '7876557512916549298', '7445437296895530546', '5042206434017001912', '6617181916911577524', '7933484783154057186', '8653651714536166889', '7912912614199852875', '8032126467502502670']
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
            



