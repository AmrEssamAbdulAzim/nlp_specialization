from IPython.core.display import HTML
def css(path = './style/style.css'):
    styles = open(path,'r').read()
    return HTML(styles)
