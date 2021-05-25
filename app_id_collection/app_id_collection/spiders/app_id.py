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
tag=['8636887461635678274', '7378134043167029317', '7687779963074899640', '6290980413021092101', '4805113245648012987', '7800686333775448914', '7063975469457227374', '5621025497539624503', '8360602806689043703', '7677882823926380646', '8324908162933270279', '5229772353722826954', '5322135036200967337', '6317801739566373025', '5946030625351448282', '8859061204267791040', '7725263022031449394', '8599779085346220611', '7987044497930745454', '7734529632664450517', '5967784964220500393', '6524932578166139479', '8182386344093465788', '6563458776669518145', '6605044548854937364', '5090037829240044490', '5060643507394548139', '6872458491681715814', '6778854578813425410', '6994182275118801386', '6066461127815016896', '4799882127010016633', '6449785206413258640', '8095884964308210606', '5268566954092969789', '8736169189161159844', '8601716327451933581', '8705033538094064667', '5049031005174069301', '8074702445000066563', '7948217467540814816', '6336183702497624329', '8500203616990118686', '5030224269248244599', '5338802923502012111', '8124543308330191770', '7454903432730832921', '6406348189631843448', '8546433605744367437', '4630314805677320030', '8422572512770202743', '6452162815424133991', '7957384111093458044', '7138145245181956997', '5477122597749977048', '8054153443941756068', '6688852138083021995', '7486525086148363624', '7880880810919736603', '8301715584309447119', '6396616068091190208', '5144845415799920446', '6168661753325346402', '7595163964069402340']
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
            



