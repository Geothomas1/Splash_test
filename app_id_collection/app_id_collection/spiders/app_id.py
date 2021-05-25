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
tag=['7800945074639440578', '5190427103844106751', '6203532942826707507', '5020932365670236819', '8280371868725909409', '8554081949679923539', '5071876487657488196', '4783948977623708984', '7475298195312778379', '9085472811236726299', '5457155986580660672', '6219579150092467395', '6652861547022882054', '5227068086456315351', '5203534154219374337', '8984131460684276994', '9189134633805139989', '6510137047328371577', '7395099115865012859', '7095867981533202223', '7063234745876235039', '5944144541282617308', '6742152580575346228', '5102606917271146186', '5914992223521470781', '5372647758390752430', '8557632385790481879', '6194801620120588665', '7006432247581644805', '8282660901557671207', '7959827333639121177', '5190690563852840907', '8448912684712185254', '9112956004356669898', '7444977450336434480', '8538048374813401161', '7062100776890118456', '6873051155728780305', '8108048346499082508', '6720610253101941373', '9037956798331018413', '8482453602994588970', '7279118603966350839', '6468306883306566514', '8134839563302056654', '5310890317203895130', '9215614892284160358', '7153760238279218208', '5959456209013630545', '7801398981398508590', '6922134329021307556', '4922225441490152702', '6204377995854093135', '8387748078040436291', '7844107938224344519', '7351694609101343444', '6523448015067312287', '8351641259293984004', '5376051293808044335', '7915801618351606475', '6337138886679456159', '8347698199543632849', '8653465422542351323', '5014570736864732990']
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
            



