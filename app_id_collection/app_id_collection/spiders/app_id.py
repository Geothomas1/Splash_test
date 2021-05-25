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
tag=['9082542861300728067', '8207153197051697284', '5021947122985027343', '8000319753740505601', '7688310385332812257', '7714912241517401275', '8153420599775647311', '5835355564590584827', '6907832444062712929', '5905397015383781976', '5831537787252991481', '4677399971720148178', '8254012457599629771', '7760233184917482766', '7841225155754880142', '7354619935199300940', '5748412328683501329', '5969428307780527221', '7480711565256643861', '8250834151905755045', '5270237370262485143', '7761931842600982620', '4978773198907287742', '5623786582603332034', '8339838690752454700', '8604119438413575663', '6563338355504711902', '6560678211506052435', '7156946861841496847', '6231368318230109573', '6359826716301752973', '6490953630186869457', '7638738716385049640', '6213279750721498670', '4963031299399508227', '7273384090142724520', '8291460085210200854', '8231104445273512593', '7358465842181813208', '7155048793772172575', '6722164267631657731', '6037534384556953705', '6074176528848241752', '4966654629501615944', '7142072718011275947', '7661988094367699399', '6474619121392157352', '4897649492664600638', '6761372541552413809', '6803125036813003229', '8649977181323846189', '8042525979610527923', '5227946957970604452', '9174509328983524561', '8342984189012601483', '9213347767869807232']
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
            



