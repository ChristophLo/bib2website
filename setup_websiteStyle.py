from setuptools import setup

# to use: python setup_websiteStyle.py develop

setup(name='Website Style',
    author='Christoph Lofi',
    py_modules=['website_bibliography'],
    entry_points = {
        'pybtex.style.formatting': 'website = website_style:Style',
        'pybtex.style.labels': 'year = year_labels:LabelStyle',
        'pybtex.style.sorting': 'year_month_title = yearMonthTitle_sorting:SortingStyle',
        'pybtex.backends': 'web = backend_htmlP:Backend'
    }
)