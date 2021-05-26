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
tag=['4791943280953700862', '6180359497574843730', '7299719793474585382', '7872423500061383086', '6463095943407695116', '9210839603057259255', '8762313232916265908', '4679622475863932182', '5461979616382274584', '6365925325605726444', '5335380207889844502', '5195143392247825844', '8479277614783637562', '6503790277552793229', '5034607856969001957', '6972223028550455938', '8215765451816780816', '8759521420031957344', '8895068120284368537', '8651419644365663018', '4944786559036105012', '6409407918589376367', '5028545197936795641', '6823404764101374014', '7240594971851857167', '5144412845874302637', '5417031417503375017', '9130285497433890351', '8463943085310198153', '8107363323701912121', '6320605061465016847', '5673840569835357829', '9169751687364421253', '7945067399956378928', '4902729103455422060', '9079296760313242518', '8271704752057011334', '8107855987752203465', '5614074995304947897', '5253789853304707629', '4937479760315816791', '6258753308606912124', '7127191341521759575', '4941788960299936345', '7636915274338932123', '7107975034578576294', '7181203960062069413', '8262395985943172025', '6578979475565954381', '8358445640014017977', '7045166111016323804', '7315419339265800962', '8786226368526474301', '8544499919567402390', '8278886069431493261', '7116043841056967494', '7199729081776703730', '7270535662329442841', '5360036014478858866', '7495700166596495310']
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
            



