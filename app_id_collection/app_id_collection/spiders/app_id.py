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
tag=['5230555995159312165', '6619335707436468198', '8294170606515707082', '7165150874885979471', '7129658814762834540', '8524896620819774264', '6580385484683037314', '8664591411347391112', '5806996355701892771', '8125412195957092699', '9030305074573031837', '8925766064661638136', '7717252826449969254', '6647075354782608592', '7859780945987939075', '8554636772863887328', '6381455972553483049', '8569056545470208249', '7613559726597399807', '4783185603315957397', '8440581117075093772', '7513118655865938510', '7122604072877223215', '7876522563716244981', '7437694615834971867', '7912149007948852779', '5759207805545009932', '8955909425625383736', '8870617501355569440', '6271148884728074198', '7368103044908769748', '6920199206777027274', '7734029986344557426', '6741845499797812416', '6398934981827248062', '4889936945308022212', '8883698560555142658', '6660005827771885056', '8042858381945372426', '6472775598144550299', '8546711543889260201', '7097966885290590429', '8498002775679095105', '7487189244731520147', '9015193849853881919', '5053677748782380597', '7566478175607714459', '4785011288290302497', '4912388653378657139', '7355952837810302762', '6124789167329458971', '5047689587100535734', '5318941343551218407', '6530486727198366951', '5811378715434152929', '6820342375462956114', '8624815982969246491', '8793432965160368639', '7693907247237794237', '8370737193006374408', '5509942031792927328', '7727916601136038709', '5786444869601776732', '6031626461207168329']
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
            



