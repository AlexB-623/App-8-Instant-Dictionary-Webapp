import justpy as jp
from definition import Definition
from webapp import layout, page

class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-blue-200 h-screen")
        jp.Div(a=div, text="This is the Dictionary page.", classes="text-4xl m-2")
        jp.Div(a=div, text="Defines a word as entered.", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        input_box = jp.Input(a=input_div, placeholder="Enter a word here...",
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 "
                         "py-2 px-4 ")
        input_box.on('input', cls.get_definition)

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40", text="Enter a word to start.")
        jp.Button(a=input_div, text="Define Word", classes="border-2 text-gray-500", click=cls.get_definition,
                  outputdiv=output_div, inputbox=input_box)

        #print(cls, req)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        #widget.outputdiv.text = widget.inputbox.value
        defined = Definition(widget.inputbox.value).get()
        widget.outputdiv.text = "".join(defined)

