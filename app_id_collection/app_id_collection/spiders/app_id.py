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
tag=['7180184502971888604', '6975763160176704161', '7009248018867218186', '7567212602874714418', '7810857680233826076', '7216392468253607429', '8785867991744716297', '7384554197180828570', '6406918880690616144', '5555916792883820395', '5443907856021144404', '5076330424665753989', '5346896192292603347', '7745656402668296184', '6269029342367412672', '6384053065552886184', '6389038453295942922', '7663189367964301383', '7265711973702410668', '6910954530998328402', '7891609072815332494', '8735414345444155686', '8881930935724814925', '4936625435116775740', '8921992343140454441', '7683034597171359137', '6751664021832545665', '6695766987207978866', '6026546822694851459', '7534109763624880979', '8871043260388010103', '7832395566066266868', '8333489392772201906', '7085989330631788917', '7573307997444323590', '6250558401774233464', '9035158383989300558', '7998005388235012553', '7169816280300048197', '8070557571433482310', '5920255640535275166', '5643002524814109641', '7950962269261926962', '6246807266900348469', '8943681028918653951', '5187199716534357538', '6949215177312836097', '6760966441031982052', '6148929476111902984', '5983333012840090651', '5932571367834346696', '8741497845456604192', '6073317223409631728', '8036164855949756457', '6837645930350091615', '8891013208268781571', '5368392061477618737', '7640888751680930159', '5205531252117160335', '7070333635458576510', '5985505151266094438', '7557161041199736267', '4965354035571938754', '8387352846622472237', '5566853724814263823', '4902612493893791040', '6333870207154764877', '6840968501317174301']
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
            



