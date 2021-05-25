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
tag=['6110982057788245759', '8155466349370063627', '7050987846191348839', '5942361994464997558', '7064049075652771302', '4972816319461272638', '8956145082759427129', '7063637161723821824', '7960468984388308933', '5866306697629323411', '4911411802477037378', '7489594886728593506', '7676048301500326955', '9181216091790920495', '5032815396252122596', '6762212273028554913', '4918467768770751558', '6197931082107227839', '6649590652509275131', '4975500419161411611', '6401207712331056345', '7437356870663808010', '5115906669109665477', '6898465428242528446', '5030885148218785788', '9194831334493608695', '5257246860945271941', '5031002471975815719', '5255646171569104601', '6313080736538226098', '8713396108022974283', '7201829880177229746', '7695781366508118762', '6836129847219805741', '5749041885278326456', '7351193028544640701', '6748266307102985835', '6993478874572600485', '7194935609945692574', '7385414401044372562', '8352141510294024214', '6673393767038822971', '6655468680133223000', '7112807194957674533', '5655588040888751450', '8098532636993523501', '6857670021861511591', '5187629073610793871', '4831450996039769629', '8610760313453635485', '7178987708399992905', '7282535658701119877', '7603221666597073887', '7257166747297236831', '5770372176281996229', '6535213428686988443']
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
            



