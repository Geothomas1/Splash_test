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
tag=['6255635862786425984', '9217428801085158876', '8405377917759873091', '8246690960940801203', '7708405474390121556', '9110322769455105767', '8513200865613590694', '7707480999727607860', '5523575197583774291', '6498536965846378753', '7154795790738196544', '8023803974010810442', '6644575663711048066', '5235653410895960460', '7356333912193102764', '7848399853315920998', '7812834815367511165', '5057058873634489942', '7743658010624204910', '7886930070136533294', '5920164835026311492', '5663956320122335892', '7886810717226049228', '8657371612651767730', '7013284109663721121', '6538492620524596530', '7066327292294031026', '6000306593059648959', '5286797363462718482', '5529128535050110345', '7746790260799059679', '6898574111631529686', '7848899517346361101', '7510749941565065003', '7305146816744789831', '7812667478711588455', '7503155286324226901', '5602309161373665584', '8837954227874223471', '7236184910506144613', '8997862640565675579', '6288836199883923544', '7029141165912445608', '8132058283668230805', '7656585193000916661', '9084551136977905022', '5416899564237708769', '8485484626033167988', '9009024646682542597', '4830557248359522317', '7037404579872786205', '6222721545060293820', '5999028863524402166', '5931516231111023825', '8024679619345223259', '8125057191550059802', '8646351380157088883', '8441642766048970424', '8246518504979807481', '4715860640289570877', '5541491807249823262', '4700124300863256057', '8542001137219996574', '5963455572546126893']
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
            



