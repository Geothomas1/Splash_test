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
tag=['7779004510808098402', '7208885850163751985', '7400869899693246844', '4845954736942800726', '5522385552623746948', '6687421036115960319', '8800510240309153304', '7464846162384441304', '6748824415117800411', '7076500837880329337', '5368817590358554630', '6839446417377474205', '5527509635138787040', '5973438933788006648', '8018673576652266005', '8978080717780688597', '8549610620990682894', '8055413842815519426', '5640882013833684092', '7948040281476983864', '5900661310906952866', '8229244296490825032', '4755826023556476760', '8488388198183321667', '7400563236019608929', '8059004494586457216', '9213539339654152230', '5652058647315453715', '5718060259290948522', '6482947269324760172', '9074369521088581714', '6190103039202443096', '7628950918694093364', '6441431861663790540', '6321507411823178986', '5694037912118792047', '9149796908166743872', '6206685411990055531', '6962043790606297617', '9024962201332143225', '9127701425612335314', '7032332895434218697', '5518665928181170160', '7083182635971239206', '5004076646959370987', '6926492978483065602', '4977632237942662751', '5337432179108084692', '4907013206830124310', '5604438105967310172', '8287846329676538382', '6525389660915785779', '7668431668227176877', '8595998371369390293', '8737320554475026419', '7025384100414125543', '6436494376776982989', '5961130251474482936', '9022360968474849061', '8120758647417753445', '5047990267947408434', '5307569455352308056', '5724912443219411247', '4716511330497003121', '7462317849588712931', '8454036107433110929', '6025358315131468914', '6408731963622295761']
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
            



