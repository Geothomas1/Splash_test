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
tag=['5481660728107568382', '4934461663770967629', '4688057536495655918', '5561916917816890433', '5158157402406404947', '8332467841235656878', '8161093088993848231', '7413431291863238399', '8667041810904407203', '5559012024609166266', '7966448614999270715', '8933575792593715746', '4803573247340653455', '8912554627117291225', '8923936729792931426', '6286189558550875554', '8064602493591051077', '9021376764549445418', '5219852638151001975', '8537184244572958038', '7834691532460600952', '5393919272634285850', '6990178528646658622', '4670767478957130662', '5488771027629832739', '5416852662364204136', '4734916851270416020', '6096060713339252212', '7436560986914370588', '7065409552873165205', '5262675996400936788', '6020126473663388527', '7922993290302497917', '9191329759658538243', '6418760394979464117', '7819119204962676474', '7278635385981253175', '5726034089055626621', '4677036829894589804', '6647328283761745360']
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
            



