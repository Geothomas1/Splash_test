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
tag=['6129250095521728414', '5889794580951948993', '8389647877513209294', '6622682829513657910', '6660016424074311484', '5636842564017786015', '5265562142467382023', '6757766895328342390', '4826377721191473936', '7491882648187779423', '8697573006434405060', '8360112784790166921', '5481287512494853209', '9030755777689633935', '6818635234410833618', '7832278806755464985', '8806955538288493518', '7459431437683004666', '7019209995775785766', '5724727398547865375', '6807300839110548631', '9068015467276965886', '8926690491753383787', '6691955070447269054', '7171737052170953279', '8427522728338548054', '6341813657055536512', '6640674686450056742', '8739575527344906778', '4969231303044142311', '4963421706149452956', '7066015150508592920', '6164464346265505739', '8041357329234171156', '7840942704756122757', '9071744231135171838', '8317296649892370981', '8797712820139658035', '8667259657274095800', '4764932309994118741', '8267588674938226976', '8028458658854886103', '7197930414095142143', '5190989861441585338', '6772881027462511619', '8100302491828831310', '7259314777797865014', '8202370843426776442', '6019202542762910642', '5830206011771948306', '7926094059048687069', '7450272158591222207', '8048019984099735689', '7316621486105060042', '6690887408008727284', '7821466375776970130', '5659502539886717798', '8362379826967613495', '5525399683204764261', '4795740031281638576', '6961277262339865393', '7048823303420170466', '5012612979556849843', '5210088548941724496', '9142365525037433995', '4856165464338376362', '5861736339967154127', '5454778391059402545', '6593577131449985296', '7172804699709559157', '5948131385545989618', '7884911604897753152']
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
            



