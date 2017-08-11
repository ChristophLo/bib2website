from pybtex.style.labels import BaseLabelStyle


class LabelStyle(BaseLabelStyle):

    def format_labels(self, sorted_entries):
        for number, entry in enumerate(sorted_entries):
            yield " "