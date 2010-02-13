Summary:	GNOME Control Center
Summary(es.UTF-8):	El centro de controle del GNOME
Summary(pl.UTF-8):	Centrum Kontroli GNOME
Summary(pt_BR.UTF-8):	O Centro de Controle do GNOME
Summary(ru.UTF-8):	Центр управления GNOME
Summary(uk.UTF-8):	Центр керування GNOME
Name:		gnome-control-center
Version:	2.29.90
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-control-center/2.29/%{name}-%{version}.tar.bz2
# Source0-md5:	87e8f65cecb6ae8ed6d4607100f2753a
Patch0:		no_update_desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.19.7
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 2.29.90
BuildRequires:	gnome-doc-utils >= 0.12.1
BuildRequires:	gnome-menus-devel >= 2.25.90
BuildRequires:	gnome-settings-daemon-devel >= 2.26.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel >= 0.4
BuildRequires:	libgnomekbd-devel >= 2.28.0
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
Requires:	gnome-settings-daemon >= 2.26.0
Suggests:	libcanberra-gnome
Suggests:	mousetweaks >= 2.24.0
Provides:	control-center = %{epoch}:%{version}-%{release}
Obsoletes:	acme
Obsoletes:	control-center
Obsoletes:	fontilus
Obsoletes:	gnome
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
Requires:	gnome-desktop-libs >= 2.29.90
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
Requires:	gnome-desktop-devel >= 2.29.90
Requires:	gtk+2-devel >= 2:2.18.0
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
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-update-mimedb \
	--disable-update-desktop \
	--enable-aboutme \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.{a,la}

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
%attr(755,root,root) %{_bindir}/gnome-about-me
%attr(755,root,root) %{_bindir}/gnome-appearance-properties
%attr(755,root,root) %{_bindir}/gnome-at-mobility
%attr(755,root,root) %{_bindir}/gnome-at-properties
%attr(755,root,root) %{_bindir}/gnome-at-visual
%attr(755,root,root) %{_bindir}/gnome-control-center
%attr(755,root,root) %{_bindir}/gnome-default-applications-properties
%attr(755,root,root) %{_bindir}/gnome-display-properties
%attr(755,root,root) %{_bindir}/gnome-font-viewer
%attr(755,root,root) %{_bindir}/gnome-keybinding-properties
%attr(755,root,root) %{_bindir}/gnome-keyboard-properties
%attr(755,root,root) %{_bindir}/gnome-mouse-properties
%attr(755,root,root) %{_bindir}/gnome-network-properties
%attr(755,root,root) %{_bindir}/gnome-thumbnail-font
%attr(755,root,root) %{_bindir}/gnome-typing-monitor
%attr(755,root,root) %{_bindir}/gnome-window-properties
%dir %{_libdir}/window-manager-settings
%attr(755,root,root) %{_libdir}/window-manager-settings/libmetacity.so
%{_sysconfdir}/gconf/schemas/control-center.schemas
%{_sysconfdir}/gconf/schemas/fontilus.schemas
%{_sysconfdir}/gconf/schemas/gnome-control-center.schemas
%{_sysconfdir}/xdg/autostart/gnome-at-session.desktop
%{_sysconfdir}/xdg/menus/gnomecc.menu
%{_datadir}/gnome-control-center
%{_datadir}/desktop-directories/*.directory
%{_datadir}/gnome/cursor-fonts
%{_datadir}/mime/packages/gnome-theme-package.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-window-settings.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnome-window-settings.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-window-settings.so
%{_libdir}/libgnome-window-settings.la
%{_includedir}/gnome-window-settings-2.0
%{_pkgconfigdir}/gnome-window-settings-2.0.pc
%{_datadir}/pkgconfig/gnome-default-applications.pc
%{_datadir}/pkgconfig/gnome-keybindings.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnome-window-settings.a
