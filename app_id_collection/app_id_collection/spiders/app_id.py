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
tag=['6830339488752221884', '7849730008707515899', '7375824285319233071', '6713406806947914827', '9057332195804786135', '6184138450187161064', '8761623343649781520', '8544456226824965855', '6350990125305911791', '8602779468616856993', '5516478294027895010', '6068374008865178847', '5490090562187298889', '8624114856010018691', '9080418954315860537', '7279442145536320139', '7980974069758858282', '6159169127821739819', '5511622873445062411', '5032227129075394102', '6499205192421311786', '4739868172772735957', '6265548927972932169', '7863076378126226297', '6106591036287505196', '6766797635574319737', '5236132833572659868', '7767821347699849360', '9041373128986035838', '5190115240305349702', '6179794243705556952', '8086300301097840699', '4793552357180811299', '5413790841388155219', '8532457180929134833', '8508582254244273924', '7450131230893424819', '8945271067801023479', '7395487378585323007', '7747675122675992956', '8835859590350437090', '7112108559653747133', '5564068531050959250', '4647289173987695686', '4725615955378054830', '8815230470063088971', '7862297425847796298', '9013010095346425873', '6496128650038483596', '6658958570055935437', '8508141389944351967', '7026341831517284926', '6446514701464564478', '7003751624917590236', '5906346538712222747', '6474367905076154153', '5512127381496722543', '7233434502807631796', '8941394957105540861', '7795842308138272179']
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
            



