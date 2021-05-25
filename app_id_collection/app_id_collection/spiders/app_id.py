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
tag=['7617548768301184143', '4956400891330472542', '8517058244053758971', '4633590907536358909', '4878585674297231425', '5087329931733532787', '7119190022426528842', '4689663406594020347', '5627378377477294831', '6098295137465662110', '8706129684154245534', '5666353176231486894', '6392806097739253404', '7050024688574513325', '6692363691545198687', '8575142790879666281', '6720028475101379940', '7594835452769008191', '4698737590260294499', '7827533453560141672', '9161264336576745646', '6667934990533035993', '7060724462687387137', '7896272988751974486', '5272626962757710917', '8748118346627030843', '7031012817479113798', '5805991345744362578', '6462507326107552660', '8449024033176410241', '6924401024188312025', '6755703714885710635', '8530020481101400394', '5530070522465616058', '5525877581341842898', '8079816519283148987', '8077753437082489031', '7176524755618473035', '7466273100167331735', '7095285241895275273', '4972241953448860529', '6360854639703788826', '6346516402503258288', '5040318473806249978', '9033665437156874708', '6770425400362860785', '6929863735995882363', '7354100060109650436', '4701103535581775979', '8683074016728924592', '6748044026530676626', '8744468344764865153', '8449607902088672269', '6155365122654521412', '6198231247511238625', '6469575573213757987', '6922956516298225034', '7121353608421121504', '7049516368754773660', '8765522468025899509']
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
            



