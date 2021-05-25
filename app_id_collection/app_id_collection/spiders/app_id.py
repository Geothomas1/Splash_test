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
tag=['8163851848922388381', '8257635495232527443', '6711610060034049850', '8083596337274622751', '5743215888875974969', '4984535831996331593', '6934062097569451033', '6358682913150476330', '7155882323176002352', '8100518220672290662', '9053656078106634175', '4779969128663469113', '6324425771244810643', '8886379821451450467', '9170275381782328383', '6217164817604877059', '5434304384901984469', '6949148031700053043', '6345473621345043765', '6274905843242884991', '7512418058857457125', '9221909225717116528', '6177492284961668428', '7266924558817293669', '6460569587932776943', '5851691295960377442', '9097044332653942940', '5587345788514684720', '5438434099680543384', '5029755957860459217', '8131449190375088041', '5846405876444943676', '7717518037355690562', '7674514660084826148', '6329278726122414123', '7695251576183226202', '7355551958512480791', '7891340555832391669', '7921818738411209811', '8140957805212266854', '8578938245819220579', '6595598812883017402', '5536898725395678245', '8117018149082863872', '7081334685631154257', '6472399032955398374', '7089073611228142958', '8648499208878745563', '5549089201406279015', '7091818582475860057', '5929655295377588931', '8272430734294874754', '7734088243367361787', '8368894388445647121', '7938476559309985542', '6426861091105194128', '7179215531664766346', '6306992671876492375', '7795666880575168001', '8020772626664092379']
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
            



