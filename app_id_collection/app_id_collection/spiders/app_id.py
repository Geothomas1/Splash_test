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
tag=['6051951828652749513', '8976154233206800256', '5670846361324826002', '9092109651615708822', '8583925737760169027', '6949036121361370906', '7264345703847394996', '8713494877388626819', '4755598692539969252', '6100527413667243104', '8802639270489632480', '8379702474749938820', '8684447088807105953', '5157401662591324256', '6644798392464089145', '5978392300521042263', '9104629181226582070', '7056325106056904290', '7523091272503424127', '6660525472576471202', '6238109878222108234', '8958673889705949159', '6369330086410190615', '5957913828385649181', '5435557757895871945', '4639565458769324004', '5785932884940212886', '9081645972946213311', '7650892645374427793', '5209823851140033458', '6376343721993030780', '6882074241033486164', '8508959757403902035', '8521988530178194280', '7473884676694961129', '7923858866786761874', '5383913004303935162', '5892064210267994756', '5078220335056375043', '6636773120459200131', '8092039199193866649', '8486231504544197967', '6219335028816681372', '7857280643314172854', '8768324077356137875', '7387826620285990576', '7384689272662000208', '7749669764788851870', '7773592692867237666', '6644079274513083390', '5726327487738231568', '4659392411820958099', '7720521932498787113', '8143101757052186883', '9161681844291235879', '5779126857103121241', '5835084041925301784', '7103513453763546143', '6663327287499284563', '5064154527017179640', '8045519862639754155', '8839166996039031895', '8985938850782358344', '8781938823888009228', '6299642825467641012', '7582351635402059272', '7079778067837468842', '6322939747960010003', '8944956255281229254', '8009481754631845713', '5982981992845727649', '5302796099051282836']
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
            



