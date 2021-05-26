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
tag=['6480067492498113295', '7997396300547592497', '6179340854760737040', '6581386003609600955', '5179975809335635357', '5736490919761049248', '7737202248787754117', '5490872689691764082', '5663244369356611470', '6973991969336325773', '5568103759260857746', '5918618593689835288', '4950866438318113604', '7874721847723303092', '8715010069986520495', '4823837874018867775', '5868586786167878959', '9118492447530150491', '8400446254553884171', '4865666723840293531', '5223994784022390103', '7417512481982083231', '8470924019770396562', '8319611253751932965', '7584371454056071079', '6144978028064292907', '8114429176533710228', '5380895901111777097', '5070008732622396849', '5239312304422800972', '6582773228793638527', '6804978169416253927', '5561995634244137752', '8037715085736938972', '8389016112556156071', '7705253489212730575', '6527796737850056416', '5295226805045639648', '7479684323020019344', '6070666933395944279', '7039591690321518933', '5642210300321155070', '5168092430937994992', '8105745308302358968', '7576932705199503286', '7012095671599126442', '8892497948616077360', '4752516198494066144', '6058419247012712231', '5145371382126043337', '8199829179519428228', '6851068626259960142', '5408843432227187062', '4698940217704070176', '9159353757673156966', '4628466809847307852', '7917131513870663760', '8323553410765419093', '4883565155119468675', '5970869472028009774', '6745855119789110233', '5476984142521908928', '5094176994936420183', '8245199172641554157', '6123263178215702660', '7038680476658827308', '5958403919479863514', '5749992122976073776', '6065043137817305363', '4760152471771772421', '6066251638635097876', '6754087684353088714']
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
            



