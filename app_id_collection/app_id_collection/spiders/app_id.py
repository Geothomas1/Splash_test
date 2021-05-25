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
tag=['7450417510196716807', '8725260485258606043', '8927338716811338704', '9206573628734900868', '8478374231979388910', '6402168187382980906', '8073794341193570591', '6746894261871291042', '5693997834933454692', '5905534951482923420', '5916677409102385570', '8319594159809964191', '6943838963793339591', '5153795527760814480', '4731189099066407560', '8629022729284169602', '5175102531862923614', '5534863732919297125', '6116618295609171607', '8335366955203612525', '5460769146474165337', '8789208989100679119', '5938833519207566184', '6269370758281416227', '6957685454452609502', '5905438781451669270', '7953007503920441591', '5766904818522015813', '5357898237292788268', '7538110937782306003', '6817647156581849686', '7032303803416115669', '6526807138754435823', '7626528234114733836', '8041327832030368020', '7561306168243011816', '7198373725572967123', '5940221413936365084', '7118874647598282669', '9089903639959809517', '8774208734991169216', '5823807334714730268', '8354912299898972930', '6531130151702537077', '8151696130014367835', '8047796482649164991', '9183043342653753079', '4711502339635425028', '7975720819912098428', '5068847949397915095', '6286060360132109453', '5820640837933616286', '7451296643970576309', '8803255959564310285', '8691236274801119981', '5050630332065951284', '8028061365935195541', '9075472648840041674', '8615867011605523085', '6331872437204939821', '7359320133149714273', '8315315095315966598', '5661093148650447713', '6473407804312298372', '7209640446722172257', '8273134989898180729', '4765596083042714620', '7996135378241325206']
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
            



