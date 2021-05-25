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
tag=['8819698729952752261', '8170592391755333851', '8931371852227611263', '5908427291778944768', '8553703844245439198', '7426391152695288142', '8111076891443836168', '5345782422249673276', '8357445997779888585', '7105764108626397066', '6551866306403173248', '7914063472596114629', '9122699904042586564', '5570745193388549122', '5001380540690243958', '8738231386379978787', '6680815792816251109', '4835812373081117603', '6824520278796265231', '5590326984553207482', '7462972767592454430', '4864673505117639552', '5012316661417012188', '8438468457954317322', '6734953287718913092', '5273672954439712672', '5413394872521115232', '5889854114365514439', '8937894086475433843', '8788845929644796629', '7781541777053893917', '9074768710666445198', '7948965038515587915', '5866673080816580792', '9061522327064910082', '4938690751404269613', '7872918715478512763', '7767429199421570283', '4644318306368816297', '7908791309174169288']
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
            



