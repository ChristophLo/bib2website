# bib2website

This transforms a Bibtex file into HTML format, i.e., for being used on a webpage, and is written in Python.
See http://www.wis.ewi.tudelft.nl/people/lofi/publications/ for an example output.

It heavily relies on the PybTex https://pybtex.org/. Basically, I just design a new plugin for pybtex, and 
overwrite  some of it's method calls. (The PybTex documentation & BitBucket repository is very useful in 
understanding how this works.)

## Installing

Run setup.bat (or the two Python commands in it). It installs pybtex, and registers the custom pybtex plugin.

## Using

Just run `python convert`. Currently, it is hardcoded to load a file named `all.bib` in the project's root folder,  
and generate `all.html`.

In order to have PDF links, the URL field in the bibtex file should be used. I use another github project to host 
all my fulltext files.
When using the month field, either use "01", "02", etc., or "jan", "feb", etc. in order to have proper sorting.


