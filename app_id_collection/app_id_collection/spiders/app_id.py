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
tag=['7277267556905944956', '5790222433485215852', '8284123889791093939', '7375063890083235293', '4946777650633029815', '6236189329207394247', '8018211599319541719', '4747799247319543390', '6074851420289717283', '8043566489894076993', '6402825260724424963', '5728226595623103050', '5766366711041032164', '7185703464677733309', '7474901038335397199', '9173793138349320479', '8130769886491361061', '6530006213201240516', '5295382507988316331', '8820197064479050917', '5876476130007648606', '7227587051161570334', '6488267948821224543', '8128532516213169694', '7639378078513286726', '8370476508159322879', '7621594471002651613', '7125885284350687141', '8381242180722924728', '8641791124571733688', '5648039746373421693', '6867976554126835381', '6485267666692575079', '5028378648527475712', '7438968370539683589', '7304956857020678290', '6656664110697055523', '8673691961556039845', '6663038915530323722', '8507617254782817771', '5715276226623964942', '7621977556026971856', '5066965259272233886', '4961168152819308405', '7742384784168379122', '8586650488773233406', '4954326688245318746', '5238445110307514224', '6886108436842788126', '6365129696809078934', '4663374008815632170', '7389342481551024537']
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
            



