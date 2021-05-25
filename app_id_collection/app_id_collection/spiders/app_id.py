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
tag=['6760871744342669776', '7468745915535889361', '8160485875019452356', '7921862966629273286', '7006468444951894025', '6555698778161546435', '7200356149375634993', '8080768259564619184', '8620593069625121201', '8989655195006515374', '8740289745103248198', '5425572230181070516', '6696507953413740214', '7274282074513677494', '8656461636233614317', '5050706477693664485', '8973246234205879666', '4654682304069795192', '7036861075190380108', '7358969370933669404', '8721312786193161851', '5005325034508793006', '6192667579323701146', '6424021119774221426', '8880462694454653791', '4781579444618139136', '5181560338502891220', '6337167373540563908', '7980827319652908866', '5620429711998667141', '7623922261649422304', '7294835878582909369', '4688201469897781893', '7574109277642013389', '5892741966948041847', '4860952496401002204', '8887068188251280731', '8662437737802198261', '4931006146103151892', '7850045072293031762', '6726689356187947345', '7696637140094003672', '6456260469777134332', '8879023778442973677', '6670543100264799560', '8760754333222750136', '5175331711517758204', '6079289435999763719', '6591182278551150548', '6467633216745407879', '9089565709447803077', '8784294396882762556']
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
            



