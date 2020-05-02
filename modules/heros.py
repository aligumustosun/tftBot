class Hero:
    buyCount = 0
    shopCount = 0
    def __init__(self,name, heroClass, origin,tier):
        self.name=name
        self.heroClass=heroClass
        self.origin = origin
        self.tier = tier
        self.poolCount = calculatePoolCount(tier)

    def increaseShopCount(self):
        self.shopCount = self.shopCount + 1

    def increaseBuyCount(self):
        self.buyCount = self.buyCount + 1

def calculatePoolCount(tier):
    if(tier == 1):
        return 39
    elif(tier == 2):
        return 26
    elif(tier == 3):
        return 21
    elif(tier == 4):
        return 13
    elif(tier == 5):
        return 10        

kayle = Hero('kayle', 'blademaster', 'vakyrie',4)
yasuo = Hero('yasuo', 'blademaster', 'rebel',2)
masterYi = Hero('masterYi','blademaster','rebel',3)
xayah = Hero('xayah', 'blademaster', 'celestial',1)
fiora = Hero('fiora', 'blademaster', 'cybernetic',1)
irelia = Hero('irelia', 'blademaster', 'cybernetic',4)
shen = Hero('shen', 'blademaster', 'chrono',2)

blademasters = [kayle,yasuo,masterYi,xayah,fiora,irelia,shen]

graves = Hero('graves', 'blaster', 'spacePirate',1)
jinx = Hero('jinx', 'blaster', 'rebel',4)
lucian = Hero('lucian', 'blaster', 'cybernetic',2)
ezreal = Hero('ezreal', 'blaster', 'chrono',3)
missFortune = Hero('missFortune', 'blaster', 'vakyrie',5)

blasters = [graves,jinx,lucian,ezreal,missFortune]

choGath = Hero('choGath', 'brawler', 'void',4)
malphite = Hero('malphite', 'brawler', 'rebel',1)
vi = Hero('vi', 'brawler', 'cybernetic',3)
blitzcrank = Hero('blitzcrank', 'brawler', 'chrono',2)

brawlers = [choGath, malphite, vi, blitzcrank]

ziggs = Hero('ziggs', 'demolitionist', 'rebel',1)
rumble = Hero('rumble', 'demolitionist', 'mechPilot',3)
gankplank = Hero('gankplank', 'demolitionist', 'spacePirate',5)

demolitionists = [ziggs, rumble, gankplank]

khaZix = Hero('khaZix', 'infiltrator', 'void',1)
kaiSa = Hero('kaiSa', 'infiltrator', 'vakyrie',2)
fizz = Hero('fizz', 'infiltrator', 'mechPilot',4)
shaco = Hero('shaco', 'infiltrator', 'darkStar',3)
ekko = Hero('ekko', 'infiltrator', 'cybernetic',5)

infiltrators = [khaZix, kaiSa, fizz, shaco, ekko]

darius = Hero('darius', 'manaReaver', 'spacePirate',2)
thresh = Hero('thresh', 'manaReaver', 'chrono',5)
kassadin = Hero('kassadin', 'manaReaver', 'celestial',3)

manaReavers = [darius,thresh,kassadin,irelia]

soraka = Hero('soraka', 'mystic', 'starGuardian',4)
sona = Hero('sona', 'mystic', 'rebel',2)
karma = Hero('karma', 'mystic', 'darkStar',3)
lulu = Hero('lulu', 'mystic', 'celestial',5)

mystics = [soraka,sona,karma,lulu]

neeko = Hero('neeko', 'protector', 'starGuardian',3)
jarvan = Hero('jarvanIV', 'protector', 'darkStar',2)
rakan = Hero('rakan', 'protector', 'celestial',2)
xinZhao = Hero('xinZhao', 'protector', 'celestial',2)

protectors = [jarvan, xinZhao, rakan, neeko]

caitlyn = Hero('caitlyn', 'sniper', 'chrono',1)
jhin = Hero('jhin', 'sniper', 'darkStar',4)
ashe = Hero('ashe', 'sniper', 'celestial',3)

snipers = [caitlyn, ashe, jhin]

zoe = Hero('zoe', 'sorcerer', 'starGuardian',1)
syndra = Hero('syndra', 'sorcerer', 'starGuardian',3)
ahri = Hero('ahri', 'sorcerer', 'starGuardian',2)
annie = Hero('annie', 'sorcerer', 'mechPilot',2)
xerath = Hero('xerath', 'sorcerer', 'darkStar',5)
lux = Hero('lux', 'sorcerer', 'darkStar',3)
twistedFate = Hero('twistedFate', 'sorcerer', 'chrono',1)
velKoz = Hero('velKoz', 'sorcerer', 'void',4)

sorcerers = [zoe,syndra,ahri,annie,xerath,lux,twistedFate]


aurelionSol = Hero('aurelionSol', 'starship', 'rebel',5)

starships = [aurelionSol]

poppy = Hero('poppy', 'vanguard', 'starGuardian',1)
jayce = Hero('jayce', 'vanguard', 'spacePirate',3)
wukong = Hero('wukong', 'vanguard', 'chrono',4)
leona = Hero('leona', 'vanguard', 'cybernetic',1)
mordekaiser = Hero('mordekaiser', 'vanguard', 'darkStar',2)

vanguards = [poppy, jayce, mordekaiser, leona, wukong]

mercenaries = [missFortune, gankplank]

### ORIGINS

celestials = [xayah, kassadin, lulu, xinZhao, rakan, ashe]

chronos = [shen, ezreal, blitzcrank, thresh, caitlyn, twistedFate, wukong]

cybernetics = [fiora,irelia,lucian,vi,ekko,leona]

darkStars = [shaco,karma,jarvan,jhin,xerath,lux,mordekaiser]

mechPilots = [rumble,fizz,annie]

rebels = [yasuo,masterYi, jinx, malphite, ziggs, sona, aurelionSol]

spacePirates = [graves, darius, jayce, gankplank]

starGuardians = [soraka, neeko, zoe, syndra, ahri, poppy]

valkyries = [kayle, kaiSa, missFortune]

voids = [choGath, khaZix, velKoz]