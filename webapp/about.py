import justpy as jp
from webapp import layout, page

class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page.", classes="text-4xl m-2")
        jp.Div(a=div, text="This is some descriptive text about the site.", classes="text-lg")
        return wp

