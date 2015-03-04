#
# Conditional build:
%bcond_without	ibus	# ibus support

Summary:	GNOME Control Center
Summary(es.UTF-8):	El centro de controle del GNOME
Summary(pl.UTF-8):	Centrum Kontroli GNOME
Summary(pt_BR.UTF-8):	O Centro de Controle do GNOME
Summary(ru.UTF-8):	Центр управления GNOME
Summary(uk.UTF-8):	Центр керування GNOME
Name:		gnome-control-center
Version:	3.14.2
Release:	2
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-control-center/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	729951bfecc3f5fa87973383ec4ab787
Patch0:		krb5.patch
URL:		http://www.gnome.org/
BuildRequires:	ModemManager-devel >= 1.0.0
# use libnm-gtk - will use correct NM version
BuildRequires:	NetworkManager-gtk-lib-devel >= 0.9.8
BuildRequires:	OpenGL-devel
BuildRequires:	accountsservice-devel >= 0.6.30
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	cheese-devel >= 3.6.0
BuildRequires:	clutter-gtk-devel
BuildRequires:	colord-devel >= 0.1.34
BuildRequires:	colord-gtk-devel >= 0.1.24
BuildRequires:	cups-devel >= 1.4
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.24.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-bluetooth-devel >= 3.12.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 3.12.0
BuildRequires:	gnome-menus-devel >= 3.4.0
BuildRequires:	gnome-online-accounts-devel >= 3.10.0
BuildRequires:	gnome-settings-daemon-devel >= 1:3.8.0
BuildRequires:	grilo-devel >= 0.2.6
BuildRequires:	gsettings-desktop-schemas-devel >= 3.14.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	heimdal-devel
%{?with_ibus:BuildRequires:	ibus-devel >= 1.5.2}
BuildRequires:	intltool >= 0.40.1
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgtop-devel
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	libpwquality-devel >= 1.2.2
BuildRequires:	libsmbclient-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libwacom-devel >= 0.7
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.103
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	xorg-lib-libXi-devel >= 1.2
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	accountsservice
Requires:	cups-pk-helper
Requires:	desktop-file-utils
Requires:	glib2 >= 1:2.40.0
Requires:	gnome-desktop >= 3.12.0
Requires:	gnome-settings-daemon >= 1:3.8.0
Requires:	gsettings-desktop-schemas >= 3.14.0
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
Requires:	tzdata
Suggests:	libcanberra-gnome
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
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-update-mimedb \
	%{__enable_disable ibus ibus} \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/gnome-control-center
%attr(755,root,root) %{_libdir}/cc-remote-login-helper
%attr(755,root,root) %{_libdir}/gnome-control-center-search-provider
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-control-center-search-provider.ini
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
%{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/gnome-control-center
%{_datadir}/sounds/gnome
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop
%{_pixmapsdir}/faces
%{_mandir}/man1/gnome-control-center.1*

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/gnome-keybindings.pc

%files -n bash-completion-gnome-control-center
%defattr(644,root,root,755)
%{bash_compdir}/gnome-control-center
