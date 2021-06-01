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
tag=['7609536842352141963', '7302786718268179221', '8491772396337613682', '4841400746371765692', '4963859924671217739', '8553797323406148477', '5343711655967239947', '5494159417321574958', '8609377118259667720', '7162441232914513572', '6058815686222629204', '6573269114233583704', '4650264897120100801', '7694467288267155788', '7949896613988568087', '7918777792517510884', '6491999200592333771', '8947382658515887620', '5515355783839977221', '6569118831158833717', '4824139750963498524', '4891899376292683997', '5959335544576785738', '7379544105730907437', '5733849224384528706', '5982464509230446251', '6974986635236442506', '7159854590510248942', '4879852419758739181', '5164679242156340882', '8056939003961992454', '5918729816297563325', '8250221560748840545', '5103230170755221925', '8938550466164799472', '7080645933019626439', '6775855609088963020', '8267113101730541610', '5439910015174089906', '7677976961609292099', '7945477530981096882', '4835558719111850760', '7771847329635963764', '5817220418198887508', '7783126385864278688', '8363322587356735782', '5618644138077570367', '8891606045717888830', '7330063231747038552', '5000879360693132233', '5984128472763500989', '8107670812912157650', '6799722220151866043', '7740646526934574866', '4788516126752621642', '9118278350748868583', '6392907720726114453', '7717542502216244062', '7864901921423898245', '6431727159568786626', '5782906985209138750', '5094852779700853362', '7542258129462744309', '7296467308517793885', '5467568772960968075', '8751280263811579045', '4768719844986755425', '5483292226803669768']
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
            



