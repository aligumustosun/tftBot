from . import crop, convert

def get():
    try:
        goldImage = crop.getImage('goldDouble')
        goldText = convert.imageToText(goldImage)
        if (goldText != ''):
            return int(goldText)
        else:
            goldImage = crop.getImage('goldSingle')
            goldText = convert.imageToText(goldImage)
            return int(goldText[0])
    except:
        print("Error when reading gold.")
        return 0
            