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
tag=['9149959017307409255', '6439584985733600562', '6025543057746790612', '8186440931703540103', '8741035511168472898', '4918145749807497684', '5753142263287687173', '5523816525275739209', '8622182788171711792', '6129154530509899420', '6920813801081050837', '8524188874318551105', '7712251101255662062', '5459858422747543537', '6016394304874143846', '5081264993391755178', '8611114973919810284', '8290616447773504535', '7713355441775984816', '5349901731228187901', '7998569620575108010', '6634791501999313498', '6493616717997087751', '8840341766585144912', '8512248742869918055', '4950399874559570964', '8514220296668660573', '9121248041345231805', '6765589066257265194', '5557093314074911698', '6771134034616071142', '9044959494022368398', '5444161410434444707', '6367044961557900850', '5610193712124666115', '5502002953642207822', '4706882063239124119', '6606197575519776775', '5843604371215345798', '5456789389650092443', '6999210529982541799', '9219998199583380936', '8231714925977809267', '6964306245292491680', '5328952739200740623', '6487037942523730425', '7793495547883470506', '8798317113552410924', '8380546301347768349', '5317991957791934822', '4901969063898591648', '7014501217618371133', '6562473125002873974', '7011642755792073831', '5059867847256046132', '4766140096964736822', '5408830062919995155', '6004216323944338849', '7652791855964173582', '5466859474658028637']
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
            



