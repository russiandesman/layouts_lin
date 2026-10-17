# layouts_lin
XKB keyboard layouts for Linux, the counterpart of [layouts_win](https://github.com/russiandesman/layouts_win):

[![GitHub All Releases](https://img.shields.io/github/downloads/russiandesman/layouts_lin/total?label=downloads-total&logo=github&style=flat-square)](https://github.com/russiandesman/layouts_lin/releases)

| Layout | Description |
| --- | --- |
| `us-de` | US layout, RAlt adds ä ö ü ß € and dead accents (grave, acute, circumflex, tilde, diaeresis, cedilla) |
| `ru-us-mn` | Russian mnemonic over US keyboard |
| `ru-de-mn` | Russian mnemonic over German keyboard |
| `ru-ralt-us` | Russian, RAlt (and Shift+RAlt) gives the plain US layout |

## Install
Download and run `install.sh` as root (`install.sh --remove` uninstalls),
or get the deb/rpm package from [Releases](https://github.com/russiandesman/desman_layouts_linux/releases).

Then select the layouts in your keyboard layout tool (xfce4-keyboard-settings in XFCE for example).

## us-de usage
`RAlt+a` = ä, `Shift+RAlt+a` = Ä. The same for o, u, s (ß). `RAlt+e` = €.
Dead accents: press `RAlt+'` (acute), `RAlt+backtick` (grave), `RAlt+;` (diaeresis), `RAlt+6` (circumflex), `RAlt+,` (cedilla) or `Shift+RAlt+backtick` (tilde), then the letter.

Upgrading from `us-de-layout` replaces that package.

## ru-us-mn usage
For a US keyboard. Letter keys give the phonetically closest Cyrillic letter:
a=а b=б c=ц d=д e=е f=ф g=г h=ч i=и j=й k=к l=л m=м n=н o=о p=п q=я r=р s=с t=т u=у v=в w=ш x=х y=ы z=з.
The keys that have no Latin partner carry the remaining letters: `[`=ю `]`=ж `` ` ``=щ `-`=ь `=`=ъ `\`=э.
Digits, `; ' , . /` and their Shift symbols are as in US.

RAlt gives back what the Cyrillic letters cover: `RAlt+[` = `[`, `RAlt+]` = `]`, `RAlt+-` = `-`, `RAlt+=` = `=`, `RAlt+\` = `\`, `RAlt+backtick` = backtick.
With Shift they give `{ } _ + | ~`.
`RAlt+e` = ё, `Shift+RAlt+e` = Ё.

## ru-de-mn usage
For a German (QWERTZ) keyboard. Same phonetic idea, with Y and Z in their German positions: the Z key (top row) = з, the Y key (bottom row) = ы.
Umlaut and special keys carry the rest: `ö`=ё `ä`=э `ü`=ю `+`=ж `#`=щ `^`=ъ `-`=ь.

RAlt gives what is covered: `RAlt+7 8 9 0` = `{ [ ] }`, `RAlt+ß` (the key right of 0) = `\`, `RAlt+<` = `|`, `RAlt+#` = `#`, `RAlt+^` = `^`, `RAlt+-` = `-`, `RAlt+q` = `@`, `RAlt+2` = `²`, `RAlt+3` = `³`.
Currency: `RAlt+e` = €, `RAlt+r` = ₽, `RAlt+s` = `$`, `RAlt+f` and `RAlt+p` = £, `RAlt+y` = ¥ (the key labeled Y), `RAlt+m` = µ.

## ru-ralt-us usage
For a US keyboard. Normal typing is stock Russian (Windows-style punctuation, as in `ru`).
Hold RAlt (with Shift where needed) and every key gives exactly what it gives on a plain US layout:
`RAlt+q` = q, `Shift+RAlt+2` = @, `RAlt+]` = ], and so on, including letters, digits and punctuation.
