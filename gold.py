import cropModule
import convertModule

def get():
    goldImage = cropModule.getImage('goldDouble')
    goldText = convertModule.imageToText(goldImage)
    print(goldText)
    if (goldText != ''):
        return goldText
    else:
        goldImage = cropModule.getImage('goldSingle')
        goldText = convertModule.imageToText(goldImage)
        return goldText[0]
            