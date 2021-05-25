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
tag=['5663496208098137848', '6115358488257854580', '5455925704315559997', '8988717614304464293', '4992836406033283005', '8637764171515976038', '6971229775755584315', '7112691348819225528', '5693910964364121877', '5658142575504481926', '9081991731474059433', '4869918833570187740', '8593356627512113446', '7330845278098725392', '5300624026381211755', '8408323534062278928', '6111798801042002051', '8524440976655517414', '4943075009961529190', '7353729039261808634', '7138242582101926969', '4740596498444893228', '6642778065760590824', '6286289897059848460', '7865614637046805833', '8857677147367483293', '9037896777894067627', '7565840919027523325', '5997593423516988653', '8974970846236633270', '4662810320550258994', '6623238395163942572', '9177216261648079666', '6154894940222162077', '7336076906108707934', '8280537453226763547', '5486973760992909009', '8920606864698807978', '4797307650791917378', '5113296646248337040', '6485779010633223428', '6619707399005275332', '6296678790393139502', '7569628894701346695', '6881671506680852216', '5382447624152835511', '4929553837499012638', '5502177812307200646', '6454325223609441626', '8412877336329069138', '7449035579201814859', '6312628331472002643', '7266082856721941713', '5994138348202125876', '7358994364489873550', '7070726199550234682', '6103773027555268825', '6452974747591175011', '4879644027951830086', '9030525507520936545', '5916831190645200918', '8837249034772914852', '8002351706703714808', '8170837540813677500']
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
            



