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
tag=['5999462668857862433', '6928645284725890918', '6409458411588093871', '4619546616055940886', '5904289130448622661', '5504511874958019671', '6024491415438976790', '5840664117349588017', '6082914357148822158', '7813828567635998204', '5531890990757525715', '7133415022327536166', '7887578732830936341', '8755302017763705461', '7018855671706435741', '6481514194041377964', '8343798540401422884', '7623755293427854224', '6837485048565497417', '5105948817497204165', '5065527547021967317', '5333493718279495843', '4853239506290481783', '5641203057156022873', '8111995201222586416', '8505992995379302722', '8866873010000587086', '8858269426735939834', '5045112000063547575', '6459265383846717035', '8677746436809616031', '9217718426385946861', '6438506733292909344', '9048260554139798969', '7755842874045936628', '7276248274029317959', '6793228252592022628', '6408385875609575522', '9014784185496290306', '7598296379323058380', '6276436986239046894', '6673881500075984658', '8707574407906011349', '7957227631041524913', '8114299427772938571', '8194392026252557243', '5827152673441848804', '8294973879588281892', '6636993142755724057', '6016084287245959792', '7348046687366315762', '5413414367290720810', '6311212312818019812', '7729843282518254108', '9164084145204514437', '7489215687164051996', '7039580205924230579', '9190577525907500179', '8978066136188956247', '6221695193692857971', '8228673875116093897', '7864188483193335986', '8177374955670286530', '7265861182694220401', '5424898825801852569', '4880329950393363615', '9097596828204605984', '6139052208122157728', '5471705753437242874', '5213250127137112372', '6518287895124496054']
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
            



