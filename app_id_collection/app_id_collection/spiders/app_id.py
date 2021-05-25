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
tag=['8081264977535938266', '6375024885749937863', '5479878731323183535', '8999084889030602957', '5001298899523389669', '4723459566459821336', '8474288931624668520', '9035921144540693824', '6454249284631887425', '5265326881483066144', '7246933359902698932', '6482697635542692723', '7536851431123862482', '9059648227963506043', '6244844202930740830', '8794716377940000321', '7400125658715647154', '5539851475818539181', '6274422522665469695', '8218268243812801680', '4908169615174552493', '8012857673010307178', '8718097319476257832', '5424511883716777141', '5055506162912678166', '6467871427328249922', '6027406050732066053', '8307251952202559973', '5550963862271632728', '9037518238182163411', '6595101323272314112', '7403711233099240213', '5184284088705603518', '5257028323002340274', '7897976090672759214', '7044704480929675112']
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
            



