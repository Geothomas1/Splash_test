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
tag=['4629569552106247233', '5501870245674234696', '6874376245537515690', '6046120897024522899', '8347646282387743907', '7104729497754513608', '9123661985939288378', '9076108670215860604', '7053276747161751661', '5583704756355396899', '5088300453925920817', '5820789003699411150', '4804375862035154346', '5770703964047914521', '9089371232312474800', '7617665847369142302', '6673788148877661418', '7803199315446469331', '7917064729764885985', '8019821523693313490', '8869767217782954494', '9088999293965821587', '6719114643248126714', '8025726570385657583', '5508041301292489079', '7992693030913369655', '5344944687055749291', '8214005633844479367', '6085587325134519581', '5064274879792681385', '8818430266679571092', '4919086172372796373', '4816573842195886686', '8377740144678586585', '5762038271003219862', '7112553834678346464', '6466200079237172714', '7917134929169269550', '5304125630901936576', '4765086322519189753', '6990042735476603793', '4682807268332334320', '4920686718664562006', '8763785751038324185', '5889740242360748207', '4949973445142154594', '7848342892975464970', '4863017296070083332', '5143413755524121934', '4859823479958818958', '5784531331957625852', '6406859221448861616', '8271445002732597000', '7678388334981819953', '4925454784986543453', '8114619066114067433', '7818375941724500450', '6442765819056942757', '7555029852462109461', '8258407898095176676', '5059364091133678988', '6158460887360859297', '9011503121806097671', '8002996063639633369']
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
            



