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
tag=['7778265063750336771', '6823602592155636380', '8401698069969689339', '8501974564633412077', '5480670470933861600', '9195250452587348770', '8685435842140546750', '8532792808174659513', '7442948277814970932', '9115671908259702233', '8904962268973788226', '7830818925344274888', '5442993565092729797', '5756372639482561977', '8660716254448862517', '4835339595039847141', '8050833375807594909', '7153203368724111677', '7395651071460535829', '5307355541905034578', '6933268402192668955', '6303061363735797538', '8910495488664322785', '6653168259955851278', '6928237143520558692', '8310049173073610816', '7415501992468135443', '8501754229891074327', '7808687186217671925', '6002704198630646537', '5283307072452267974', '9009299467586107971', '6764162556629491345', '7505042192863063313', '5560295183611633712', '8993195399885453984', '5665533263548117863', '4673451105999232933', '5156488372101316114', '7164639809130083491', '5946671071223929433', '8834977280211535695', '4884542432585728897', '5644263914745919271', '6604607189943717338', '4618184724816309039', '9151348737905172529', '6391453960516703034', '5199911840295314448', '6811549047576051930', '7007179553049859627', '6318580310668118933', '6326647579692608937', '5361740613259288180', '5512403648805629587', '4885702290713970198', '7215255014191725240', '9172773201065533927', '5062714391960334516', '5018743430406908961']
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
            



