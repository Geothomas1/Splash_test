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
tag=['7869741626574386509', '6991603797333969024', '5930437092697579145', '8342237356707988495', '5728529501729088241', '6271329037569022061', '5483530693238951176', '5025020445326631009', '5439029666960327955', '8535547745196843885', '5142626413956897400', '8212118121724309640', '8977642676848453827', '4789258906418344419', '5690825265218088610', '8132143429253916563', '6313598302785117151', '7143718602581957594', '5717891115569887983', '6396054006205873142', '5574603867036537774', '6911426451855478618', '6440209878071865926', '6417697764174067965', '8486042261033749428', '6538597265728639020', '6587650089412189455', '5394256898986964167', '5372808507629328548', '7377724616707475454', '6692707427001655430', '8467937417565426110', '7515761085860334575', '4923511704223195335', '7611044097093739088', '8325657000152317866', '8307876062402593836', '7690988119815101160', '6134471949065301430', '5570870773959718228', '5574377251742556407', '5268755458235428172', '6764088955104110890', '8309173529935773267', '7300110278256090297', '8116545300283226411', '6486757945822149835', '8314312934915346876', '4830493610892831176', '8149422968449365069', '5560690671160482007', '7986703481092486661', '6859173202566452199', '7088818990071872417', '8019159852907195500', '7563356113759790067', '7754474998603501355', '8876235997624091258', '6058820582570442962', '7063461788114274538', '5008101826173560204', '4622967442740406548', '7667991169764585208', '7239458142886872266']
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
            



