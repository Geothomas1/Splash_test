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
tag=['8589075223085910946', '6650834186977515237', '8358756008268462526', '5000569706213199201', '7868411720817775951', '8515568343609001999', '6938298709975174416', '7913994625101152757', '8200798554206155238', '6743393923839786514', '8309695933815408824', '7484419857666127755', '7602978102231839745', '8619611150976893500', '6587132276212584848', '8890723712967774017', '6111519313570037491', '5414897073837567444', '5333153968612647110', '8869034413793298378', '7404515537760712285', '5517054645876426707', '7863201505943162054', '5939615022080696941', '5513910508053475374', '5299331269432868861', '4885417599438872680', '4907572025980617983', '7324988016582852208', '6943021025006889296', '6928193833730629774', '8723049441097578550', '8006904489019665740', '8822969577404048962', '7184124210650472734', '7132655361321937613', '6542629453112769547', '8435593180733910238', '8749913084192358255', '6732635997720242124', '5198195467565508961', '8487402377460617298', '7642382398572009715', '5940184662372695832', '8122330999794743500', '4803759912553852966', '6422348890433089428', '5047041295977488190', '6163102761666559735', '5701903548355780845', '5868280839211498375', '8197613058147804975', '8687904899358370769', '6894174744315201897', '5152308042470685378', '4890720064902740707', '9072547481264810908', '6359341241047165543', '6102954125919756310', '8641955660523692550']
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
            



