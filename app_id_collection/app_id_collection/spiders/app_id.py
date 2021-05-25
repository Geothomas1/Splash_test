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
tag=['6868270558485544137', '7680835712265407059', '5547061053835697166', '4730366959171565998', '5723010796773653351', '7518768913889957312', '8815886658662427637', '8789008242285349083', '5611060368826643035', '4948699111141426435', '6075736819016455327', '5207120848651743105', '5111681870028343903', '7252933074709348199', '5289992214197329711', '7960400539253051173', '8955217944788638045', '7093906263261548493', '6306203537800573543', '8104607978218558787', '8643636801389944522', '5025055235544243089', '7975617242323057696', '9028773071151690823', '8920797348503464233', '8625784257554818676', '6681606924556273560', '7323445163548927341', '6615809648420562690', '8795443019107304361', '6373975433895862443', '6299173333574516062', '8762409391147516532', '9014127775828288003', '5271770170668986787', '5304788608416827002', '7167385607482562497', '7282226673529026474', '4722701091173003730', '7886462319320555758']
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
            



