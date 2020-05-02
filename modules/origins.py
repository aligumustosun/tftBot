from .heros import *  

class Origin:
    shopCount = 0
    def __init__(self,name, heros):
        self.name = name
        self.heros = heros
    def increaseShopCount(self):
        self.shopCount = self.shopCount + 1


celestial = Origin("celestial", celestials)
chrono = Origin("chrono", chronos)
cybernetic = Origin("cybernetic", cybernetics)
darkStar = Origin("darkStar", darkStars)
mechPilot = Origin("mechPilot", mechPilots)
rebel = Origin("rebel", rebels)
spacePirate = Origin("spacePirate", spacePirates)
starGuardian=Origin("starGuardian", starGuardians)
valkyrie=Origin("valkyrie", valkyries)
void=Origin("void", voids)

originList = [celestial, chrono, cybernetic, darkStar, mechPilot, rebel, spacePirate, starGuardian, valkyrie, void]
