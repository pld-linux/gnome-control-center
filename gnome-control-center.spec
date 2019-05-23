#
# Conditional build:
%bcond_without	ibus	# IBus support
%bcond_without	wayland	# Wayland support

Summary:	GNOME Control Center
Summary(es.UTF-8):	El centro de controle del GNOME
Summary(pl.UTF-8):	Centrum Kontroli GNOME
Summary(pt_BR.UTF-8):	O Centro de Controle do GNOME
Summary(ru.UTF-8):	Центр управления GNOME
Summary(uk.UTF-8):	Центр керування GNOME
Name:		gnome-control-center
Version:	3.32.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-control-center/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	307d87113d66a9b0cfe15d7b7888ca7e
Patch0:		krb5.patch
URL:		http://www.gnome.org/
BuildRequires:	ModemManager-devel >= 1.0.0
BuildRequires:	NetworkManager-devel >= 1.10.0
# use libnm-gtk - will use correct NM version
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.8.0
BuildRequires:	accountsservice-devel >= 0.6.39
BuildRequires:	cairo-gobject-devel
BuildRequires:	cheese-devel >= 3.28.0
BuildRequires:	colord-devel >= 0.1.34
BuildRequires:	colord-gtk-devel >= 0.1.24
BuildRequires:	cups-devel >= 1.4
BuildRequires:	docbook-dtd42-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.24.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gnome-bluetooth-devel >= 3.18.2
BuildRequires:	gnome-desktop-devel >= 3.28.0
BuildRequires:	gnome-menus-devel >= 3.4.0
BuildRequires:	gnome-online-accounts-devel >= 3.26.0
BuildRequires:	gnome-settings-daemon-devel >= 1:3.26.0
BuildRequires:	grilo-devel >= 0.3.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.31.0
BuildRequires:	gsound-devel
BuildRequires:	gtk+3-devel >= 3.22.20
BuildRequires:	heimdal-devel
%{?with_ibus:BuildRequires:	ibus-devel >= 1.5.2}
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgtop-devel >= 2.0
BuildRequires:	libhandy-devel >= 0.0.9
BuildRequires:	libpwquality-devel >= 1.2.2
BuildRequires:	libsecret-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libwacom-devel >= 0.7
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	meson >= 0.48.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.103
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
%{?with_wayland:BuildRequires:	udev-glib-devel}
BuildRequires:	udisks2-devel >= 2.1.8
BuildRequires:	upower-devel >= 0.99.8
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.2
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.54.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	accountsservice >= 0.6.39
Requires:	cheese-libs >= 3.28.0
Requires:	cups-pk-helper
Requires:	desktop-file-utils
Requires:	glib2 >= 1:2.54.0
Requires:	gnome-bluetooth-libs >= 3.18.2
Requires:	gnome-desktop >= 3.28.0
Requires:	gnome-online-accounts >= 3.26.0
Requires:	gnome-settings-daemon >= 1:3.26.0
Requires:	gsettings-desktop-schemas >= 3.31.0
Requires:	gtk+3 >= 3.22.20
Requires:	hicolor-icon-theme
Requires:	libhandy >= 0.0.9
Requires:	libwacom >= 0.7
Requires:	polkit >= 0.103
Requires:	tzdata
Requires:	udisks2-libs >= 2.1.8
Requires:	upower-libs >= 0.99.8
Suggests:	NetworkManager-applet
Suggests:	cups
Suggests:	gnome-color-manager
Suggests:	libcanberra-gnome
Suggests:	libgnomekbd
# info panel needs glxinfo
Suggests:	mesa-utils
Suggests:	mousetweaks >= 3.0.0
Provides:	control-center = %{epoch}:%{version}-%{release}
Obsoletes:	acme
Obsoletes:	control-center
Obsoletes:	control-center-libs
Obsoletes:	fontilus
Obsoletes:	gnome
Obsoletes:	gnome-control-center-libs
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

%package devel
Summary:	GNOME Control Center development files
Summary(pl.UTF-8):	Pliki programistyczne GNOME Control Center
Group:		X11/Development/Libraries
Provides:	control-center-devel = %{epoch}:%{version}-%{release}
Obsoletes:	control-center-devel
Obsoletes:	gnome-control-center-static

%description devel
GNOME Control Center development files.

%description devel -l pl.UTF-8
Pliki programistyczne GNOME Control Center.

%package -n bash-completion-gnome-control-center
Summary:	bash-completion for gnome-control-center
Summary(pl.UTF-8):	Bashowe uzupełnianie nazw dla gnome-control-center
Group:		Applications/Shells
Requires:	bash-completion >= 2.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-gnome-control-center
bash-completion for gnome-control-center.

%description -n bash-completion-gnome-control-center -l pl.UTF-8
Bashowe uzupełnianie nazw dla gnome-control-center.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	-Ddocumentation=true \
	%{!?with_ibus:-Dibus=false} \
	%{!?with_wayland:-Dwayland=false}

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-control-center
%attr(755,root,root) %{_libexecdir}/cc-remote-login-helper
%attr(755,root,root) %{_libexecdir}/gnome-control-center-search-provider
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.ControlCenter.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnome-control-center-search-provider.ini
%{_datadir}/metainfo/gnome-control-center.appdata.xml
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
%{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/gnome-control-center
%{_datadir}/sounds/gnome
%{_iconsdir}/hicolor/*x*/apps/gnome-power-manager.png
%{_iconsdir}/hicolor/*x*/apps/goa-panel.png
%{_iconsdir}/hicolor/*x*/apps/preferences-color.png
%{_iconsdir}/hicolor/*x*/apps/preferences-desktop-display.png
%{_iconsdir}/hicolor/*x*/apps/preferences-system-time.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Settings.svg
%{_iconsdir}/hicolor/scalable/apps/preferences-color.svg
%{_iconsdir}/hicolor/scalable/apps/preferences-desktop-display.svg
%{_iconsdir}/hicolor/scalable/apps/preferences-system-time.svg
%{_iconsdir}/hicolor/scalable/categories/slideshow-symbolic.svg
%{_iconsdir}/hicolor/scalable/emblems/slideshow-emblem.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Settings-symbolic.svg
%{_desktopdir}/gnome-*-panel.desktop
%{_desktopdir}/gnome-control-center.desktop
%{_pixmapsdir}/faces
%{_mandir}/man1/gnome-control-center.1*

%files devel
%defattr(644,root,root,755)
%{_datadir}/gettext/its/gnome-keybindings.its
%{_datadir}/gettext/its/gnome-keybindings.loc
%{_datadir}/gettext/its/sounds.its
%{_datadir}/gettext/its/sounds.loc
%{_npkgconfigdir}/gnome-keybindings.pc

%files -n bash-completion-gnome-control-center
%defattr(644,root,root,755)
%{bash_compdir}/gnome-control-center
