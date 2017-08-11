import io
import six
import pybtex.database.input.bibtex
import pybtex.plugin

filename="all"

pybtex_style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'website')()
pybtex_html_backend = pybtex.plugin.find_plugin('pybtex.backends', 'web')()
pybtex_parser = pybtex.database.input.bibtex.Parser()



data = pybtex.database.parse_file(filename+'.bib')
data_formatted = pybtex_style.format_entries(six.itervalues(data.entries))
output = io.StringIO()
pybtex_html_backend.write_to_stream(data_formatted, output)
html = output.getvalue()

#print(html.encode('cp850', errors='replace'))
f = open(filename+'.html', 'wt', encoding='utf-8')
f.write(html)
print("Wrote "+filename+".html")