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
tag=['8721501916892687736', '8558229615138913472', '5483282490080906244', '7920811193864196899', '7120854028166488936', '7553274869275570262', '7290233625471657780', '6880843692150926521', '7866251001808675883', '7053397787104765925', '4775761051658045813', '5914044639826981887', '6168512703224804094', '5945061049667527266', '6751831735137792577', '9088168584925525965', '6696120324521095578', '8109118806261349144', '4665215361516353511', '8845186186949051072', '8126367524894466384', '7234058793438796910', '5339076793638178981', '6439460247209426995', '8824194909212190889', '8639005082731214723', '8533842426196319277', '6824309161739243080', '5367497935076945448', '5275398609085533875', '4657336401010969674', '5476720985596858240', '5108502619843194316', '8587442742363712649', '8009831496945331257', '7751799722984789255', '7273046100443723364', '8507632293076702480', '4932990477609169466', '9023298587621708152', '8509087224415485371', '9187190393156464201', '4659029515162839487', '6499943181840817817', '6405564264043337149', '5752001918947518593', '7452042544814991275', '7565493331812937071', '5779626587264277888', '6236993332005361803', '7013885772412488026', '5197797415113272131', '5907450820591047394', '7013673993301054070', '6417243713901528852', '7582963547064226819']
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
            



