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
tag=['9024785033613347132', '4874816267220123258', '6406205477012277982', '7650266781643005085', '8007139963275396401', '5839009228202651904', '7155916540712254833', '7734912852975701154', '5786944734605531631', '4712012074177447843', '7657397522416896091', '8787400710408397605', '7685649251095633349', '6346546372609943785', '4705298051065995328', '7160512524880644009', '6456143002488072242', '8260943179739148532', '7186054758717029567', '4764447296923018552', '5425295683058781723', '4804911247287820805', '7879673693503976662', '8955066934454601955', '7186523347504857767', '7091157210497198698', '4704635207187493506', '7646835617777537911', '8637503013537959397', '8645821167129935437', '5380487398740284635', '7889498290704751659', '6543432390798002813', '5714576899279520552', '5578065933699990424', '5088016233298186369', '8579446343667738903', '6086305120070720849', '6252868932814796836', '5193503158089681326', '5729306004579477178', '5084686838291461668', '6996304839054709706', '8007676981578235400', '6849024866096914155', '5134145306500852970', '5653924082213188846', '7357595066704070157', '4957096291964364761', '5308901333316223436', '5331251284760727656', '5654276803117676922', '5535445381408094066', '5501423313311714738', '4942264640966703145', '8148519679766250207', '6614685948019853087', '5992804372998105965', '7553118301206664478', '7017086792494895233']
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
            



