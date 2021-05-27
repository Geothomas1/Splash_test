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
tag=['7527059279485714785', '5023382999804961994', '9035572663537159933', '7486519919626675502', '6318849245691316071', '8619816316947116208', '6043810612129469630', '4761756773759466657', '7418969410851110902', '7760391990436708102', '6954060600211221926', '4635798689239586963', '7542342314085805619', '8650827185006920783', '5143147366520294834', '8477160791238144829', '8585617622618807198', '7135386887923450821', '5520866875929643279', '7826509718335370748', '8982697840361306810', '6436809088582555978', '7770323565514395732', '8713018207726107849', '6456103458130943425', '6505144360337972499', '8700505533045926964', '5699591569207915760', '8011527337429819776', '6576508125262652221', '6605831940140622570', '5035150003288626185', '6994732560799780573', '5751483060686246634', '7960571561427835610', '9110061396483086039', '5830807639601943917', '8706109602802412135', '7969548815811862240', '6773780251750155124', '7107991547261029710', '7767237820613678666', '8805736551862315171', '7745357870224935253', '7894416514660798484', '7959698253158571258', '5072699254547589727', '5830813308162880666', '6499886470572973558', '5868985085711282464', '6152735036123460290', '8870970682678030927', '6548272634128943546', '6644421747307260174', '7679340883931496934', '9062145765077344490', '8399276706772532499', '4946987770468052999', '7845338307989970045', '6390095030355507969', '5357617968382561556', '7393283248330705261', '7308402474883021447', '6505027874454618606', '5636916668699199802', '6428268730053234821', '9195370710669702857', '8383029841253340105', '6069251730530075954', '5477613425512997339', '5273394471208764532', '6577902653429990807']
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
            



