from browser import document, alert, window, html


def show(e):
    print(e.target.id)
    if e.target.id == "btn1":
        document["hello"].text = "Hello World!"
    cal = html.TABLE()
    cal.border = 1
    cal.id = "cal"
    for i in range(1, 13):
        row = html.TR()
        for j in range(1, 13):
            cell = html.TD()
            cell.text = str(i * j)
            row.append(cell)
        cal.append(row)
    document["calendar"].append(cal)
    document["calendar"].bind("click", show)



document["btn1"].bind("click", show)
