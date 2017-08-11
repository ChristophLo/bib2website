from pybtex.style.labels import BaseLabelStyle

# supresses labels of indiviudal publications, replacing them by year labels if a new year block starts

class LabelStyle(BaseLabelStyle):



    def __init__(self):
        self.lastyear = None


    def format_labels(self, sorted_entries):
        for number, entry in enumerate(sorted_entries):
            year = entry.fields['year']
            if self.lastyear != year:
                self.lastyear = year
                yield entry.fields['year']
            else:
                yield ""