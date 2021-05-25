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
tag=['4855130611498364316', '6093352993398167860', '7011233263819374462', '6814092164763665024', '6246065000957952309', '6309454660779365011', '5888460665412460525', '5186911209482453181', '6225048255144253010', '6775629480928024144', '7515480061471658211', '7345012756723220198', '6667084469034700808', '4985164453676857421', '7441714947163056695', '6440564140276616378', '8408476106489836105', '4974705534019282284', '6947375796369339928', '7590815180117612946', '6198302669601833079', '6581639190552237110', '7057991287898902125', '8675218270656682890', '7487031522913097725', '7997519679277101122', '6664193375360676681', '8730706130844478678', '5326442596362075819', '4815994421315093803', '7124330998028117760', '4647322305733638943', '4897263483617551852', '7817043497710646306', '6573101156789714089', '5302467630764439507', '8959121300552209162', '8905638241099435713', '5353426033492446280', '9179663449544633208', '5075666297389476158', '5612651096702285719', '6483394247866966083', '4668053405185766149', '5597790927388805801', '7763879368624760772', '5500701453004013549', '8452786924064733106', '6405838649550279680', '5660622683758606290', '5494672990680454820', '7297370861400908349', '8950577524693187618', '6753241411459191302', '7975875162379106117', '6456574067886363117']
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
            



