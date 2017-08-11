from pybtex.style.sorting import BaseSortingStyle


# sorts all entries by year, month, and then conference in reverse order

class SortingStyle(BaseSortingStyle):

    def sorting_key(self, entry):
        month_labels = {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
        month_label = entry.fields.get('month', '')
        if month_label in month_labels:
            month = month_labels[month_label]
        else:
            month = month_label
        return (entry.fields.get('year', ''), month, entry.fields.get('title', ''))


    def sort(self, entries):
        entry_dict = dict(
            (self.sorting_key(entry), entry)
            for entry in entries
        )
        sorted_keys = sorted(entry_dict, reverse=True)
        sorted_entries = [entry_dict[key] for key in sorted_keys]
        return sorted_entries
