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
tag=['6861780579904438175', '5619705514579381159', '7853215840962813729', '6711335536439627375', '7878739734537858311', '8014379719892422968', '8595758521518356894', '7993261173536026363', '8777057043488957218', '7328080612526510733', '7558414237076230665', '8127130148333466418', '5229070112536767347', '5663259854341670677', '9060101706093336387', '5636266799010625325', '6930096309844876977', '7634823805541474057', '9164253829251975204', '6473421354871744170', '7162705202207596178', '8007560665522658101', '8902210573391972244', '5054062184596018525', '6141132371121472740', '8377314319662536433', '7853787288794178537', '5926956842675325252', '6636365839273971543', '4893651774469608298', '6670339010912734522', '7166902830376215526', '5574587989957479403', '6962870384886979694', '7618231268159740424', '6721700247509781910', '4612448863357374554', '8049938545889616732', '8924066410704845047', '8055727943405100863', '5481404911511264476', '4842920517352227799', '6808775547707213495', '9044078671576515925', '6924870766143044594', '5323382055742372105', '5759278118004073561', '6120712040925683714', '8323708780491861075', '7677444116970178624', '6455514886003965814', '5368977278588192702', '8123119289979542452', '6316107869278086027', '5062936828841364895', '8971365357671309751']
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
            



