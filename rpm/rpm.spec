Name:           layouts-lin
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        US-DE and Russian mnemonic keyboard layouts for Linux

License:        MIT
URL:            https://github.com/russiandesman/layouts_lin
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       perl
Requires:       libxkbfile
Provides:       us-de-layout
Obsoletes:      us-de-layout

%description
Adds XKB layouts: us-de (US with German umlauts and dead accents on RAlt),
ru-us-mn and ru-de-mn (Russian mnemonic over US and German keyboards) and
ru-ralt-us (Russian with the plain US layout on RAlt).
Select them in your desktop environment's keyboard settings after installation.

%prep
%setup -q

%build
# No build step needed (config files only)

%install
install -d -m 755 %{buildroot}/usr/share/X11/xkb/symbols
install -m 644 layouts/* %{buildroot}/usr/share/X11/xkb/symbols/
install -d -m 755 %{buildroot}/usr/share/%{name}
install -m 644 layouts.xml %{buildroot}/usr/share/%{name}/layouts.xml
install -m 755 xkb-register.sh %{buildroot}/usr/share/%{name}/xkb-register.sh

%post
/usr/share/%{name}/xkb-register.sh add

%preun
if [ $1 -eq 0 ]; then
	/usr/share/%{name}/xkb-register.sh remove
fi

# The old us-de-layout %%postun restores its evdev.xml backup, dropping our entries
%triggerpostun -- us-de-layout
/usr/share/%{name}/xkb-register.sh add

%files
%license LICENSE
/usr/share/X11/xkb/symbols/us-de
/usr/share/X11/xkb/symbols/ru-us-mn
/usr/share/X11/xkb/symbols/ru-de-mn
/usr/share/X11/xkb/symbols/ru-ralt-us
/usr/share/%{name}

%changelog
* Fri Nov 14 2025 Denis Maryin <des.maryin@googlemail.com> - 0.0-1
- Initial release: add US-DE layout for German umlauts on US keyboards.
