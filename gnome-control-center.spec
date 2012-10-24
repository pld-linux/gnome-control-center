#
# Conditional build:
%bcond_with	ibus	# ibus support need not yet released ibus 1.5 or at least devel 1.4.99 version
%bcond_without	systemd # use systemd for session tracking instead of ConsoleKit (fallback to ConsoleKit on runtime)
#
Summary:	GNOME Control Center
Summary(es.UTF-8):	El centro de controle del GNOME
Summary(pl.UTF-8):	Centrum Kontroli GNOME
Summary(pt_BR.UTF-8):	O Centro de Controle do GNOME
Summary(ru.UTF-8):	Центр управления GNOME
Summary(uk.UTF-8):	Центр керування GNOME
Name:		gnome-control-center
Version:	3.6.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-control-center/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	0bb96e62b3803a779832518a841fc769
Patch0:		system-locale-archive-path.patch
Patch1:		configure-gettext.patch
Patch2:		systemd-fallback.patch
Patch3:		krb5.patch
URL:		http://www.gnome.org/
# use libnm-gtk - will use correct NM version
BuildRequires:	NetworkManager-gtk-lib-devel >= 0.9.1.90-2
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	cheese-devel >= 3.6.0
BuildRequires:	clutter-gtk-devel
BuildRequires:	colord-devel >= 0.1.8
BuildRequires:	cups-devel >= 1.4
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.24.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-bluetooth-devel >= 3.6.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 3.6.0
BuildRequires:	gnome-menus-devel >= 3.4.0
BuildRequires:	gnome-online-accounts-devel >= 3.6.0
BuildRequires:	gnome-settings-daemon-devel >= 1:3.6.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.6.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.6.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	heimdal-devel
%{?with_ibus:BuildRequires:	ibus-devel >= 1.4.99}
BuildRequires:	intltool >= 0.40.1
BuildRequires:	iso-codes
BuildRequires:	lcms2-devel
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgtop-devel
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	libpwquality-devel
BuildRequires:	libsocialweb-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libwacom-devel >= 0.6
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.103
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.9.1
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	accountsservice
Requires:	cups-pk-helper
Requires:	desktop-file-utils
Requires:	gnome-settings-daemon >= 1:3.6.0
Requires:	gsettings-desktop-schemas >= 3.6.0
Requires:	hicolor-icon-theme
Suggests:	apg
Suggests:	libcanberra-gnome
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{?with_systemd:%patch2 -p1}
%patch3 -p1

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-update-mimedb \
	--with-libsocialweb \
	%{__enable_disable systemd systemd} \
	%{__enable_disable ibus ibus} \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules - shut up check-files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/*.{a,la}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/gnome-control-center
%attr(755,root,root) %{_bindir}/gnome-sound-applet
%dir %{_libdir}/control-center-1
%dir %{_libdir}/control-center-1/panels
%attr(755,root,root) %{_libdir}/control-center-1/panels/libbackground.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libbluetooth.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libcolor.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdate_time.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libdisplay.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libinfo.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libkeyboard.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libmouse-properties.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libnetwork.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libonline-accounts.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libregion.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libsound.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libpower.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libprinters.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libscreen.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libuniversal-access.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libuser-accounts.so
%attr(755,root,root) %{_libdir}/control-center-1/panels/libwacom-properties.so
%{_sysconfdir}/xdg/autostart/gnome-sound-applet.desktop
%{_sysconfdir}/xdg/menus/gnomecc.menu
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
%{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/gnome-control-center
%{_datadir}/sounds/gnome
%{_datadir}/desktop-directories/*.directory
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop
%{_pixmapsdir}/faces
%{_mandir}/man1/gnome-control-center.1*

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/gnome-keybindings.pc
