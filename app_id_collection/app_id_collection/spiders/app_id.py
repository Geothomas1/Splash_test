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
tag=['6231865228871805970', '8495314997069321006', '5690354516027987975', '7836288565757644649', '7630802525166577768', '9114669831982867175', '9118647368512655676', '8334254364112249823', '6849257673288467668', '7136444214307797007', '5394081770973981948', '6901479092928353978', '8756932539650848128', '7279522209780705556', '6256086716650712908', '9157373646962199653', '9067383956856548403', '6297861025057265272', '4853701633246693385', '7840149044341635214', '9205902632927830308', '8879167528622083463', '6016125024942124441', '9160370153281633718', '7874133619884098948', '8265893209493089384', '8485686574326390435', '6266010547161500656', '4812837403358483535', '6425246176445234147', '7462069034001648662', '7143198137251857748', '7619967318478414945', '6323245562758811379', '8375338338665946579', '5248901395331214625', '4653975230708469146', '6896856179995238998', '7965961349776285505', '4903868956461810528', '5690185289338687730', '6590972746235966972', '9076157968089029721', '9161476813136845170', '5151818854087703689', '6141247908935079033', '5850876700002153420', '8133089937868527365', '6856187845089861642', '6683147022031270212', '6090925400484661559', '4884060234762127302', '7805248238920941167', '7769968743817016500', '5954111817996472402', '5979976167515684404', '8861938524772156725', '4970148250064615345', '9184881701604535163', '6077510830236742095', '7722992552834415439', '7391880357029014337', '7949958676360116567', '7362251228733740878', '5490832954180067748', '6627606971973873645', '8677751222774589049', '8336163855820540306']
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
            



