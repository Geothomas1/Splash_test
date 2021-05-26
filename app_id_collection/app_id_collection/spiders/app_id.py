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
tag=['6701362177669633767', '5815239504306297457', '7952720040734185162', '6018285424133432283', '7499256512358365541', '6610737040402996468', '6166901007283349853', '8274451085761868391', '6301755157210115557', '8543608235114042313', '5922919954166686783', '8798245466605217500', '8119229856273856257', '6003967168349386457', '5098998022514040461', '8670719948161597272', '7725402557584400079', '5809562556229343209', '7959864725542648986', '7868550296219264281', '8580624130716533255', '8468784292013491858', '6947556644764074972', '8031295638675999757', '8950393860599764952', '7642594770614125124', '4817793232310892365', '8758563454050477814', '5379685710960729317', '7532879156454387436', '8228703397536036345', '7961242804719675600', '4790476561996637955', '5831741218298092798', '6684428555030517022', '8774804613087723819', '8202723012657381784', '5284643674100261978', '7980043509581610980', '6976192343062494733', '6070161350609535667', '4708751211546649787', '4739102538760287077', '8851066080134344628', '8728733250954036305', '7893226527422530588', '5853938972360561823', '8997071017052053474', '7606452914412415153', '5995605107085635372', '8661793916848775635', '7176940439673770906', '5322927662824790872', '6803116255087799045', '7863277015281640476', '4846188687267655842', '7049547296456333527', '7685035892551595386', '5862715948226110697', '4878639854060206927]
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
            



