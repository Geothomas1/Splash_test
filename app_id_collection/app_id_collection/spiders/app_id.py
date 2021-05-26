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
tag=['6324331771210995731', '8488028955197610822', '8634534336203114021', '9138277502707326933', '7495482576108205533', '5943102410143165456', '8404024925803725317', '6536810170831414067', '8285857627826256752', '5941988213471024486', '8399952291441459619', '9162265237404797383', '9040798300270550820', '4806548082676503798', '5015529879106087687', '6118221238661130963', '9135627884013724161', '6276812955865367792', '5448714512505346152', '8024937380713779869', '6938192309608563274', '4664062132977048345', '8901239924520659583', '4857785061614102522', '8533367514727698541', '5038114540649591984', '5734629456188755485', '4696251799620081526', '9219179332656617922', '6732255963723365752', '7857914999501017740', '8430308080610971422', '7828546591157000619', '9197622661570657736', '8128785271004936333', '4697621986045042424', '6032809542751503534', '6159164350662105107', '5660540598004646423', '8377945128991900805', '7473133955449750675', '8054113930407542091', '5229706829140512599', '6379443585294642194', '5019535404433459218', '8264278221503661667', '5781711887749363486', '7562197840432606874', '8125367806341362231', '4981047048485379006', '5010991296348314716', '7929500381656106742', '8295305621930182229', '8112583962804012005', '6273094339220990778', '5861778531754165749', '6017379033834134722', '5132295279651304016', '6917041651603732660', '5652925689338288029', '8065963838441938591', '5113340212256272297', '5602142920564923111', '7938158485537087527', '5164593797865173287', '8786921793888465476', '8402519815506918470', '5662752730693290222', '6337229670035066771', '5831113001306206967', '7178763725457724012', '8248594363885617582']
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
            



