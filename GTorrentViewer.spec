# gnochm.spec
%define name GTorrentViewer
%define version 0.2b
%define release %mkrel 7

%define Summary A torrent file viewer
%define title	GTorrentViewer
%define section Internet/File Transfer
%define iconname gtv
%define runname gtorrentviewer

Summary: 	%Summary
Name: 		%name
Version: 	%version
Release: 	%release
License: GPL
Group: 		Networking/Other
URL: 		http://gtorrentviewer.sourceforge.net/

Source: 	http://heanet.dl.sourceforge.net/sourceforge/gtorrentviewer/%name-%version.tar.bz2
Source1:	%iconname-16.png
Source2:	%iconname-32.png
Source3:	%iconname.png

BuildRoot: 	%_tmppath/%{name}-%{version}-%{release}-buildroot

BuildRequires: gtk2-devel, curl-devel
BuildRequires: perl(XML::Parser)

Requires: bittorrent 
%description
It is a GTK2-based viewer and editor for BitTorrent meta files. 
It is able to retrieve information from trackers, check files, 
show detailed information, and modify .torrent files without 
having to start downloading.

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
command="%_bindir/%runname" \
needs="x11" \
icon="%iconname.png" \
section="%section" \
title="%title" \
longtitle="%Summary" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
Comment=Bittorent Gtk2 Interface
Exec=%{_bindir}/%runname
Icon=%iconname
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Internet-FileTransfer;Network;FileTransfer;P2P;
EOF

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%iconname.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%iconname.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%iconname.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog INSTALL README

%{_bindir}/gtorrentviewer
%dir %{_datadir}/GTorrentViewer/*
%{_datadir}/GTorrentViewer/pixmaps/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/gtorrentviewer.desktop
%{_datadir}/man/man1/*
%_menudir/%name
%_liconsdir/%iconname.png
%_miconsdir/%iconname.png
%_iconsdir/%iconname.png
%_datadir/applications/mandriva-%name.desktop

