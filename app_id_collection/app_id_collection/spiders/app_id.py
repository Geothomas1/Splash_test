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
tag=['5892896420997180613', '7465179486998625255', '7422847694123577424', '8608361469800700014', '5101937198185715525', '7579213553035722287', '7487269574841753053', '7774746132611575805', '5445025509717706143', '6141013919453837613', '5306964836620635204', '6007625242696910158', '5265365392581993410', '8847475748098199636', '5707607841384614715', '7552372087577284767', '9168645875493882147', '7380699866334433450', '7637751473451953752', '6391774274796490404', '8913007979819179435', '7106272011724404665', '5594977991986922040', '8534359187310564223', '7427650426441583591', '9200292883393016799', '7832176051276305708', '6382673845901852664', '4824095201141744076', '6220737717348556353', '5566219960135977722', '5901522547043104221', '5548270739440488900', '6030117397513680821', '6503718411004832775', '6824393389065942833', '5926338925519592621', '5997686785003835939', '9171390020439420041', '8540106303476092115']
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
            



