# stormkitty

Welcome to Stormkitty, the one and only open-source stormbound related python module!

To install Stormkitty use:

WINDOWS:
>py -m pip install stormkitty

MACOS:
>pip install stormkitty

LINUX:
>pip install stormkitty

PYPI SITE(documentation is wrong on here...but installs and everything else is fine):
>https://pypi.org/project/stormkitty/

## import

To import stormkitty type:
```py
from stormkitty import skgen
```

## documentation

The Stormkitty module defines these functions:

```py
skgen.generate_random_deck(faction)
```
Generates a random deck given a faction, i.e ```skgen.generate_random_deck("shadowfen")```, takes in another parameter: display. Set display = True to display all debugging statements in the function.

```py
skgen.kitty_to_deck(link)
```
Converts a stormbound kitty link to a python list.

