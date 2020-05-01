
def initializeValues(botInstance, options):
    attrs = vars(options)
    for item in attrs.items():
        setattr(botInstance, item[0], item[1])
