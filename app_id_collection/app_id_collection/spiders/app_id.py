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
tag=['5239336943174580259', '6144789182621834251', '8920403466755634839', '7044778343143443742', '4743004323104801107', '4824549668973034305', '6073118594627082918', '7478866976704782261', '7125744562568053772', '5418250238214188743', '5809494716020317771', '5265750018554996732', '7372306443521662895', '5091437083545417178', '8228880767701326722', '7291763925953378135', '6825657502194266459', '7626160520048658616', '7429759198330545772', '7383936910318543011', '7796673666177625561', '8573492615399615905', '6755111619083408553', '8247170330950867863', '8354414006963029559', '5853548182240433952', '4742556904591852009', '8432378763675405745', '4873706322039788689', '7689849532967671992', '4854965522532750318', '8962462742290828506', '6228977922961856240', '8825794184548352018', '7589953741036306030', '5301207466551661098', '6019948279059541287', '7471120406917554133', '8295600943599725943', '5887472250590920983', '6483093350535730373', '7553440236571719579', '5428337135095819260', '6608637595389219208', '9208906915923078420', '5785099984219112122', '5756965413036142971', '4909259358425357222', '6651481676089454066', '6252682850953876093', '6557923588427918218', '4927359589496482128', '7925454854089648018', '6926847469998858873', '9067936907063532546', '6005219833646900231', '9181617929022876701', '5370920623237131392', '6591300949222881369', '7700943178826772298']
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
            



