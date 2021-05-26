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
tag=['5106256092000264794', '5974961919949765829', '8009995264816632577', '8681746765284691365', '8351053017163732973', '8825633726210863651', '5797362044671721677', '8144116374836693624', '6295337706296843782', '6928214480311523298', '6335541071240142953', '7150073629398910784', '6499621994133141836', '5124227544754535546', '7726994626564255251', '9180971978456225695', '5341384172504084328', '5112137337674982155', '5294830792045639171', '5553512241509279276', '6014207378961140604', '4853352544704072237', '7049909116061806824', '7266372009569545617', '6488807626217264896', '5417608463901585695', '4971597023821593055', '8635429727829120677', '7234017972830944161', '8319098749428609038', '5260266383047667744', '6277557169686910852', '7265678888812659353', '6951717752477491672', '7164002943998762662', '7002436385081637591', '8900683127979486042', '8357444268722550143', '6986601647854856609', '5433512159132148291', '6514438665633869560', '8960935526565966970', '8558223608151028037', '8393270052415845608', '5415959559536493810', '8018593231756752565', '6780876731389878911', '7947929804160402117', '5521252493018986115', '8468940951880613675', '6097657252814995747', '8707958915754236759', '8391150779610632008', '6416470982103820450', '8151352720452672201', '7574773176305258197', '8988387544477629485', '8037609104948916115', '4767594581349341713', '4826188390797347521', '8393360416371912006', '7387950367177336759', '5035652270305619783', '9116602738027013837', '6241880976999342555', '4615688081731279009', '7759005393032745005', '7054796911362697599']
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
            



