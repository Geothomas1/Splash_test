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
tag=['6350059224995713537', '7119528464328901451', '6054404461506189972', '7548777239623810200', '7525503020396102481', '6551879310109921470', '5209129333566556263', '7322331845936781829', '8378617178875547862', '9193694762831495961', '8105772416207754950', '6102118479929529032', '7721833653776063386', '5597390656092670459', '6253361634769591938', '7136847125841671360', '7551647126691918468', '5005428177830444825', '8683312348831701211', '4675527057763401949', '7147157000803351991', '8577581364344393772', '7994391094920129798', '9222196074014812005', '8791547849227280675', '7311986728602984127', '4641862048407841490', '7803509568831157746', '8485015457203576837', '6406548926476763527', '5628399893543620440', '7908805917093292127', '7846218294077502112', '8507326308533346818', '6550604165603830609', '6112873452941356425', '7174908331407638481', '7815775335951265570', '5746188617278517738', '7806594010630606095', '8569774102074512805', '8339252880339794026', '5336015248855950042', '5174185361470774548', '4788706135661893559', '5306192050493525400', '5493710909793550703', '4965997883804609652', '5067957331885596176', '6281451975521648233', '9065438427456473119', '4863382925961593039', '4925592275800448365', '5668226879959863330', '8392872110720574853', '5018700233439740089', '8739594812324937227', '8092286678012585720', '7322969736637551169', '6437547794800861642', '6910498187402834843', '6368919717996552453', '8714819525850995439', '6361439295321038204', '4940939650185692511', '5824571224029788946', '7567001406164312180', '4643921437689495286']
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
            



