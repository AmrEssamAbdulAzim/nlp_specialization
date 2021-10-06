from IPython.core.display import HTML
def css():
    styles = open('./style/style.css','r').read()
    return HTML(styles)
