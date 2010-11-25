
%define name	gnome-subtitles
%define version	1.1
%define rel	1

Summary:	Subtitle editor for the GNOME desktop
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
URL:		http://gnome-subtitles.sourceforge.net/
Source:		http://kent.dl.sourceforge.net/sourceforge/gnome-subtitles/%name-%version.tar.gz
Patch0:		gnome-subtitles-0.9-destktop.patch
License:	GPLv2+
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel
BuildRequires:	mono-devel
BuildRequires:	pkgconfig(glade-sharp-2.0)
BuildRequires:	gnome-sharp2-devel
BuildRequires:	imagemagick
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	sublib-devel
Suggests:	gstreamer0.10-decoders

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It
supports the most common text-based subtitle formats and allows for
subtitle editing, translation and synchronization.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang --with-gnome %{name}

install -d -m755 %{buildroot}{%{_iconsdir},%{_liconsdir},%{_miconsdir}}
convert data/%{name}.png -resize 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert data/%{name}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert data/%{name}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %{name}
%{update_menus}
%endif

%preun
%preun_uninstall_gconf_schemas %{name}

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
%if %{mdkversion} <= 200710
%doc %dir %{_datadir}/gnome/help/%{name}
%doc %dir %{_datadir}/gnome/help/%{name}/C
%doc %{_datadir}/gnome/help/%{name}/C/%{name}.xml
%doc %{_datadir}/gnome/help/%{name}/C/legal.xml
%doc %dir %lang(ca) %{_datadir}/gnome/help/%{name}/ca
%doc %lang(ca) %{_datadir}/gnome/help/%{name}/ca/%{name}.xml
%doc %dir %lang(sv) %{_datadir}/gnome/help/%{name}/sv
%doc %lang(sv) %{_datadir}/gnome/help/%{name}/sv/%{name}.xml
%endif
# FIXME: someone else should own this:
%dir %{_datadir}/omf
%dir %{_datadir}/omf/%{name}
# TODO: add omf handling into find_lang.pl:
%{_datadir}/omf/%{name}/%{name}-C.omf
%lang(ca) %{_datadir}/omf/%{name}/%{name}-ca.omf
%lang(de) %{_datadir}/omf/%{name}/%{name}-de.omf
%lang(sv) %{_datadir}/omf/%{name}/%{name}-sv.omf
%lang(el) %{_datadir}/omf/%{name}/%{name}-el.omf
%lang(es) %{_datadir}/omf/%{name}/%{name}-es.omf
%lang(oc) %{_datadir}/omf/%{name}/%{name}-oc.omf
%lang(fr) %{_datadir}/omf/%{name}/%{name}-fr.omf
%lang(cs) %{_datadir}/omf/%{name}/%{name}-cs.omf
%lang(ro) %{_datadir}/omf/%{name}/%{name}-ro.omf
%lang(sl) %{_datadir}/omf/%{name}/%{name}-sl.omf
