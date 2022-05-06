from browser import document, alert, window


def show(e):
    print(e.target.id)
    if e.target.id == "btn1":
        document["hello"].text = "Hello World!"


document["btn1"].bind("click", show)
