#!/bin/sh
# usage: xkb-register.sh add|remove|check [evdev.xml]
set -eu

dir=$(dirname "$(readlink -f "$0")")
cmd=${1:-}
file=${2:-/usr/share/X11/xkb/rules/evdev.xml}

strip() {
	perl -0pi -e '
		s{[ \t]*<!-- desman-layouts begin -->.*?<!-- desman-layouts end -->[ \t]*\n?}{}sg;
		s{[ \t]*<layout>\s*<configItem>\s*<name>(?:us-de|ru-us-mn|ru-de-mn|ru-ralt-us)</name>.*?</layout>[ \t]*\n?}{}sg;
	' "$file"
}

case "$cmd" in
	check)
		grep -qF '<!-- desman-layouts begin -->' "$file"
		;;
	remove)
		strip
		;;
	add)
		strip
		FRAG=$(cat "$dir/layouts.xml") perl -0pi -e 's{([ \t]*)(</layoutList>)}{$ENV{FRAG}\n$1$2}' "$file"
		;;
	*)
		echo "usage: $0 add|remove|check [evdev.xml]" >&2
		exit 2
		;;
esac
