#  Wikipedia Country Flags

This repository contains all country flags plus two JSON files—one including
the Wikimedia Commons link to the flag SVG details page
(`countries-remote.json`), and one with just the flag information
(`countries.json`).

The included `scraper.py` script can download the flags from the Wikimedia
Commons URLs. To run it, first create a virtualenv and then download the
requirements:

    pip install -r requirements.txt

Then simply run:

    ./scraper

This script is written for Python 2.7.

## License

The code is MIT licensed. The flag SVG files are in the public domain. See
the Wikimedia Commons links for more information.
