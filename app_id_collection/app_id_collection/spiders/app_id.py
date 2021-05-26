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
tag=['7303804976590471399', '5002650060821952731', '7756763157319228873', '8302490045814731011', '7225275863799365610', '7521791612608721759', '8841939610845306454', '7775114473013501019', '8566392148662536187', '8231564889276180067', '8529715749031145287', '5054359056020144251', '6959526238859339120', '7034129653720243427', '9031177233335426586', '6743351871693829033', '7667676158088987726', '6288229135815648324', '7848169987063658703', '7095241823954227725', '9029239508853672042', '7083306018778244312', '8036835697788369781', '7691759152524707707', '5320878310891737852', '7884016305306450409', '6637232144242323004', '8358116023073556533', '5292172105805129427', '6861906581664932040', '5432474436276944851', '5798520808794069858', '9208683183364654096', '5795310686363668217', '8730344021155223141', '8472459119037168027', '8755201370269345476', '5098404652381278867', '5082268215048187696', '8983953568983045767', '5480983591045220265', '7479761300133274679', '6122909108154532973', '6413929742348867656', '7987416923533646496', '7687136110608797526', '6773541816598877702', '5311396783099201809', '8281696871670304543', '6255378953981435017', '6520824775389723301', '7754016951728422895', '7777927871280338760', '6880713677722117746', '6950163093734214354', '6709980703426428139', '6914911790744547365', '6457525047837794623', '8235669704987837150', '6880473948813098012', '8170078085594259123', '4652195492405991290', '5611819854980639847', '6556010903217705537']
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
            



