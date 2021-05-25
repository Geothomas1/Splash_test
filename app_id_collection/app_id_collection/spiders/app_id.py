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
tag=['6248041253636254082', '8078293098034355632', '8563168127601237279', '6626720585336981822', '6759270530445161451', '4653255330630064164', '7309798795499817833', '7264616766822747039', '6870964679910714093', '7544284391342892334', '7106147798960805680', '5148420297631324044', '6524834394542894682', '6196738093699868625', '4797888579286699402', '5707194723486037757', '9049171545073040139', '5006455422838188245', '7705077453684003100', '8927372468482477196', '5243745125681968825', '6609422342359681799', '7561844357934539552', '8858034574306643292', '6586446680687749448', '6300016652050785971', '8567646723268777320', '7263645302164630442', '7670331570699900357', '4787668976400770516', '8503753108326993615', '8057230495664781722', '8318786497754536688', '5981335106476514858', '5975903415714115015', '8476331292479103195', '6848177009077450865', '6988417967071057070', '7958405082226061986', '5515765620403081913', '7598455829905594537', '6345261670638519127', '7786610230657616881', '8086266740700000611', '7537986813266629785', '7018912757664405572', '6886919362373660592', '7186791252237508317', '7587445973347788488', '5705148315929971496', '7033627942863017296', '6446803702512074490', '6012600657594903378', '8002844273783316701', '8832114234698936822', '5568626362316510919', '7426371415851456012', '5493600245546080916', '6125644571795195171', '4678027420363017452']
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
            



