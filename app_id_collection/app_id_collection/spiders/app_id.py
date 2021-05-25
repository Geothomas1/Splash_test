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
tag=['8079955917303844402', '6684910003004836960', '5895899721894250963', '4753252917723519378', '7472726716209378277', '5232135485269293273', '8584248579290082162', '4753490543437411657', '8644884162358965696', '5894614106108708006', '8922759641957919013', '7068415173431274849', '7453784257136161248', '7401370038771571034', '6458361402538998431', '5702755021056795237', '6976163580580833640', '7527275342120625141', '4753728819200715319', '6073454506753223131', '5971194736923269270', '6959060733285647693', '9097330061873557541', '8537906390447207727', '8601570156292368382', '6556531494862331777', '5119927304674687508', '6628633217518563439', '5937540532878899842', '5615570874779308530', '5621070044383975821', '5779705162275747762', '6184264835129104758', '4832530708930453268', '5686935970274699130', '4673974461175569519', '8108023238099833611', '5145884633576778421', '7997445572702428974', '5577029779191202734', '6473927149931201921', '8390907165763915922', '7915220460954696537', '8223732465863768123', '7429437200391510127', '7470465118062916723', '5047555158135158047', '6580651661718103128', '9147250652346042617', '5746884977063063254', '5426969801846046500', '8646255328208507716', '8923881278968064760', '4684520990643024417', '4817678496049908863', '4958553927474292074', '5261674557356362705', '4818490654128725661', '8049629713604820627', '7117358121811947947', '8999869250127226879', '4803901892787038368', '6134938121683955482', '5557753668168425521']
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
            



