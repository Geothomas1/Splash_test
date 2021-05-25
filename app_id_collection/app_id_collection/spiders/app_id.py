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
tag=['5703447331110116266', '5991820500290225627', '5951651740951698949', '4752859590457236573', '4879986113139967562', '4830096108162114659', '7781812905994602063', '5580753889161430391', '6969432818927594171', '6946214991042968160', '4910067383519368299', '6921902750734689038', '7173825782151163970', '5536369398281991413', '7514532260246976284', '9098949793629248142', '7184623397550987805', '8812293306013257434', '6430481524202549253', '7142911710952180802', '7323033508948948661', '5248323385005787636', '7468190409947973272', '5427737915563914060', '5668115854920695224', '6768033056419806404', '8278990351028394215', '8331818305029646302', '7486557340409834297', '5322067040989819369', '4705841309895745907', '6687626582919335283', '5762372871367347350', '6013359427889042354', '6078764175206603489', '5818463921423105010', '8810568067913087175', '7698945525845997282', '7607779422266139562', '8766567902703128738', '5237706065932797238', '8441716054945709576', '5322088913293892687', '6745204088656950886', '6172324052633291740', '5177114267834249850', '8045320491742913780', '5010470516879670397', '6368329215346388078', '5341220067940219234', '7862052344916793257', '6079274718015610863']
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
            



