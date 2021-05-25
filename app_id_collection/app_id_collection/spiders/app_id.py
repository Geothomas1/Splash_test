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
tag=['5292655742535538100', '8821283674927730745', '6504027944347832056', '8295654346829730257', '8922165429020565740', '7817355175054794518', '4975552040647080689', '5777289292019877915', '6033331672770915236', '7781629231947269034', '8059182133280644587', '4863789631992005995', '9118636446845177720', '4690058052047957258', '7956451155677777542', '5242637664196553916', '7347259763539427346', '8177774334723216869', '7694058680077753790', '5656745006364476535', '6286470130829059169', '6577981237362163650', '8982669678303208146', '6173727838862467184', '6525856186127864437', '6259831402052261779', '7918683813975555822', '5848068795804361091', '7740096317704304177', '7771348814703258289', '6972312360891598931', '7807965221608171298', '7418002299881635538', '6647680965769163905', '8778010793199987545', '6629526768126031132', '8532907581042995001', '8940674763789826981', '6822438534853511255', '5082369244243268639', '7464058839089985834', '6805884969373448765', '4717006573762881800', '8638120915920097780', '6857643651845790053', '5195759440434026200', '6365145997021948499', '9133452689932095671', '5374976432969357837', '6413148044699721166', '8599293521285797759', '8955965820616231140', '7401895045766760359', '4872147383896877371', '6101010425660199296', '8747420266509441425', '7638841618488639337', '9170985961245337722', '4802403663604899862', '7085461508651340810']
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
            



