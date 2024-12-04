import justpy as jp
from webapp import layout, page

class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        #calling the layout class
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        #adding the homepage content
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page.", classes="text-4xl m-2")
        jp.Div(a=div, text="Homepage", classes="text-lg")
        return wp

