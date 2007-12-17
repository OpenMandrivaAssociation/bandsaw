%define name bandsaw
%define version 0.3.0

%define Summary Band Saw monitor large numbers of computers by monitoring syslog
%define title	BandSaw
%define section System/Monitoring

Summary: 	%Summary
Name: 		%name
Version: 	%version
Release: 	%mkrel 2
License: GPL
Group: 		System/Servers
URL:		http://bandsaw.sourceforge.net/

Source: 	http://aleron.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:	%name-16.png
Source2:	%name-32.png
Source3:	%name.png

BuildRequires:	scrollkeeper, GConf2, pkgconfig
BuildRequires:  pygtk2.0-devel, gnome-python 
BuildRequires:	desktop-file-utils

Requires: pygtk2.0, gnome-python, python, gnome-python-gconf

BuildArch: noarch

%description
Band Saw helps system administrators monitor large numbers of computers 
by monitoring syslog and alerting the administrator whenever interesting 
log messages arrive. The administrator has complete control over what 
constitutes an "interesting message".
 
# Prep
%prep
%setup -q

%build
%configure2_5x

%make WARN_CFLAGS=""

%install
rm -rf %buildroot
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %name --with-gnome

# menu
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="x11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%Summary" \
xdg="true"
EOF

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

%post
%update_menus
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q -o %{_datadir}/omf/%{name}; fi
touch %{_datadir}/gnome/help/%{name}/C/%{name}.html
if [ -x %{_bindir}/yelp-pregenerate ]; then %{_bindir}/yelp-pregenerate %{_datadir}/gnome/help/%{name}/*/%name.xml > /dev/null; fi

%preun
if [ $1 -eq 0 ]; then
  GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null
fi

%postun
%clean_menus
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q; fi

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)

%doc AUTHORS COPYING COPYING-DOCS README NEWS TODO
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas

%{_bindir}/*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/glade/
%{_datadir}/%{name}/glade/*
%{_datadir}/omf/%{name}/
%{_datadir}/applications/%{name}.desktop
%_menudir/%name
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%py_puresitedir/*
%{_datadir}/pixmaps/%name/*

