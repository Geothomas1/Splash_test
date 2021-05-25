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
tag=['6362617821084569080', '8543808028447094717', '5886046441896040260', '6746921252859588150', '9104457198089339529', '5895427308507981734', '4619663695857345939', '6544793107738140215', '8125340861419401744', '6562182879268239235', '4699526921952220594', '8729296885103116944', '5401107896513099601', '7171777474719574358', '7006181994130331856', '6538043644209226140', '4739332266027224934', '8784691922048246110', '9107966839519389532', '8965203798529801347', '8698102133499397929', '6495582515087357435', '5415425812860184091', '5315681843979939146', '7010004677922348564', '7517758073840264816', '6533976066106630984', '9084292884241052196', '6705353803662462298', '5440225474779024023', '6440927141362018205', '6430085252470210957', '5406670944475532752', '7192299817302644188', '7848524104751212251', '4869538617835261220', '5771977041877680517', '5031127982315510998', '8249955520207425408', '5308788559017803046', '6484103794139944787', '9134020005744179184', '6785444890720651855', '7783311984787710212', '7713639241422011143', '5031158841064325556', '8303291564330244190', '6831000268101361315', '5947436689534002511', '6295989021709804783', '5038547449227636061', '6980118829813518682', '8752121257243689563', '7347222123606137392', '8154550354216445583', '4894015863822067629', '5383121816437054335', '7837599681692970357', '6029623849524031372', '6953200378576217823', '4726011372132294837', '9034971394194265195', '8652601183300845527', '8094511342623808581', '7858247503133323610', '5867764354378005830', '5963443096922659076', '5952772010143192291']
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
            



