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
tag=['7260620016824528048', '8332919416286263192', '7231766101336721409', '6900405775201586818', '8930875377393121766', '6346650809574709290', '5523198071083763858', '4775682139646061496', '7676639753677707554', '6603474980694116610', '4814606819870230850', '8233022382420300363', '5344809082234748158', '5676678248117707014', '8065875049254042438', '6077907784377178469', '7353063306135692755', '6953388109633466012', '6871295273749852876', '9202133717490871190', '8919209511768807346', '7491037096017880494', '5738153851647753588', '7869525314130408224', '4822138275722759110', '4838241904142787596', '8225982816274219161', '6265231972066557049', '6810740401537686844', '5116267303378645901', '8441585565200371907', '8232444212807332118', '6248685388663461441', '8824297098750550401', '7173727390354840125', '6412711161965453869', '5260096596716620160', '8124300348530687784', '6351867895812839703', '4725576691027898381', '9092123354421353761', '6443480545826427894', '4969444090817677319', '5339945739868969483', '6805147201492693872', '7905215815722896088', '9028081560946224212', '8702749817661403581', '9094283289885491799', '6141841617372451435', '5455755705389667930', '5024696630416017326', '7201044287780351818', '7956323330814532594', '8603441533298862984', '9041369024808341661', '6985261208004197434', '5925953578101341231', '6599001017670379452', '5148082945422081818', '6087819101008288176', '7669165886359187478', '5409072382190744223', '6020382319060603158']
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
            



