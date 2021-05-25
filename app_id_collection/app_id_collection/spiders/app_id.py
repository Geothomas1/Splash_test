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
tag=['8845989045962492255', '4974373457372675433', '6109727420380587100', '7177522510008003462', '8569053704305438219', '6652204215363498616', '8329128493092595197', '8378379050415836542', '6945065669524980357', '6359127544023348883', '6902781118617052240', '7501565740759326848', '7967021935927788100', '5234081374686607357', '8164692733374583600', '7512860745899086653', '6506789924810034651', '6319120981614333173', '4958271348455148937', '6509589977203669354', '8852110459087379813', '5413818837993147136', '5899481596543981682', '7522753104729450556', '7408514901361227487', '8246846804647898907', '6609028214845253036', '8137263171989801686', '7675193699102172570', '7552662956053320937', '5552831794136932226', '8618197750848187511', '4636127343048591981', '6039896374800904750', '8687360836752847921', '5756470432824689504', '7009198853434431624', '5051971012315799255', '4855531173145198384', '8141117198831554751', '5987241365750978230', '5642703513409476274', '6528811196348758064', '6121265220714918912', '7254306595367699032', '7717865146720288098', '8956405876087413010', '6269157789752782502', '7131320753425091714', '7404417934018800993', '4956360225355267757', '9060121168255561144', '5726714232238156247', '7728500280927353474', '7366482407755204650', '6477477712317562239', '7930656545935917988', '5165848438589069541', '8932614134248228962', '7509577868289761266', '8065093959658744305', '6223066190039159950', '8838852983959657472', '7830779348988121640']
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
            



