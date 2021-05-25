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
tag=['7283749095064262617', '9150916318290128513', '8842514874303574857', '8382119549645625419', '8713520328786207819', '6094284299996887380', '8560162257577595232', '7592429957971796713', '5599725018001477725', '4672011185132646724', '6275117263799294143', '7739323866949324662', '6324983890747629651', '6145372530887755816', '8696216234951434473', '4666479693962974994', '5803460148334258466', '8332172611342086518', '5282000619223025472', '6891079333414847023', '5778751415051947938', '8131189399913356945', '5269183489950559815', '8607872208291727196', '5804961650213804474', '7859138891558791204', '8348579901166079625', '6290983356531270140', '7519189995322500640', '8587707348801262678', '5557258465244632251', '7812288468579108768', '5377048679909319186', '4780965204769750495', '9172651815063772433', '7336490990953064365', '8505572370382073494', '6137702943820097131', '5328210429564327228', '4825368529348935153', '5450976432286054034', '9068814486223169993', '8251744921157915127', '7508913079769971438']
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
            



