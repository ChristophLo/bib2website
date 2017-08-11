from setuptools import setup


# This registers my custom styles with the pybtex plugin system (see bytex docu)
# to use: python setup_websiteStyle.py develop

setup(name='Website Style',
    author='Christoph Lofi',
    py_modules=['website_bibliography'],
    entry_points = {
        'pybtex.style.formatting': 'website = website_style:Style', # my custom style
        'pybtex.style.labels': 'year = year_labels:LabelStyle', # only use years as labels
        'pybtex.style.sorting': 'year_month_title = yearMonthTitle_sorting:SortingStyle', # sort by year, month, title in descending order
        'pybtex.backends': 'web = backend_htmlP:Backend' # use my html tags (e.g., h3 and p)
    }
)