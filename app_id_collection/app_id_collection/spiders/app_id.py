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
tag=['9120469403975107329', '8016566420192178805', '8074006773415820131', '6027623839818468958', '8195332930891542149', '4877289508094635033', '5550952230747720704', '6143935442918635295', '8037379431786682703', '8157574795722632732', '6000773344675202498', '7151232942159481018', '7250509164576869654', '5197527487940398717', '5121190530275013369', '8702197959022172025', '4866781126364652072', '9067900440196140337', '7632238382729581414', '8002703324518409296', '7396530117240735296', '5856390214538204141', '4717519886080823170', '8517959265305990625', '8512667409063377145', '8122263305727184882', '8813614102725674011', '8807737763173991980', '8720530477826084277', '6158383236882421120', '9127789311115686994', '6549921409980981613', '8255872018809360488', '8651519030896121427', '7487577962265079318', '6247118862873290254', '6605125519975771237', '9087509962033752464', '5255025567337855923', '7052399597269318681', '4724771764306559450', '9190650635741968936', '8874025902646436777', '7268010411837962168', '7468463311589977937', '7801314150799336819', '6090445212879885918', '7934661478765762665', '8576336221984462126', '8708492391675371964', '6898190794971933883', '6707416029016192240', '8782595456902732805', '8385803056643019941', '8561591584225474813', '6357029444281946957']
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
            



