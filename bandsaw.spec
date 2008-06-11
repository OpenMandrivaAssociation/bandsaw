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
BuildRoot: 	%_tmppath/%{name}-%{version}-%{release}-buildroot

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
%post_install_gconf_schemas %{name}
%update_scrollkeeper

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%clean_menus
%clean_scrollkeeper

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
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%py_puresitedir/*
%{_datadir}/pixmaps/%name/*

