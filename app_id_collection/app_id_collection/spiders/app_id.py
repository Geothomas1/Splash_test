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
tag=['6912364080292089134', '7224990580681779609', '9168077694393863866', '5574990290619836600', '6321038402673563833', '7049037502404570242', '8131128488175432233', '8750824374692989985', '6795424472946988135', '7981974271066858968', '8527166107607249754', '6854968900371828059', '5713535194445576260', '5590586817582939485', '6793627170989723386', '7984326188031687589', '6495190637161262258', '5071720579068364561', '4801450099339440441', '5594949626264639008', '6192385722490864662', '7357077554773026171', '8964796452670258823', '7875597118855651989', '6657817875248174362', '8130048622570332986', '5049111248897315235', '6785719089730647786', '9195297237820315394', '5059399487265338806', '6370038073440670176', '8482407643425828333', '8158152773099656487', '6953151266645017120', '5889891896395932236', '8375636348799368407', '6119503451304895276', '6212438872135073083', '4645328656091439629', '4924423898094945122', '8365780106871534780', '7062447377552692694', '6680565987074242063', '4930540268134166147', '8569921424046553762', '5003073745404439865', '5700118808912373449', '5491574674132678829', '8623502759155452205', '8913547834687611765', '6330285788739193654', '7765388680340736843', '6200985419341822795', '5428815555502421464', '6262165380736838894', '7826419708260303910', '4620089695197417615', '8667970161070086593', '8451277703746469817', '7819081978330144122', '7693431271240399835', '5736940466556987050', '6826317627386619511', '5265550176477501552', '6813966546933628821', '8894772693497421398', '8206118674608292847', '5691631621868844812', '8170524783873652834', '6982967509927017360', '7774184653679959840', '6893996348905678523']
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
            



