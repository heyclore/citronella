#MIT License
#
#Copyright (c) 2023 Eko Purnomo
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


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
