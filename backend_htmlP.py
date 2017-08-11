# vim: fileencoding=utf-8

# Copyright (c) 2006-2017  Andrey Golovigin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""
HTML output backend.

>>> from pybtex.richtext import Tag, HRef
>>> html = Backend()
>>> print Tag('em', '').render(html)
<BLANKLINE>
>>> print Tag('em', 'Hard &', ' heavy').render(html)
<em>Hard &amp; heavy</em>
>>> print HRef('/', '').render(html)
<BLANKLINE>
>>> print HRef('/', 'Hard & heavy').render(html)
<a href="/">Hard &amp; heavy</a>
"""


from xml.sax.saxutils import escape
from pybtex.backends import BaseBackend
import pybtex.io


PROLOGUE = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head><meta name="generator" content="Pybtex">
<meta http-equiv="Content-Type" content="text/html; charset=%s">
<title>Bibliography</title>
</head>
<body>
"""

class Backend(BaseBackend):
    u"""
    >>> from pybtex.richtext import Text, Tag, Symbol
    >>> print Tag('em', Text(u'Л.:', Symbol('nbsp'), u'<<Химия>>')).render(Backend())
    <em>Л.:&nbsp;&lt;&lt;Химия&gt;&gt;</em>

    """

    default_suffix = '.html'
    symbols = {
        'ndash': u'&ndash;',
        'newblock': u'\n',
        'nbsp': u'&nbsp;'
    }

    def format_str(self, text):
        return escape(text)

    def format_protected(self, text):
        return '<span class="bibtex-protected">{}</span>'.format(text)

    def format_tag(self, tag, text):
        return '<{0}>{1}</{0}>'.format(tag, text) if text else u''

    def format_href(self, url, text):
        return '<a href="{0}">{1}</a>'.format(url, text) if text else u''

    def write_prologue(self):
        encoding = self.encoding or pybtex.io.get_default_encoding()
        self.output(PROLOGUE % encoding)

    def write_epilogue(self):
        self.output(u'</body></html>\n')

    def write_entry(self, key, label, text):
        if bool(label and label.strip()):
            self.output(u'<h3>%s</h3>\n' % label)
#            print(u'<h2>%s</h2>\n' % label)
        if bool(text and text.strip()):
            self.output(u'<p>%s</p>\n' % text)
#            print(u'<p>%s</p>\n' % text)