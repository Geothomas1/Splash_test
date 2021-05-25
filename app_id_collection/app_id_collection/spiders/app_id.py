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
tag=['8337337556188554422', '5727281918668770233', '8778145293316571713', '6955865141313516850', '8210063275497266236', '9003873124033768561', '5932602861668461165', '7953926523629818193', '8851495890098155904', '6863660225783655708', '5176389557995011208', '5470352506825221475', '9038214858828077471', '7329727274311663970', '6803189851043526392', '7318610436081902813', '7989763632565953614', '7196853208127263298', '7823459848851024030', '8550239394877360493', '5231417212653215524', '7710270795402105867', '4857052337317959122', '5159412086616954784', '8736246333130398172', '8132928251142915312', '7226891587109343907', '7410263471330413031', '6141971975698439159', '6899235863428512122', '6804371481370659921', '8269125425847863562', '8973280186746174189', '6383541376549322486', '9018002417865699301', '5225335583529426505', '8267006738147263003', '6786784248394984990', '8885581409676521728', '4951786929648200993', '9051340790851293188', '8487124793505681886', '6471043160303537545', '8284715209700573166', '6516502689225935098', '4647655354866404261', '5283325226687181635', '8870354335175025739', '6055619949021145439', '7424551952730750278', '7468623163831023932', '5549684002229539060', '9160472029556114620', '6280318120627708333', '6028037470394175266', '4934808085538804926', '5931123157174072533', '4841503036897376368', '6155939441094596991', '7407271375720328978', '7257484776235236912', '8544093505266146501', '5975368266950989264', '4662269381945447072']
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
            



