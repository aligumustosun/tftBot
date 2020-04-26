import cropModule
import convertModule

def get():
    goldImage = cropModule.getImage('goldDouble')
    goldText = convertModule.imageToText(goldImage)
    if (goldText != ''):
        return goldText.split[0:1]
    else:
        goldImage = cropModule.getImage('goldSingle')
        goldText = convertModule.imageToText(goldImage)
        return goldText[0]
            