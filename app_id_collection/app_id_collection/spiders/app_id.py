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
tag=['5054904379876013930', '4712656101120387441', '9134966397852256976', '7202409270261184849', '5501301400877578671', '5304780265295461149', '7269704759597705101', '6702243359150166310', '4805408015718691442', '7329383055539325451', '7940398974105309077', '7944373301068016862', '8251855146399047359', '7428480088431229618', '7085816884079006362', '5090581519530412354', '8117585005772645113', '6158560934258888523', '8983041900356603899', '6005619443614255030', '6390103579106991622', '5404245822107412744', '6910719627384765267', '6272126739706369897', '8266297123979442498', '7699838077545555058', '6917812355675763032', '8920411261987725757', '8721271102014787065', '7457012453865781086', '4747964102251669835', '6938428493150384391', '5446342743455293164', '8120198890187084920', '7235961877460881732', '7268133066612098309', '8816786674298250921', '4872121712940723150', '7384858087749447908', '8519184354148100199', '5823721485212743808', '6016454352501571185', '4691969427979164946', '7391001914817731179', '8331838498168679964', '8667182650150587214', '5040168393510461358', '5156110400634422914', '7827049835786659604', '7704144261174809075', '8750294559715948452', '7301770788672848330', '7978917842873634164', '6079393151091967548', '8055206899286363452', '5879613807094071430', '4655202250776327807', '5999824997801479481', '8144184771110593871', '8299588247363747816', '5078602881104558307', '7359018666695983370', '8557873250275362724', '7540147141708296598']
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
            



