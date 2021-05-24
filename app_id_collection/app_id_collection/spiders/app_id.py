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
tag=['5493827619333849158', '5953899060857093739', '7616013801936750943', '4732508951530669034', '5674675083940565769', '4792627220499024267', '4662738378441941373', '5183235697422098559', '7250442151934849941', '6540162077545226218', '5780951275285977016', '9026918347550147003', '7074783673860142530', '5882151793474682578', '8344395899084344479', '8703316532995157489', '4699951760778727455', '7436689054200949090', '8412111974998572669', '5914789279947061054', '8527760436938251586', '8814668688577681059', '7927921140104315807', '5673594371298752777', '8081008290964226185', '5080272940774919759', '8016462318464244999', '9017397922998813113', '8852749347021141716', '8396698779701600828', '8609632911731289602', '6558893104981604121', '7837462927897324993', '5857156564939874535', '5054071932619131185', '4820464931528715396', '6811281457353247126', '6073070480358154440', '8322446308246797994', '9148775230606986868', '8628441344302043961', '5406469272404860036', '4990344183546452045', '4916116423987192588', '8120067906396157769', '8814170128014481600', '8991276905776159101', '4812813469777961743', '6975778903186969024', '8078808307616667252', '4917466754585552320', '5066657096754698003', '6775043045109571645', '8213431378781379108', '6734186728507929911', '8568542481935390704', '4825371204703370189', '5700313618786177705', '5032485548806526009', '5543390628344294744', '7029800880238044365', '6720847872553662727', '7220292605194330413', '6501672491544717993', '6437300643703400451', '7763572332649219375', '5035872748406210902', '5819342261711162750', '4753719216406213136', '5822547169936380282', '6759146811367238757', '4706337142975398211']
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
            



