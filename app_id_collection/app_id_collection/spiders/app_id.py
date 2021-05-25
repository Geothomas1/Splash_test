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
tag=['5503655433278294345', '7286743576877731641', '7309208351846755609', '7287118900067551434', '4858490666867856703', '6151550621042143050', '8666936964019499600', '8839154096879034176', '5594111371514098522', '6946784258980756144', '7512173930989265272', '6381000359035679764', '8840294702292935316', '7389401077236676918', '8624731915808516833', '5939978641104704311', '6561690398918875500', '9180423026394836511', '7870784336233027937', '8712195630292425164', '7108165036376022839', '4613702646313716094', '7597213329136637965', '8387658909865206470', '8132771303646903101', '6347521131350214300', '7181809297857872397', '8083491395969879055', '8008078341620039448', '5042939762592943088', '7604680694537377809', '4853553881095416334', '5951386366988050915', '5538973920118438648', '5767281301831566189', '8183473170143142986', '5416858111791653287', '8177953827369490168', '6110517085102406359', '6889212639670330774', '8409372731084434534', '7134875155331601381', '7435846375482744096', '6523622099074451753', '7228356620005514153', '5261276536141629826', '5117445609482008507', '8153975657701484166', '8519899770592943420', '7737810875098092325', '5944549432123078244', '8997983183516294163', '8268828170978028166', '5578628898591989304', '4682432532609369869', '7420529155737384302']
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
            



