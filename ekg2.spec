%define		_snap 20040411
Summary:	A client compatible with Gadu-Gadu
Summary(de):	Einen client kompatibel zu Gadu-Gadu
Summary(it):	Esperimentale cliente di Gadu-Gadu
Summary(pl):	Eksperymentalny Klient Gadu-Gadu
Name:		ekg2
Version:	2.0
Release:	0.%{_snap}.1
License:	GPL v2+
Group:		Applications/Communications
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	e5a43aa21c15781eff21dda4d602ba28
URL:		http://dev.null.pl/ekg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgadu-devel
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
%setup -q -n %{name}

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
rm -rf docs/{CVS,.cvsignore}
mv $RPM_BUILD_ROOT%{_bindir}/ekg{,2}
mv README README-main

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README-main docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ekg
%dir %{_libdir}/ekg/plugins
%attr(755,root,root) %{_libdir}/ekg/plugins/*.so
%{?_with_ioctl_daemon:%attr(4755,root,root) %{_libdir}/ioctld}
