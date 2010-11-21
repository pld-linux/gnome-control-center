Summary:	GNOME Control Center
Summary(es.UTF-8):	El centro de controle del GNOME
Summary(pl.UTF-8):	Centrum Kontroli GNOME
Summary(pt_BR.UTF-8):	O Centro de Controle do GNOME
Summary(ru.UTF-8):	Центр управления GNOME
Summary(uk.UTF-8):	Центр керування GNOME
Name:		gnome-control-center
Version:	2.91.2
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-control-center/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	2bd94f06e66eba6554a1c5808dc0e1d1
Patch0:		gnome-desktop3.patch
Patch1:		default-apps-chrome-chromium.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop3-devel >= 2.91.2
BuildRequires:	gnome-doc-utils >= 0.12.1
BuildRequires:	gnome-menus-devel >= 2.30.0
BuildRequires:	gnome-settings-daemon-devel >= 2.91.0
BuildRequires:	gtk+3-devel >= 2.91.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgnomekbd-devel >= 2.91.0
BuildRequires:	librsvg-devel >= 2.22.0
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	metacity-devel >= 2:2.26.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	desktop-file-utils
Requires:	gnome-settings-daemon >= 2.91.0
Requires:	libgnomekbd >= 2.91.0
Suggests:	libcanberra-gnome
Suggests:	mousetweaks >= 2.24.0
Provides:	control-center = %{epoch}:%{version}-%{release}
Obsoletes:	acme
Obsoletes:	control-center
Obsoletes:	fontilus
Obsoletes:	gnome
Obsoletes:	gnome-media-volume-control
Obsoletes:	themus
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Configuration tool for easily setting up your GNOME environment.

%description -l es.UTF-8
El control-center es una herramienta para una configuración facilitada
el entorno GNOME.

%description -l pl.UTF-8
Narzędzie do łatwej konfiguracji środowiska GNOME.

%description -l pt_BR.UTF-8
O Control Center é uma ferramenta para facilmente configurar seu
ambiente GNOME.

%description -l ru.UTF-8
Пакет Control Center содержит утилиты, позволяющие настраивать среду
GNOME вашей системы (такие вещи как фон рабочего стола и темы,
программа сохранения экрана, оконный менеджер, системные звуки,
поведение мыши и др.)

Этот пакет нужен, если вы устанавливаете среду GNOME.

%description -l uk.UTF-8
Пакет Control Center містить утиліти, які дозволяють настроювати
середовище GNOME вашої системи (такі речі як фон робочого столу та
теми, програма збереження екрану, віконний менеджер, системні звуки,
поведінка миші та ін.)

Цей пакет потрібний, якщо ви встановлюєте середовище GNOME.

%package libs
Summary:	GNOME Control Center gnome-window-settings library
Summary(pl.UTF-8):	Biblioteka Control Center gnome-window-settings
Group:		X11/Libraries
Provides:	control-center-libs = %{epoch}:%{version}-%{release}
Obsoletes:	control-center-libs

%description libs
This package contains gnome-window-settings library.

%description libs -l pl.UTF-8
Pakiet ten zawiera bibliotekę gnome-window-settings.

%package devel
Summary:	GNOME Control Center header files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek GNOME Control Center
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gnome-desktop3-devel >= 2.91.2
Requires:	gtk+3-devel >= 2.91.0
Provides:	control-center-devel = %{epoch}:%{version}-%{release}
Obsoletes:	control-center-devel

%description devel
GNOME Control-Center header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek GNOME Control Center.

%package static
Summary:	GNOME Control Center static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNOME Control Center
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	control-center-static = %{epoch}:%{version}-%{release}
Obsoletes:	control-center-static

%description static
GNOME Control Center static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNOME Control Center.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-update-mimedb \
	--with-html-dir=%{_gtkdocdir} \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# no static modules - shut up check-files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/*.{a,la}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install control-center.schemas
%gconf_schema_install fontilus.schemas
%gconf_schema_install gnome-control-center.schemas
%scrollkeeper_update_post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall	control-center.schemas
%gconf_schema_uninstall fontilus.schemas
%gconf_schema_uninstall gnome-control-center.schemas

%postun
%scrollkeeper_update_postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/gnome-at-mobility
%attr(755,root,root) %{_bindir}/gnome-at-visual
%attr(755,root,root) %{_bindir}/gnome-control-center
%attr(755,root,root) %{_bindir}/gnome-sound-applet
%dir %{_libdir}/control-center-1
%dir %{_libdir}/control-center-1/panels/
%attr(755,root,root) %{_libdir}/control-center-1/panels/libbackground.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdate_time.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdefault-applications.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdisplay.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libkeyboard.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libmouse-properties.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libnetwork.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libregion.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libsound.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libuniversal-access.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libuser-accounts.so
%{_sysconfdir}/gconf/schemas/gnome-control-center.schemas
%{_sysconfdir}/xdg/autostart/gnome-at-session.desktop
%{_sysconfdir}/xdg/autostart/gnome-sound-applet.desktop
%{_sysconfdir}/xdg/menus/gnomecc.menu
%{_datadir}/gnome-control-center
%{_datadir}/sounds/gnome
%{_datadir}/desktop-directories/*.directory
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-control-center.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-control-center.so.1

%files devel
%defattr(644,root,root,755)
%{_gtkdocdir}/libgnome-control-center
%attr(755,root,root) %{_libdir}/libgnome-control-center.so
%{_includedir}/gnome-control-center-1
%{_datadir}/pkgconfig/gnome-default-applications.pc
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_pkgconfigdir}/libgnome-control-center.pc

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libgnome-window-settings.a
