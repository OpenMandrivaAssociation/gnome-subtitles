
%define name	gnome-subtitles
%define version	0.6
%define rel	2

Summary:	Subtitle editor for the GNOME desktop
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
URL:		http://gnome-subtitles.sourceforge.net/
Source:		http://downloads.sourceforge.net/gnome-subtitles/gnome-subtitles-%{version}.tar.gz
Patch0:		gnome-subtitles-desktop.patch
License:	GPLv2+
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2
BuildRequires:	glade-sharp2
BuildRequires:	gnome-sharp2
BuildRequires:	ImageMagick
Suggests:	mplayer

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

%post
%post_install_gconf_schemas %{name}
%{update_menus}

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS CREDITS NEWS TODO
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*
# FIXME: someone else should own this:
%dir %{_datadir}/omf
%dir %{_datadir}/omf/%{name}
# TODO: add omf handling into find_lang.pl:
%{_datadir}/omf/%{name}/%{name}-C.omf
%lang(ca) %{_datadir}/omf/%{name}/%{name}-ca.omf
%lang(sv) %{_datadir}/omf/%{name}/%{name}-sv.omf
