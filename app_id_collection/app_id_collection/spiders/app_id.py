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
tag=['7065081805875144950', '8692996074079909386', '7443485104444030548', '5687273344499948433', '6058876897349671351', '6065070488969278177', '4891063256694501336', '4982410150783083654', '5186778135420058626', '4970726922498388416', '7769366979601471884', '7326920226317918390', '5406087987857296006', '4876399437293036379', '8758028500167036554', '7565157942012339236', '5782943467454304862', '5849393469195873334', '8131945433173477183', '7580272089034921457', '4903572435611033573', '4652861614931863893', '8655332648829694833', '7218934167467173100', '9050076692178953988', '5917371497212543150', '7117847536434853747', '6237450269561629881', '7194810861563908518', '5132799519198769136', '8565390775868410106', '5608175256611330044', '5419263900914532673', '8309959283364251417', '4745641900732694767', '6847484700613088928', '6490650028603678221', '8258663382168572156', '6801327324122919897', '5856860109760086175', '5476581720912379844', '8131955164123013024', '6898251547357723394', '5225259139704788328', '5523152170640732668', '4856674160792477318', '6205833312517348946', '7619928119234185691', '6041565480154761482', '9008320467149344433', '9077046431383856414', '7021124223418022621', '5309712566868291219', '5458114422910351285', '4976339756140289064', '6603385326117648226']
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
            



