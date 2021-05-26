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
tag=['6017920813301046912', '8014856855722099566', '8382438876050671303', '6125523682341459500', '8657364104187803118', '6184647823093847603', '8242007230470418333', '4789121393960183353', '8217601881841194771', '5500086056436930894', '7538595775088509018', '4744559207594823968', '5839528850006614068', '7323381933738908725', '5419057757705334142', '8103962861761737599', '5589304528147042696', '5628133900935419752', '5842073697631524762', '7999369250220694465', '9093438553713389916', '6960633251685672148', '9000644641182165923', '6672324286460664831', '7878862173002269507', '9151178108161893601', '6358399885102604803', '7806797352173616720', '6218065248943483332', '5194807779769490867', '5119191241095675629', '5786611168632929887', '7130452962130649213', '7654413900716230786', '8077342674707330887', '5923513214207758667', '5434668364201614200', '8296450397892209303', '7078910568407236473', '6269804686717206206', '8474056126590102114', '5661487373706422936', '7859513593998844328', '5242684734642358176', '5970545234728876768', '6775631092773912948', '6445231020892003022', '5709961888773960280', '5874568059802808845', '8945833224244442741', '6920379375921764484', '8536077871659961117', '7833736286912318665', '5259631011358911297', '5448967615590056551', '6465071433241388481', '7803821373914286475', '5400886004604298305', '6636036929415414830', '4693637645310909490', '7760935662578019838', '5558182897833213665', '4660711703558984210', '8104720018544131385']
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
            



