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
tag=['7458710648649831520', '7435691368118076604', '6000457270382135944', '5030215091153493141', '7709272010579555590', '8239388062551888544', '6837714705380878037', '5429886960078413650', '4787924952581121310', '6483181419534443830', '6562840654865063101', '5849752411583555949', '4920944901472600926', '7929585857419652136', '4951840469724672447', '8097517480528345077', '8912539664922103166', '7478854179093429954', '6309586922618650462', '5929888981934711049', '7507830517826479314', '4791068738421570858', '6670232843082341199', '6022206739736259467', '5191812881960609031', '4737738100150898110', '6432172309914971318', '5084522933775138667', '5364156759866729703', '8291617979019549065', '7347235321384563614', '7879428577414805675', '8641431834180289750', '6800861151420863055', '8227237868464522664', '7315706573700759915', '4684843660688611502', '4872939153261964116', '5156751533339284502', '6188034454598466210', '9213693001430155335', '6290390603068670547', '7338026722237800504', '7402300963456843524', '7812877308107321925', '6843863645668238218', '5859142547966485181', '5275021287523588210', '8777304444243699797', '5973431222214021013', '7103833940780701616', '4745391997680110268', '5495749892977154499', '8981962049679413544', '9034249023223421909', '5104976176358171231', '8371778130997780965', '6336413416180921582', '7016850595107203430', '6066402705699838242', '5157398607737086098', '7950419895673083795', '5767355450367263257', '7542649614388141535', '8065969433231964430', '5392459675676520612', '5303677165535672055', '8698634429789515109', '7600098593392542490', '5174089612406387649', '7246965209963259124', '5794073949562754893', '4726554229261549763', '6802293645107255261', '5829287075355252046', '5835428874694639698']
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
            



