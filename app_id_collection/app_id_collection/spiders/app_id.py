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
tag=['7364063264686244092', '6373483886976136504', '7820848285417067542', '7895405907334548472', '6095481310509571043', '6486606146580108393', '4670493263401464225', '5136921095482064480', '5408490176522893987', '8240129486068019200', '5394589464617666288', '4963534211284337565', '8868026909409570591', '6198718448307649938', '5719283186856480461', '7712822686355399583', '8196463383228867342', '6484606348020566355', '8549982525175224794', '6095891294324453183', '4840392963709529846', '6512945126708192062', '8046011114380843949', '7127160967849610936', '7917406766895882092', '5131935316667995009', '5018482428897077144', '7243535053449677846', '5185503876597016632', '9116908195572202762', '6508799610932709086', '5193406758168835540', '6726523214242250532', '4977601967915289923', '8489126217752744192', '6534297510193326067', '5167158288486269925', '7416022132232123311', '5234126047545735344', '4938569982851083276', '6328328251168545804', '4652636824579422565', '7455074266209943232', '8634108302579275179', '7256394520844402385', '5930365396324924587', '8234803880983384369', '5070356455691124088', '4878365092369165417', '4647829689618135759', '7984230714628987712', '7677156771759165691', '7006448213390739780', '6917460053443694729', '9192493280801413487', '7558003440350962093', '9082544673727889961', '4678881964570346633', '7618184701161402841', '7306432898834554483', '8683545855643814241', '5292443799849405732', '7394476988339982527', '7110275902107076400', '6542825718125289015', '6699818065335710572', '7873155639823959966', '5317681582000902393']
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
            



