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
tag=[
'7629492194650316043', '8053638883225320952', '6410474450161514967', '6827020137409775981', '6606517650967717103', '6114322266729554171', '5781487188033065713', '7593474336411463807', '4933195047043219148', '8361394598702961772', '6264712726613180683', '7301300940481308537', '6399034087358414262', '5611387408615160200', '6702245798172599147', '5688780253878636492', '5649550218561884424', '8806247245524555054', '4856613473285277213', '7445440321282451103', '4888832637031513957', '8829343768034390423', '6475437305993333424', '4710984708419433443', '8397613283450188522', '8267903666170168180', '8977808737470449222', '7646607831544007713', '8519750831052373325', '7261624469856326668', '6257052265272019295', '8458066141208799066', '6710508499151430534', '8992394803284798263', '7832162857456081866', '8843750481982942861', '5576433517122596365', '5106009135499880425', '6061726228463739055', '7537061376996550117', '6316379119216018387', '6358817798807807916', '5557189563640849887', '8132016962172692578', '6096584730462436432', '5252449404306242119', '5835557018444455614', '5368911125977618206', '9210446533150113011', '5578120269731400480', '8208895465280067623', '6782587435720757912', '5254877886363138319', '5800483214611531142', '4644667773125940753', '9080757874599856750', '6514027630640778774', '5855097163724769457', '8943927931057499798', '8089682249090069145', '7021232503830857752', '7702928124686187323', '6767533363572246846', '7878858248674990622', '8584193581342277058', '4919062092646751301', '7083242674966483652', '5376224779511937130']
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
            



