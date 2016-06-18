# country-flags

*Note: this is incomplete at the moment and hasn't been updated in a while, so I would recommend you use something else instead.*

This repository contains all global country flags, plus a JSON file that
contains the countries' ISO 3166-1 Alpha-2 codes (same as used for domain
TLDs).

An entry in the JSON file contains the following information:

    "mh": {
      "name": "Marshall Islands",
      "slug": "marshall-islands",
      "size": {"width": 570, "height": 300}
    }

The proper name and slug were taken from Wikipedia. The width and height
values refer to the proper size of the SVG flag and are meant only to indicate
the proportion rather than a specific size.

## Scripts

Two scripts are included which you don't need to run unless you want to update
the repository.

### `svg2png.sh`

Invokes [svgexport](https://www.npmjs.com/package/svgexport) and
[pngcrush](https://www.npmjs.com/package/pngcrush-bin) to convert the SVG
images to PNG. (All PNG files are already included in the repository.)

### `scraper.py`

This script can download the flags from the Wikimedia Commons URLs.
To run it, first create a virtualenv and then download the requirements:

    pip install -r requirements.txt

Then simply run:

    ./scraper.py

This script is written for Python 2.7.

## License

The code is MIT licensed.

The flag image files were taken from Wikimedia Commons and are in
the public domain.
