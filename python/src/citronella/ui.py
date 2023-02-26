def ui(by, value, page=None):
    """
    forward the data to page decorator and wrap into WebUi class.

    Args:
        by
        ui

    Kwarg:
        page(optional)

    Usage:
        without reference / page object. ui(By.NAME, 'q')
        with reference / page object.    ui(By.ID, 'submit', UserMenuPage)

    page are reference for the next page object if the element redirect to
    another page with WebUi click and send_keys(enter key) from input form.
    """
    return {
            'by': by,
            'value': value,
            'page': page,
            }

#MARK TO REMOVE {
def Ui(by, value, page=None):
    from logging import warning
    warning("Ui module is deprecated and will be removed in the next version.")
    warning('use "from citronella import ui" instead "from citronella import Ui"')
    return ui(by, value, page)
#MARK TO REMOVE }
