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
tag=['6362486356489191167', '5189648535951667453', '6873380610601889920', '5073499114004010169','6026694887861433090', '8512927906427199463', '5893617769670448518', '7637933278077959289', '6931667906782760733', '7971703256694375923', '7922759924555516929', '6295400766369581765', '4711353706827542648', '4953443365699999896', '7385958080524828270', '8393924255291119513', '5586168019301814022', '6472385040152963370', '6926180598799437828', '8429831032655153713', '7697512938933308671', '7035319457375052603', '5825403642343449037', '8854334508530464044', '5511903698132849539', '5045439400844702446', '6626999113762703513', '7689876207028565624', '8291602603469474526', '7487302895684269573', '8482967742627928359', '5525099005655730103', '5839867742890509836', '8703435308336497104', '8194087058443607932', '4881549472206186235']
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
            



