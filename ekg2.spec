%bcond_with	yesterday_snapshot	# Build most current ekg2 snapshot
					# (must use ./builder -n5 or plain rpmbuild)

%if %{with yesterday_snapshot}
%define		_snap %(date +%%Y%%m%%d -d yesterday)
%else
%define		_snap 20040427
%endif

Summary:	A client compatible with Gadu-Gadu
Summary(de):	Einen client kompatibel zu Gadu-Gadu
Summary(it):	Esperimentale cliente di Gadu-Gadu
Summary(pl):	Eksperymentalny Klient Gadu-Gadu
Name:		ekg2
Version:	2.0
Release:	0.%{_snap}.1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dev.null.pl/ekg2/archive/%{name}-%{_snap}.tar.gz
# Source0-md5:	ee1e7993975ae70878bf4a51e2bc2bee
URL:		http://dev.null.pl/ekg2/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgadu-devel
BuildRequires:	libtool
BuildRequires:	libltdl-devel
BuildRequires:	libgsm-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A client compatible with Gadu-Gadu and Jabber.

%description -l de
Einen client kompatibel zu Gadu-Gadu und Jabber.

%description -l it
Esperimentale cliente di Gadu-Gadu.

%description -l pl
Eksperymentalny Klient Gadu-Gadu. W wersji 2.0 obs³uguje zarówno
Gadu-Gadu jak i Jabbera. Planowana tak¿e obs³uga ICQ.

%prep
%setup -q -n %{name}-%{_snap}

%build
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -rf docs/{CVS,.cvsignore,Makefile*}
mv README README-main

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* NEWS* README-main docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ekg2
%dir %{_libdir}/ekg2/plugins
%attr(755,root,root) %{_libdir}/ekg2/plugins/*.so
%{?_with_ioctl_daemon:%attr(4755,root,root) %{_libdir}/ioctld}
