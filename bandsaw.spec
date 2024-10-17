%define title	BandSaw
%define section System/Monitoring

Summary: 	Band Saw monitor large numbers of computers by monitoring syslog
Name: 		bandsaw
Version: 	0.3.0
Release: 	9
License: GPL
Group: 		System/Servers
URL:		https://bandsaw.sourceforge.net/

Source: 	http://aleron.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:	%name-16.png
Source2:	%name-32.png
Source3:	%name.png

BuildRequires:	scrollkeeper, GConf2, pkgconfig
BuildRequires:  pygtk2.0-devel, gnome-python-devel 
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
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %name --with-gnome

# menu

desktop-file-install --vendor="" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# icon
mkdir -p %{buildroot}/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %{buildroot}/%_miconsdir/%name.png
install -m 644 %SOURCE2 %{buildroot}/%_liconsdir/%name.png
install -m 644 %SOURCE3 %{buildroot}/%_iconsdir/%name.png

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %name.lang
%defattr(-,root,root)

%doc AUTHORS COPYING COPYING-DOCS README NEWS TODO
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas

%{_bindir}/*
%dir %{_datadir}/%{name}/glade/
#%dir %{_datadir}/omf/%{name}/
%{_datadir}/%{name}/glade/*
#%{_datadir}/omf/%{name}/*
%{_datadir}/applications/%{name}.desktop
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png
%py_puresitedir/*
%{_datadir}/pixmaps/%name/*



%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.3.0-8mdv2011.0
+ Revision: 677512
- rebuild to add gconftool-2 as req

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.3.0-7mdv2011.0
+ Revision: 592378
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-6mdv2010.0
+ Revision: 436770
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.3.0-5mdv2009.1
+ Revision: 323375
- fix BR
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - use %%update_scrollkeeper/%%clean_scrollkeeper
    - use %%post_install_gconf_schemas/%%preun_uninstall_gconf_schemas

  + Frederic Crozat <fcrozat@mandriva.com>
    - Use more macros

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 0.3.0-2mdv2008.0
+ Revision: 63859
- XDG menu
- Use py_puresitedir instead of py_platlibdir/site-packages to fix build on x86_64
- Remove the %%exclude on /var/lib/scrollkeeper/* as it is not generated


* Fri Mar 10 2006 Jerome Soyer <saispo@mandriva.org> 0.3.0-1mdk
- New release 0.3.0

* Wed Mar 08 2006 Jerome Soyer <saispo@mandriva.org> 0.2.0-1mdk
- New release 0.2.0
- Use mkrel
- clean spec

* Mon Jan 23 2006 Jerome Soyer <saispo@mandriva.org> 0.1.1-7mdk
- Rebuild

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.1.1-6mdk
- Buildrequires

* Thu Aug 26 2004 Jerome Soyer <saispo@mandrake.org> 0.1.1-5mdk
- Another BuildRequires

* Thu Aug 19 2004 Jerome Soyer <saispo@mandrake.org> 0.1.1-4mdk
- Fix BuildRequires

* Wed Aug 18 2004 Jerome Soyer <saispo@mandrake.org> 0.1.1-3mdk
- Fix BuildRequires

* Tue Aug 17 2004 Jerome Soyer <saispo@mandrake.org> 0.1.1-2mdk
- Fix BuildRequires

* Sat Aug 14 2004 Jerome Soyer <saispo@mandrake.org> 0.1.1-1mdk
- first build

