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
tag=['6287989650956749126', '5282094363839833539', '8427278889971809996', '4968465157494545986', '6652266705779304080', '7520828103313655553', '9028092319028521457', '5143088460222708867', '8414441784957489448', '6793049041585184273', '8008719444491355149', '5655198026020607487', '8214038667755736960', '6169253860870779343', '5111526795743073171', '5923741154386769289', '6076456794302024549', '7389331043997530214', '7585541022225224643', '6233324316594141971', '8882008923225214033', '7294266137910511020', '5134340805090796317', '6365071554875589319', '6278000792128258202', '5742052531448409195', '6380065003756340522', '5131935445241450245', '7663973636960361438', '6166245662185922810', '5840044159746169146', '8546151336155604880', '5948247146774803388', '8185315102667235537', '5819541650108536561', '6926424078935767102', '5160414446713205206', '5526133326405128590', '7204098107805591836', '5333145588379939701', '7416036497005831052', '5224172264819052762', '7769966689762626963', '6542263599860318744', '7019361452902095273', '5835572268783650988', '6870865343336881806', '6612894131620091772', '6966877216731402571', '8094173051960257762', '7369362400968269926', '4641490051547700602', '5723283153570631532', '8622619535130521980', '8109996135600213546', '8692689253912447957', '4727247219803333337', '7275382569983408024', '6167711248071037875', '4634636544786464580', '5799633190621161004', '8249079113789922200', '7113315725522468999', '6816731396482012756', '7406148856139778891', '6833715359242728598', '7196429347464820986', '8578506654148026989', '5503516145303845908', '7946804664644508836', '7810022576086546438', '8639322789478556181', '4638068222939387522', '8414105821730633575', '6119407705787493511', '8260243700325913255']
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
            



