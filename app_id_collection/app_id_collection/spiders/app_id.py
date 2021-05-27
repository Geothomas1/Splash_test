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
tag=['8016189493316319102', '5873528659541833928', '8467344007713336064', '5009983141847453486', '7666590837372717259', '8490742354909589961', '8596493465287119793', '5589474985638515998', '9215497286952289402', '5848234473971998012', '7421718580720492739', '6203448337154291323', '5371665786520468302', '8784349674269511568', '4949759416091622001', '7477304117395410284', '8725056520371898667', '9031991684184028671', '5004686940863976016', '9027257451638050761', '4630046838693272688', '8026318893078307000', '7119588719986818385', '6986245886974779966', '7633829966830692806', '4841819270387302022', '8557298974280743285', '6704131689389898283', '6157630834917126553', '8707991648356128860', '7103668823328731354', '8572904136878930394', '7703493084570566552', '7650012590234453837', '8869836383249786903', '4717034007793529190', '5967739750628620793', '4901015553877356102', '7142105676058670855', '6793328204317855704', '7314924942221165496', '8352484698901451873', '5402566388565550579', '5462843777539313894', '6235322422675497571', '8929842424781370205', '6543179715746061433', '9047826085768471573', '6379252920287475757', '8505544222162700729', '7365925310766481407', '8764676644107844297', '5145254054310886999', '6448654209571781083', '7654989392690005002', '9138610910702675308', '6106683871818249343', '8721464164015383953', '4707470156482138305', '6835599094614424927', '8109845618040194690', '4981622187260885864', '6524369079285005492', '5030559208193479843', '6423350946249867028', '4773341033391855203', '7657777333274999167', '6139452084909553869', '6499807825067689582', '8124563735771622256', '4848088868271911179', '8674490723948838520', '5871523021041578969', '9221555372496620789', '7554521997597875198', '5912150201235927240']
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
            



