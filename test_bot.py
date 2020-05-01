import inspect
from . import bot

myBot = bot.Bot()

def test_instance():
    assert inspect.isclass(type(myBot)) 
    
def test_class():
    assert inspect.isclass(bot.Bot)