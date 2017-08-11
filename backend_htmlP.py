# This file was copey from pybtex and modified (mostly in order abuse the label system:
# in its original version, it would generate a <label, reference> pair for each bibtex entry.
# however, I changed it such that it will only generate a label for the first publication of a given year, and the text
# of that label is only the year itself. This is not how pybtex was designed to work, but I want my publication list
# grouped by year.


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