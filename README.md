# snapspam

Spam sendit or LMK messages.

## Installation

You can use snapspam without installing it.
If you want to use it from a command line anywhere on your computer,
then you can run:

```sh
python setup.py install
```

This will let you run snapspam anywhere.

## Use

To get help from the CLI, run:

```sh
python -m snapspam --help
```

or

```sh
python snapspam.py --help
```

Some information about how to use the app will be returned.

To get help for a specific target app (eg. sendit), run:

```sh
python -m snapspam sendit --help
```

or

```sh
python snapspam.py sendit --help
```

Here's an example usage of the app to spam a sendit sticker:

```sh
python snapspam.py sendit cd06ec9a-2879-1afa-5108-fed08b1ecaa0 'Spammed'
```

The ID can also be replaced by the full URL, like this:

```sh
python snapspam.py sendit https://web.getsendit.com/s/cd06ec9a-2879-1afa-5108-fed08b1ecaa0 'Spammed'
```

## License

snapspam is licensed under the GNU General Public License, Version 3.0
([LICENSE](LICENSE) or <https://www.gnu.org/licenses/gpl-3.0.en.html>).
