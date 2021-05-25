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
tag=['7659489793755917149', '5155774373845672462', '7224688450800416548', '8622914620410896420', '8655515295282779739', '8275018044931724073', '5104977666646671293', '4986770375272643739', '8690835042818503652', '7854661013681508387', '8295492311057900546', '8786055212883898968', '7744025270063480045', '5685151858125894494', '7530601575643168273', '7105367870106447069', '5481991796290772150', '6224821759910637523', '8120074582605905323', '6176055387072068495', '5135147781959969551', '6333691093902638034', '8068619710140831344', '8177557037262186540', '6808882026542751289', '5347487463366650352', '4980695148773520284', '8161716128506609478', '6587721047803245737', '8484035634811244989', '4669677832631139207', '8514376024252400540', '5988057339172766630', '7167555626006380306', '8917488907474993387', '8136935935686387300', '8357286521422088545', '8170068135464600560', '8660304129214504169', '7755379730625062881', '6535913542227910548', '8233337230952400208', '8807757752657588254', '8193574052088468807', '5782282508966246810', '7273510839974748636', '7947222944311463985', '6188473045484218244', '6957842755751332836', '6822706159945971024', '5765907833035779387', '9171079976768419078']
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
            



