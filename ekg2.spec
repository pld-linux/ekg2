#
# Conditional build:
%bcond_with	yesterday_snapshot	# Build most current ekg2 snapshot
					# (must use ./builder -n5 or plain rpmbuild)
%bcond_without	aspell			# Don't build in spell-checking support with aspell
%bcond_with	ioctl_daemon		# With (suid-root) ioctl daemon

%if %{with yesterday_snapshot}
%define		_snap %(date +%%Y%%m%%d -d yesterday)
%else
%define		_snap 20040804
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
Source0:	http://www.ekg2.org/archive/%{name}-%{_snap}.tar.gz
# Source0-md5:	88d88568d560eb9e3e9d4836b1fc5d60
URL:		http://www.ekg2.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgadu-devel
BuildRequires:	libtool
BuildRequires:	libltdl-devel
BuildRequires:	libgsm-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	gpm-devel
BuildRequires:	expat-devel
BuildRequires:	libjpeg-devel
%{?with_aspell:BuildRequires:	aspell-devel}
BuildRequires:	gnutls-devel
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
%configure \
	--with%{!?with_aspell:out}-aspell

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf docs/{CVS,.cvsignore,Makefile*}
mv -f README README-main

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS* README-main docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ekg2
%dir %{_libdir}/ekg2/plugins
%attr(755,root,root) %{_libdir}/ekg2/plugins/*.so
%{?with_ioctl_daemon:%attr(4755,root,root) %{_libdir}/ioctld}
