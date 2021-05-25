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
tag=['6306448674829026208', '7878009122471162106', '7601392885699381165', '8333143293815040883', '5279601646180713139', '5286790089270932286', '6091442766932589829', '5707397146287459126', '6442189179999487514', '7309930463025033601', '7199385734845309914', '6621050690545391940', '8147052735478590119', '5041937753538858542', '7693823923394883229', '7822713121776523400', '8100240259800312424', '6032614565346327606', '4834908731257138861', '7810577635981259177', 
'5453549494789991809', '6252953944251832205', '7554099845187918369', '7919312605181969468', '8561554078957047066', '4674373684024077891', '9063928225823989275', '5368474011254612936', '8885597054835947501', '6066994521290468340', '8183989433141828144', '5933611429942957630']
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
            



