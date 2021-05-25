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
tag=['6326552568877571622', '4821063992681531183', '6824172270623548337', '9133805840658145295', '6210892191814219739', '6363680316049191453', '8867762761121579760', '9079495187558250222', '7738341481752798664', '5340607874093184002', '9156197050939245360', '8346241893457194872', '8110545517917947173', '5120608264612581403', '8139980401558834673', '9051416296714690795', '6084630210939053254', '9117066348430156540', '8453266419614197800', '7485625865937539827', '6122785809835701236', '8639687712685240031', '4633363737443524616', '6830735644801210985', '6265974710689821899', '8945700516389597914', '8982032693403290183', '6855367077925350149', '6081695019104263888', '7468614254825273390', '7167433634843766053', '8648437764305366837', '7726589470979124240', '8773055115709493082', '6785179244029480206', '7171278455558423306', '7242794089742642803', '4966770649856918359', '5936958381705961095', '7771193477760727924', '5188907250231402288', '4618462911525860026', '7995429441780197731', '7642165564141060559', '6171217726420235283', '8772211604771808682', '4905497296259340293', '7207907366520110352', '7632441788225363601', '6873703430690430701', '7604507924975836995', '9153363562567870894', '5063646542534198021', '6595810323871232089', '7206116052122291421', '8644025671489381606']
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
            



