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
tag=['5637429864365951514', '4790612881094082402', '6914174066347135597', '8722265083914099039', '7158246655505604778', '6222190402667890045', '7460567971527850230', '6054197513203380012', '8899065650239037652', '8768606447367526700', '7061545768084190314', '8024798716054605949', '8993328820659516551', '5147660840707403654', '8316022784409737247', '6797597710259707586', '6824907427361644705', '6219331770085463083', '8715317180962553411', '7706714075287612145', '7921462604522866853', '5404401136974624742', '8627297907362980844', '8012517277060108010', '7874234134476459079', '8815419854000223035', '7889013176032773316', '7005839755310179543', '5726180667255973860', '6241899858790670188', '8716008981559813282', '6183448847236799928', '6382078421030645995', '8384448047916094149', '5746679410549632395', '8250717977863157639', '9071747887405518104', '8326642621664460077', '6003361308918013001', '6724768372782189846']
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
            



