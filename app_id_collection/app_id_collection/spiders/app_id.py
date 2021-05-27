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
tag=['8477330265650303454', '5057205066219237646', '6811100197368215660', '6398983204912556602', '8770524221636234808', '5330882012688773082', '5479053918790975185', '8153968423966562085', '7571735847772242141', '7340517266053483448', '7626835024493271768', '6071217222050797031', '8546246219761361624', '4644930279609598034', '8814541383037385329', '4829809212871316099', '7421513937836120672', '7883413449385121938', '7983076240713157601', '8293567295350057732', '5540375743867510508', '6237715829965588918', '5167898992825061825', '5772241316752601287', '5573588716175867665', '5471621199626367057', '4866699445711675994', '8858928162165567702', '7242195378095340889', '8185591919638004333', '7021614058533493553', '6687585029850093500', '6429639755351273131', '8300449534111494115', '7316299518796374212', '6439430251746194432', '5420037430718119685', '5702471393258602680', '8537539720533969781', '6517072115047400034', '6899462599108757852', '7246508922876085550', '5611976973613060146', '7318696982289093901', '6583833804287207115', '8009200430222730376', '8607750465675620163', '6299082762803343173', '7884039430273190491', '8803560453618027938', '8349995955169540929', '8386483420449020052', '7067002171531266653', '4780488636884711042', '7470073434502409036', '5871391326720355977', '8177477730777318013', '4824202858829604059', '5208961169657900932', '5362426020349440356', '6268401709120881168', '8430679059652796709', '8140695975958595371', '5530261387211638284', '5878760154528042781', '5916041038408626763', '4927302671110267915', '4852743658840781198', '8684376270268532371', '8250157071639820002', '7538703141191446616', '4774583956478474669']
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
            



