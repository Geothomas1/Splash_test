import scrapy
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

#url=['https://play.google.com/store/apps/developer?id='+i for i in tag]
class DeveloperSpider(scrapy.Spider):
    name = 'developer'
    allowed_domains = ['x']
    def start_requests(self):
        tag=['Ashudosa+Apps', 'Megan+Davies', '123+Kids+Academy+LLC', 'Tibus', 'Grow+Together', 'OWNA+Childcare+Apps', 'DynamicDevs', 'Greysprings', 'Learning+BOOKtique', 'KritiDev+Developmental+Solutions', 'LearningBook', 'BYJU%27S', 'Tiltan+Games', 'REMINI', 'Exam+Books', 'Ultra+Education+Pvt.+Ltd.', 'Creative+Galileo', 'Benipol+Limited', 'AtoZ+Kids', 'OckyPocky', 'hartwell+Mhunduru', 'Faddu+Lab+Technology', 'ChuChu+TV+Studios+LLP', 'ZSH+Studio', 'Baby+AngelGames', 'Infxcel+Education+Services+Pvt.+Ltd.', 'Sharp+Brains', 'Kunal+Applications', 'KinderPass+Pte+Ltd.', 'Last+Fighter', 'Smart+%26+Serious+Software+3S', 'Students+Apps', 'Satvik+Ghag', 'Digital+Teacher', 'SAS+Tech', 'Learning+Genie+Inc', 'PRAADIS+TECHNOLOGIES+INC', 'Khan+Academy', 'SUBCORTICAL', 'Aussie+Childcare+Network+Pty+Ltd', 'Culture+Alley', 'Age+of+Learning,+Inc.', 'Orenda+Educational+Studios', 'Great+Learning', 'Perpetuum+Capital+Ltd.', 'Flinto+Learning+Solutions', 'Plato+Media+Ltd', 'tp+Kids+Games', 'Extramarks+Education', 'GunjanApps+Studios', 'Vedantu', 'funnymentalgame', 'CBIEN-TECH', 'NATIONAL+INSTITUTE+OF+OPEN+SCHOOLING', 'Saleha+Group', 'SBT+Human%28s%29+Matter', 'Xplorabox', 'Growth+Book', 'Urva+Apps', 'Data+Ingenious+Global+Limited', 'Bhavishya', 'Blink+Max', 'kidpid', 'GalaxyProduction', 'Chu+Chu+Games+Studio', 'Lihan+Deng', 'Tyche.app', '10X+Learning+Lab', 'Roger+Federer+Foundation', 'PleIQ', 'Didactoons', 'myillumine', 'Jseyn', 'Gamester', 'Proven+Kids', 'HeyCloudy+-+Audio+Stories+for+Children', 'Digital+DS', 'Wachanga', 'Spongeminds', 'urmyapps', 'AV+Store', 'Apple+Byte+Games', 'Pine+Tree+Studios', 'Parenting+Pets+Care+Tips', 'Oda+Class', 'Preschool+Learning+apps+for+Kids', 'Blake+eLearning+Pty+Ltd', 'chimdel', 'apps4allStates', 'roxx+ton', 'RajalakshmiRTY', 'Parvez+Khan', 'Team+Madlab', 'ADB+Cipta+Studio', 'InnovationM', 'Techprolix+Services', 'DiGi+Gamez', 'ApDroid', 'Glob+Tech+Hub', 'upGrad', 'Learning-Aidan', 'Matthew+J+Lawrence', 'Playfully', 'Eduplum', 'JobboJ+APP+-+job+tools', 'Viva+Books', 'Taman+Edukasi', 'Entrepreware+for+Education', 'Free+Educational+Games', 'Neon+Technologies', 'Therithal+Info', 'The+Brain+Stormers', 'CuSeJu', 'Mansur+Haider', 'eStudy+Solution', 'Hidden4World', 'Picslo+Corp', 'MobDevs', 'Millionaire+Mind', 'Cambridge+University+Press+%28India%29', 'ParentsCare', 'Communication+School', 'Technovert+Library', 'Solution+Maker', 'Krishna+Communication', 'Rajshri+salve', 'Stansoft+Corporation', 'Avaz+Inc.', 'Tech+Mateen', 'freeCreativity2019', 'Masta+Communication', 'Appmax365', 'Ambika+Recharge+Point', 'Signal+Foundation', 'EnglishEverydays', 'My+New+Studio+World+Apps', 'DevTek+Studios', 'JABstone+LLC', 'Appseen+studio', 'APLUS', 'SK+COMMUNICATION+PVT.LTD', 'BS+Communication', 'Infinite+Buffer', 'EduSoft+Dev', 'CART+-+RLANRC', 'Engineering+Wale+Baba', 'STATE+ELECTION+COMMISSION+UTTAR+PRADESH', 'Explore+Quiz']
        for i in tag:
            url='https://play.google.com/store/apps/developer?id='+i
            yield SplashRequest(url, self.parse,  endpoint='execute', args={'lua_source': script, 'url': url})
        
    def parse(self, response):
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

        
