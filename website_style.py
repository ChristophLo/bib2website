# I am extending and overwriting pybtex's UnsrtStyle here.
# I change the following:
# - Simplified URL and DOI labels
# - surround titles with "
# - Remove the "IN" for conference proceedings

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.formatting import toplevel

from pybtex.style.template import (
    join, words, together, field, optional, first_of,
    names, sentence, tag, optional_field, href, Node
)



# Initialize to use only year labels for sections, sort by year, month, and then title in descending order
class Style(UnsrtStyle):
    default_sorting_style = 'year_month_title'
    default_label_style = 'year'


# Overwrite URL format for PDFs: Process URLs, only use PDF as link label
    def format_url(self, e):
        # based on urlbst format.url
        url=field('url', raw=False)
        return words [
            href [
                url,
                'PDF'
                ]
        ]

# Overwrite URL format for DOIs: only use DOI as link label
    def format_doi(self, e):
        # based on urlbst format.doi
        return href [
            join [
                'https://doi.org/',
                field('doi', raw=True)
                ],
            'DOI'
            ]

# Overwrite title style: surround with " "
    def format_title(self, e, which_field, as_sentence=True):
        formatted_title = field(
            which_field, apply_func=lambda text: text.capitalize()
        )
        formatted_title= join()[
            '"',
            formatted_title,
            '"'
        ]
        if as_sentence:
            return sentence [ formatted_title ]
        else:
            return formatted_title

# Overwrite: Remove 'IN' from proceedings.
# THIS DOES NOT WORK - NO IDEA WHY....got too annoyed by it so I gave up on fixing...
    def get_inproceedings_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            words [
#               'In',
                sentence [
                    optional[ self.format_editor(e, as_sentence=False) ],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    optional[ pages ],
                ],
                self.format_address_organization_publisher_date(e),
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

# Overwrite: Remove 'IN' from proceedings.
    def get_incollection_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            words [
 #               'In',
                sentence [
                    optional[ self.format_editor(e, as_sentence=False) ],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_chapter_and_pages(e),
                ],
            ],
            sentence [
                optional_field('publisher'),
                optional_field('address'),
                self.format_edition(e),
                date,
            ],
            self.format_web_refs(e),
        ]
        return template