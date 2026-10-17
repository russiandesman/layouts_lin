#!/bin/bash
# usage (as root): ./install.sh [--remove]
set -eu

here=$(dirname "$(readlink -f "$0")")
symbols=/usr/share/X11/xkb/symbols

if [ "${1:-}" = "--remove" ]; then
	"$here/xkb-register.sh" remove
	for f in "$here"/layouts/*; do rm -f "$symbols/$(basename "$f")"; done
	exit 0
fi

cp "$here"/layouts/* "$symbols/"
[ -f /usr/share/X11/xkb/rules/evdev.xml.backup ] || cp -p /usr/share/X11/xkb/rules/evdev.xml /usr/share/X11/xkb/rules/evdev.xml.backup
"$here/xkb-register.sh" add
