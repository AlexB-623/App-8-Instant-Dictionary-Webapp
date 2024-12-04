import justpy as jp
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp import page
import inspect
#dynamically generating the website map
imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

#from manual entry
# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(port=8001)
