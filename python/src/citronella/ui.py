def ui(by, value, page=None):
    return {
            'by': by,
            'value': value,
            'page': page,
            }

#MARK TO REMOVE {
def Ui(by, value, page=None):
    from logging import warning
    warning("Ui module is decrepated")
    warning('use "from citronella import ui" instead "from citronella import Ui"')
    return ui(by, value, page)
#MARK TO REMOVE }
