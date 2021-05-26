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
tag=['6848893265173703392', '6156543945068839912', '6400697913003120319', '9026276733942411249', '6759091990972460087', '4879752542548385390', '7275672297469926236', '8504673628058540735', '5827870719129805040', '8863209968855584140', '9047984037627553059', '9084777547076204183', '5245434995562023944', '6940955801520592875', '8233080612482598419', '8931939761497249126', '7681643331316616628', '7912152304992264255', '7481894709243185341', '5834347666569055160', '6356611387299221609', '5388039698156406932', '4756612065940363983', '8350339668472203565', '8874656645233496696', '6586831311911659865', '5743956338204048830', '4807512999034360059', '8075268109882442064', '8269151046386258190', '7030493736864800610', '5698089116578374758', '5986559782227990564', '8552749662222181364', '5494901571419021034', '6121270418405995714', '6123809417984357973', '4630370587267892254', '8188968846352525287', '6637255510876518673', '9217064211095758510', '7848729999860293210', '8815613630531993292', '7120375397619006967', '5250474570745402965', '6318147985191255034', '4688550400526906779', '5075531480319489843', '6480583540251940511', '6896520975268523863', '8320704299942923058', '8223164395468033996', '9034671424644810922', '7748988082425487385', '8003740429242089634', '5249324404845433077', '7399185471421849469', '5850379710128600985', '8578733961037734770', '6676385477632245816', '6226647200439090866', '8221211288446637005', '4950941990992214322', '4652542788213151758']
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
            



