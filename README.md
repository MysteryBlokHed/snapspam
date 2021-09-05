# snapspam

A CLI + library to spam multiple common anonymous message apps for Snapchat.

## Supported apps

- sendit
- LMK

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

Some information about how to use the app will be returned.
To get help for a specific target app (eg. sendit), run:

```sh
python -m snapspam sendit --help
```

Here's an example usage of the app to spam a sendit sticker:

```sh
python -m snapspam sendit cd06ec9a-2879-1afa-5108-fed08b1ecaa0 'Spammed'
```

The ID can also be replaced by the full URL, like this:

```sh
python -m snapspam sendit https://web.getsendit.com/s/b2e143fa-75f5-47ff-80ec-4fb366b336cc 'Spammed'
```

## License

snapspam is licensed under the GNU General Public License, Version 3.0
([LICENSE](LICENSE) or <https://www.gnu.org/licenses/gpl-3.0.en.html>).
