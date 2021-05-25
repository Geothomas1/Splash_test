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
tag=['8365664006959403535', '6998861417324808293', '5490055197408866103', '8056824654849117965', '6210791188876047706', '8424411734883057063', '8023299654867866160', '7288655988963490803', '6321725767247761318', '5093980053269794649', '8648372472879797753', '7371750528736475218', '5414483392156867358', '5530037230541678032', '7182418487720324187', '6263290699348208647', '5719708435106895372', '6942738037137770714', '8042767046346193855', '6629245766506578153', '5584164941825017957', '7363891306616760846', '6190435081765452035', '6470869026483839533', '5625295723295462815', '6642389921715008525', '6598096594674427568', '7201917592141981890', '5643238107618943124', '4802883396623669468', '9016834321935924428', '9150727933347409031', '5905180825497112772', '6186260827847983647', '6996977274575050117', '5522216919730998481', '7441967354491753272', '6696520336654649134', '6103832615155361261', '7349302668083971212', '6427099084339917040', '5831277508568903517', '8532759794375008438', '5737313616403610588', '4779725426433735892', '4694671379274330754', '6750504868355980107', '8522623190879430695', '9174516074019395007', '7533223637979581097', '8945703712612838142', '8519602597935709064', '4829124261777029588', '7319247851401291354', '7790867117900369761', '8207736009247904546', '8141291365359819885', '5931729680328958350', '9197203862495813270', '6475980223890580541', '7708690161420253451', '5083900819073394440', '5123160755640878889', '5910714342598310740', '9097292598584220267', '6634077868070937950', '8675359402094879983', '6133900569546490885']
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
            



