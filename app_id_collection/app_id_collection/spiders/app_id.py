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
tag=['5618359968547622675', '6009596001004613657', '5444078246239418222', '6771367032574225290', '8451224868666847322', '4851937824680914423', '6388091340693855706', '4619189391945421469', '6912080349644995010', '4714929692502465097', '6939136607373189165', '8322231146791187861', '6471209344518827374', '6993789714792805126', '6427017515650316640', '8138864662765360213', '7944632166339864791', '8837927194666352270', '8882762324310362801', '7189785937426947458', '5443589688751144102', '7427339023813824229', '8360468563382595973', '4856301758665930572', '6887911351021456165', '4904411149839398490', '4626552963435708431', '6749058773626431687', '7763204046331663699', '7409330339480770760', '7085161160987827872', '8916171025654224127', '7268898997815915359', '7666709667877958099', '9141563412839288966', '6942000361635813428', '8184141546793711948', '7640345417699712720', '9135829080968193807', '6605166034023780330', '4782352504264579263', '7306303968239881894', '5434856562043187855', '5152401689162712468', '7185863685995412797', '7417365811267480065', '6480186809591449078', '5750196497283445588', '5507025021813359851', '5709416098328895334', '8436941191418738541', '4721556689682137567', '6164101710769638692', '6110510903439204737', '6977835865753931974', '5015266578532322195', '4791840901148567689', '6444156082126200344', '6256141919349101796', '8685830660901726320', '7197733307727598726', '4773299176769795321', '4856562856406690527', '7211240420787885936', '5177674863654001962', '8442902954194777187', '4764343509860143092', '8721792023405436016', '4974670343973647824', '7736527093442553200', '9063402259407222043', '8119138727408860896', '8695218616884672041', '4738879279526818733', '6544294840756183324', '7861453436981849383', '5906039958077211397', '5156685669113307397', '7232298937605828489', '5859017026485744973']
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
            



