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
tag=['7067774811407542797', '9040234912198379053', '6371432843822743336', '5680423532430186640', '8920034269562060728', '4894008586539345362', '4635849298843013993', '4785503010157418232', '7951118518332869031', '9098232026026749995', '5551663097723105743', '6381865564348393435', '8047777886056206275', '7619117349658882627', '5448635863614201206', '5657945287075259088', '6886564471574175138', '5252059894685948474', '8306713433237834214', '5498168134670956302', '4826827787946964969', '9140745422489147190', '8935462946679538264', '7063148299497943432', '6413501468238383679', '5464069849262017456', '5436096482781596811', '7589750362749800208', '4733647434788408208', '5489318347364161461', '4740431411518214879', '7559466989659892180', '8754264732913048176', '6996361088306051084', '8805045002538983960', '5619129883336263711', '6416530365823251089', '6673589621983030078', '8369629392252386483', '5509112426504227243']
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
            



