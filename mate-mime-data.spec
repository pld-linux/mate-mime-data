# NOTE: this package is deprecated, meant for MATE <= 1.4 compatibility only
Summary:	MIME and Application database for MATE Desktop
Summary(pl.UTF-8):	Baza danych MIME i aplikacji dla środowiska MATE Desktop
Name:		mate-mime-data
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	61e3706c1c7b7e9703cabba1e543099b
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.2.3
BuildRequires:	intltool >= 0.35
BuildRequires:	rpmbuild(macros) >= 1.446
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the base MIME and Application database for MATE.
It is meant to be accessed through the MIME functions in MateVFS.

%description -l pl.UTF-8
Ten pakiet zawiera podstawowe bazy danych MIME oraz aplikacji dla
MATE. Przeznaczony jest do udostępniania przez funkcje MIME w MateVFS.

%package devel
Summary:	Development files for mate-mime-data
Summary(pl.UTF-8):	Pliki potrzebne przy tworzeniu programów używajacych mate-mime-data
Group:		X11/Development/Libraries
# doesn't require base

%description devel
Developmet files for mate-mime-data.

%description devel -l pl.UTF-8
Pliki potrzebne przy tworzeniu programów używajacych mate-mime-data.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man5

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/mate-vfs-mime.5 $RPM_BUILD_ROOT%{_mandir}/man5/mate-vfs-mime.5

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{sr@ije,sr@ijekavian}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_sysconfdir}/mate-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info
%{_mandir}/man5/mate-vfs-mime.5*

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/mate-mime-data-2.0.pc
