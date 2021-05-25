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
tag=['6342995731669914234', '4668934121132289537', '5015614164434071583', '8268322353396886232', '6254066507905825480', '6652161207718409000', '7024278614265404123', '5302246096583475481', '6850209733834062330', '8089216097164571805', '7361099981261426713', '7523465495536214681', '5032575981749536800', '5310848321784419148', '8867515009520278694', '6281767209366412919', '6919505348264598721', '6334056915695072593', '6774717208644425046', '4928015747104013274', '9045910527081070289', '4900572350260281006', '8195506844305942637', '6619571480222085241', '5718732953562697502', '5319772794662103550', '6983898812738908563', '8948459530193160153', '5857483678333630761', '6664443611611737272', '6462287121578018300', '5466293758968802045', '7178363532503492861', '7782351777076755727', '6068288863030660321', '7032303034737907419', '5933307376193718810', '6026947153372361240', '5932082780178314329', '6632498816130253988']
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
            



