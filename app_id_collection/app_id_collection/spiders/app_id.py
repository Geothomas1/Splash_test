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
tag=['5724083469015956681', '7411142827109422638', '7604270667374004724', '7005590155524199072', '5027283747998054293', '6854854993980629622', '8282881121169577203', '7363782766112928385', '6831318754582254644', '6346502411066495624', '7721540908257733634', '9114729002951785341', '6971196307096028927', '6854351010387078197', '8661646059741070914', '4793235223478262915', '5070507835911167457', '6766716560811922992', '7073033229549322235', '9105501219743574162', '5034946907336193520', '8255351570022502533', '7072004424196986348', '7402948443883748492', '7828778929395862624', '8004015939227290547', '7796469259261506228', '5628406346950598965', '7523915100976301397', '7639671321761547240', '5224808347113105639', '7005215065502044041', '5619049600499747493', '8609038393479580902', '9035882766975912845', '6192891547337946730', '7181014046147655336', '8357929066656890996', '8389801411700660407', '8904496665597228919', '6436751786847581046', '7445857388176857361', '6513514954662648970', '8524147456809301772', '8062024059993989938', '6638875339340134054', '6742020338480528791', '8173090495744578265', '8964723379402809738', '5238301390163152853', '6993780207527157787', '7372403061489341194', '7121821132566538392', '7633149539259360982', '6783138382795365023', '7328836074120817235', '5448809053461726067', '5062298237373103345', '6687545649807914423', '8487041794552403356', '7411433083841951061', '4996955248857079922', '8038749736533940412', '4932124767453059203', '7506805245578402716', '7276832647889288104', '6648558942107861407', '5508707564295299555']
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
            



