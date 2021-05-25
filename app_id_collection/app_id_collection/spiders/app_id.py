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
tag=['4998905880934854120', '6249202213106591684', '5634577872708699745', '7487432106452304619', '6054355236747479153', '8608582805307418947', '5100232410553863425', '4790516017113678329', '7566195279524076917', '5174560493335601869', '8026944002181256079', '8024744474397279425', '7613467650557644914', '8905848431985403707', '5179235369549587043', '7369915294756894162', '6164980448549424598', '5767774183580698237', '5606530844640665996', '6304272297927860818', '6211983233463622335', '4952188307878553448', '7586339965618757262', '7108521876094604052', '7516658445409236792', '6920352717939662208', '5620658503624629738', '8622075584094738656', '5360860234776895786', '8937379671344331084', '5200192441928542082', '6144901434893121087', '5788836030543982669', '7294187812990053072', '5468792872247497072', '6064900731986769962', '4758885743568544097', '6936834541370547357', '8209495314763865910', '6458252214101045804', '7069236154400829159', '7964283944382112788', '6159652571014897838', '8292457204635344823', '7522615915868445182', '8521794209458899239', '6411727115793723050', '6720710222501346065', '8210874504688335036', '6811378963839386870', '8967273887478673009', '5713796040511063347', '9125492304201173321', '6115766181463678254', '5972568355582725518', '6580705647706169167', '4886357526358259022', '5397108672004026154', '8128648310895390802', '6082660406713819958']
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
            



