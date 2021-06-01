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
tag=['8453050552608864450', '4731455310932876078', '5826658695780515101', '5613926216377211169', '9220832967063682851', '7161132526416062293', '5590507773860463198', '5418419284972301255', '7198807840081074933', '8934848548747347540', '5303585434427015385', '6851542386118790752', '5867633860293913811', '5742525399702068183', '8575377796831916790', '4965529572701357445', '7459374303988085432', '7617928052829487062', '4976741012020149132', '5680176953688156758', '9135165741484938670', '6329180147071621228', '4793001538560147312', '8551845612931782770', '5209618649320417725', '5343038778669502158', '7462055590366838980', '8608112411639118948', '8370089986526728678', '8606293477677343418', '6288320000222168085', '7914023640674141967', '4847841756611443627', '5920599758791067813', '7623600053690589384', '6032199050372536452', '5411008958069875176', '5879374323488164415', '6207418185183526438', '5584342684886700375', '8587997920132997064', '5204603126902930560', '7856700613704078895', '5695007729502642221', '4619950301745715207', '7288359718234821587', '6677698179098584519', '8459686365976095948', '6326687603874220895', '6275097862825829247', '8421743085353587848', '6215805987066412110', '4661858929332099976', '5823497573355077610', '9222635353408198758', '5186183270029982619', '7847809166172077361', '5568561849731527634', '7290626085125482703', '4631465000030912292', '7990189312355005597', '6166991346549604593', '7056037792991834747', '7869615586662183573', '7242518977443297315', '4920220132570332460', '7484824553057994141', '7278020566356794369']
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
            



