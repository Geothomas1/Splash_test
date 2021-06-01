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
tag=['4615510722268071447', '5019475767463580074', '5148323979592690385', '6100716301773757749', '6495077509052169077', '8758569943787630449', '6688413481338834264', '9092309358838059623', '6915901175784849855', '7128784511156905985', '5907964973028676738', '4828641744725948908', '6644296608047560938', '8835037414483186946', '8927403212710021390', '4737354144616321734', '7167505373655907425', '5302914065114406058', '5365609412493042281', '8300271212741347560', '8238521733535463625', '6102225140849554440', '9207342756817386180', '6499508588783439318', '5641955415441053465', '7651828250969574232', '8561605739265869547', '7242222815654765876', '7516120071269103166', '7420781587243635014', '9208857686559028718', '6841109092002777863', '5911864986551438817', '5404295872965661881', '6506939732544695649', '6049418254268436863', '6277407227159328360', '8943863732834633521', '7896158407610024525', '7530279228261817937', '8835488637255658371', '7350161687160448607', '7312183468996865232', '8530277740600734431', '5641696234999344861', '7585850630230964122', '7365007003806139495', '5871162806386329158', '6951890225478609563', '4819773001047527786', '8827829994088552831', '8340363567920379762', '5922835369854337147', '7206213022914115558', '5781213370243125315', '5055892917356573211', '8875815412055268474', '5666809025597224749', '8084058150308403862', '4926416816986360146', '8205473476028368924', '5611152835602166395', '6838870359065450699', '6547949513875314812', '8397875400461057969', '5219940065100189595', '7523249721225006885', '4698297710838788035', '6623889183459662932', '5220922888229276502', '6500771597344387049', '8435443450623193572', '5308205921199964069', '9080810217533172161', '6081018741390099347', '6687824338264384159']
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
            



