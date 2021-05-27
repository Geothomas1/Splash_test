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
tag=['8775081457221856353', '7019485828897028019', '8705932994768098635', '8754033884378019323', '5831359213935146421', '6919162882130996928', '6682841885717538533', '6295716475949244884', '7686194056937543414', '8343645726609648207', '5398665944199388404', '5431158417217653512', '7790177431403907507', '4934938254167092419', '7789957673955675970', '7168263043387564654', '8195837963688127156', '7700459620007193141', '6827504276769432249', '8811057342055379613', '6915261801345011098', '6883128421109443662', '8189487451561882349', '9056554144614937411', '6208524665499510567', '7526655877048557790', '6641250738393437993', '8155932531518409266', '5426030454596349772', '6885542347755761328', '7348316848735452837', '7530231193074438608', '6389919162818792210', '5617848948072921163', '4710857213064624013', '5927151686819374113', '5925140520329850553', '8423074146696097070', '7725486445697122776', '7128994579708106608', '8373792304079870635', '7137538439457445826', '6419334351754265656', '5374386074687764961', '7282538041318232185', '7260648009456928018', '4859664986255107201', '7552709652135185796', '8547979362694237509', '5817081448555497827', '7495440330263947729', '9088707552106700714', '5936741008733903214', '8517069064970410639', '9014550269890984600', '6546115448844739846', '6575722454612709666', '7510786529600557284', '7985584868116711077', '5474137946144630162', '5488714652077356802', '8725600669896916222', '9038864615989079188', '8512494844580700061', '5850203886760616599', '7425729344556158031', '7955827231779717327', '8336750947549318654', '6003731687492622632', '8296074494266057421', '5787818478554661072', '8610638423196297609', '7040114452287892812', '5987591346958263084', '6292192026101034724', '6324646465463897958']
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
            



