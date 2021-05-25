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
tag=['8799287544869103417', '8177767716036753857', '5054100336718777716', '7971689297057456978', '7376997889575170266', '7118381535300531301', '9170374226340538582', '4845678107952608200', '7405291348832307808', '7980236402233523571', '6957790963724025053', '8303261579726805387', '8452274342341551246', '8565001205116030983', '6467764924748919249', '7600076039959501027', '6250653333404066854', '4957026383745143548', '6229137220582721191', '5396229733351759132', '8387589286898375037', '4680476163854203393', '6693021783623901421', '8837650268504175119', '9048946412517301749', '8384129624529484599', '8545083715916481352', '8877157440399496306', '6075165531768716801', '8236250652182048610', '8735477036873604804', '4656343638685426415', '7565902691518792438', '5008941174174978115', '4925976860338825268', '6290986103939408975', '4965108846089559093', '5351598058178212764', '6380945586035889122', '4938847300036336646', '5813453899714431792', '6304734212719647502', '6419149029293804684', '5515021379431089426', '4664534164976759213', '5636295361649069546', '8401944924818644128', '5652389115747746054', '9106923612252429752', '6634799579349342125', '6635010324226306360', '6384770293240231428', '8316925974532835033', '6071334656709749720', '5812866175713301024', '7774452492795229256', '8117243197439902812', '7794148306018100572', '8345494053559195428', '5788023972891525673', '5354109590240370491', '4691813211944454685', '7910178651862672520', '4846771086459924061', '6656359931532360289', '7486661504684506773', '5426997585131798235', '5059496263043925303']
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
            



