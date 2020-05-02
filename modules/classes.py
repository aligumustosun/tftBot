from .heros import * 

class HeroClass:
    shopCount = 0
    enemyBought = 0
    def __init__(self,name, heros):
        self.name = name
        self.heros = heros
    def increaseShopCount(self):
        self.shopCount = self.shopCount + 1
    def enemyBoughtIncrease(self, x):
        self.enemyBought = self.enemyBought + x

def getMaxRolledClass():
    return max(classList, key=lambda x: x.shopCount) 


blademaster = HeroClass("blademaster", blademasters)
blaster = HeroClass("blaster", blasters)
brawler = HeroClass("brawler", brawlers)
demolitionist = HeroClass("demolitionist", demolitionists)
infiltrator = HeroClass("infiltrator", infiltrators)
manaReaver = HeroClass("manaReaver", manaReavers)
mercenary = HeroClass("mercenary", mercenaries)
mystic = HeroClass("mystic", mystics)
protector = HeroClass("protector", protectors)
sniper = HeroClass("sniper", snipers)
sorcerer = HeroClass("sorcerer", sorcerers)
starship = HeroClass("starship", starships)
vanguard = HeroClass("vanguard", vanguards)

classList = [blademaster,blaster,brawler,demolitionist,infiltrator,manaReaver,mercenary,mystic,protector,sniper,sorcerer,starship,vanguard]
