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
tag=['4965239659520545261', '7043232623961710187', '6649631536199567215', '8764917260430183176', '5369004115736525914', '8888426228090824848', '8420080860664580239', '8742147433790603073', '5930459391842003590', '6422575920916366992', '7643587616668965342', '9125681457705584811', '6282714357770190362', '8831946150671257704', '7063287159436207953', '8395257673867455000', '7034492189502928509', '8638841144824740015', '7138406129688133706', '7059424641738398829', '8340986430788462719', '4977539946621148443', '4784006597731195749', '7691438629453514158', '5163955494107917703', '5688185120427149899', '4877435830839072907', '5517701664940657356', '8552325357593841502', '4860860223670197155', '7403548159315789908', '4912900723694136900', '6014721891270585927', '5778787446116242811', '6420724462927168095', '5313970562113086456', '7159802790466848065', '4907307349161033119', '6122917544880027084', '6888597105028391289', '5854026384585450911', '8490607248807111211', '6702831139482500152', '5003339544742675182', '4856252356182720678', '6374859445876861693', '8015975901504553999', '4749516082998468718', '8210788778811696574', '8307058967521007291', '8516103066164530742', '6206618813943963783', '5027991673439234321', '8566893378069450560', '4805133420821211993', '8715047180085105330', '7642303328052285220', '5504613122676415018', '7690891472206572177', '8319874825264574626', '6830150806644785534', '5096233774909251047', '8229370313174418397', '8994920712470406363', '6794592207929601831', '7793400040486951587', '9160386606313595079', '7511861032296977274', '7804891706408809655', '5641247571933368869', '5418486075279727727', '7233863592533675758', '7380668640045473908', '9049355176350674430', '6746876498477979213', '6361940396597260760']
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
            



