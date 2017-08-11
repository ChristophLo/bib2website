from pybtex.style.labels import BaseLabelStyle

# This is a label style which just returns whitespace instead of labels (which consequently means that the custom html
# backend will simply ignore the label

class LabelStyle(BaseLabelStyle):

    def format_labels(self, sorted_entries):
        for number, entry in enumerate(sorted_entries):
            yield " "