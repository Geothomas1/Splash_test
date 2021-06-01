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
tag=['5916021916323754001', '5423123442527584113', '5455714323056757660', '7392259381359373428', '8309760023652145687', '5376882061498343107', '7204804806671865945', '4834741911194926364', '9007244131904541402', '7886251635695876585', '5478184498237234861', '8709222688258356982', '5723540925260269727', '7405165335320155356', '7289380923849881406', '5601863351707722850', '5864914833051323614', '7732974967851994989', '9101561504608515615', '7251994996830956628', '8689527253823333168', '8532913460643669367', '6953279392241620625', '6308571988260812159', '6026662091126952149', '7668437179940949084', '8827393609830729715', '8428714843821644566', '8149340042168206762', '6175439068782733243', '5834537757514841658', '4704948125368239743', '7979003911176195612', '8842520425875022308', '6533804748613694032', '6173772219884369338', '7055952154975103367', '5635460827578728682', '4785136720665883843', '8131303897564344011', '8890974987844105827', '8603748042972386324', '6174346963061737104', '5432412240591964493', '5978809520974942611', '5860660234681628777', '5138833726102357711', '5012790930527588462', '8750386834662718684', '5294497516434897025', '6242834575678506469', '8256466388637009150', '6871077279091887172', '6448568837591418600', '5813430632685690933', '7249142474316336529', '6182357168573217023', '7363732724075687497', '5663977698074970225', '6883964833740727871', '8945539023671021149', '8577900714837720826', '7933302450459111395', '5286438232740520071', '4621612365242715855', '5161174874361148977', '6789675197501125384', '7150734169177801104', '6837197251844856870', '5163668033564547514', '8934854774710992946', '7750988640342773111', '8742758264384045595', '8697182991655560960', '6070329290279442076', '8832820871119576011']
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
            



