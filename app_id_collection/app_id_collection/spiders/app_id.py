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
tag=['5348216302908550036', '7813047737432418418', '7511248943331051503', '5882715484911510337', '7452464398660132826', '5147050611197083185', '7205232592286531669', '5046811202250893219', '5379650403169417845', '8238136847941378727', '6422366922903869369', '5516190540716864597', '7115681139862408260', '5123694568480209700', '8561459617463593657', '7765504091534475813', '7928538706812079681', '5002028582015207797', '7642041077844492462', '7895390459353611588', '4985860497005230036', '8455994377550400554', '5858569602843678425', '7983474384394804723', '6523922411169419627', '7748385630698133308', '7139409056857096525', '8273200614269474165', '7619179554962382546', '6884297510646397212', '5990393928385096404', '7395377430775961717', '8850726458951723884', '5501717181097922072', '7678296481008878035', '5484138080495413960', '6290347233024089616', '8784608602437157148', '9192146316794317265', '8652106433906391829', '4928784632635954796', '9046354352885848467', '7859424541745883752', '4691550566754224401', '7912884720699783932', '4879175203187317224', '5719763700257089442', '8067532454246708631', '7197365081454168259', '5891704005291122254', '5528823404666678666', '8367614760114088823', '8394005212541785198', '6392770866476508109', '4905714803526247923', '8085561383966718534', '7856203804146823548', '9155367848378055236', '5422322963921095010', '9009573348036334344', '6180933336491609839', '9214145668810348659', '8969484046335453277', '7489105120650111643', '5344969260769243344', '7910987878760794105', '5353634690627881425', '5592628091795672680']
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
            



