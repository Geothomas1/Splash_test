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
tag=['5348963261007952058', '8689562767134265419', '6893351667866882124', '5425858462510307651', '8937803722012550943', '9164931821869442682', '7961697405815336147', '8094408836964062012', '7039474225328394984', '8755072298400564962', '5388715782034979460', '6935119863303609605', '9179035619222021154', '9011900625546389312', '7528537393826584694', '9218870525169505081', '6367016382542689978', '7594184611184681419', '7874214349379810765', '9196397586126736208', '6680614500117195970', '6199980706726160420', '5047721648125418497', '8066547858435152492', '5979242633604160560', '5192298363751699648', '8911018875837647146', '6446465459377141474', '7012467671434832283', '8194879539283181850', '6236128267733362757', '4730507445401680794', '4919265583026901892', '4758037713884285017', '6153025687283802874', '5640292770246134663', '5362355705811727981', '6790926766572360607', '7155401493577770345', '9114904218538707520', '6709076263762798192', '6405685974996326719', '7383512265243583111', '8439381091842483054', '5525532405228454583', '6430809027451137039', '8883663691018917237', '6983514835584838345', '7340652782675193720', '6980083735741436533', '8631384323439427849', '5947990617477965883']
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
            



