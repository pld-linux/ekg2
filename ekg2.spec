#
# Conditional build:
%bcond_with	yesterday_snapshot	# Build most current ekg2 snapshot
					# (must use ./builder -n5 or plain rpmbuild)
%bcond_without	aspell			# build without spell-checking support with aspell
%bcond_without	gadugadu		# don't build gg plugin
%bcond_without	jabber			# don't build jabber plugin
%bcond_without	libgsm			# don't build libgsm plugin
%bcond_without	python			# don't build Python plugin
%bcond_without	sqlite			# don't build logsqlite plugin
%bcond_without	xosd			# don't build xosd plugin

%if %{with yesterday_snapshot}
%define		_snap %(date +%%Y%%m%%d -d yesterday)
%else
%define		_snap 20050129
%endif

Summary:	Multi-protocol instant messaging and chat client
Summary(pl):	Wieloprotoko�owy komunikator internetowy
Name:		ekg2
Version:	1.0
Release:	0.%{_snap}.1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.ekg2.org/archive/%{name}-%{_snap}.tar.gz
# Source0-md5:	66c87ecef5a4643ee364544201b32dc3
URL:		http://www.ekg2.org/
%{?with_aspell:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_jabber:BuildRequires:	expat-devel}
BuildRequires:	gettext-devel
%{?with_jabber:BuildRequires:	gnutls-devel >= 1.0.0}
BuildRequires:	gpm-devel
%{?with_gadugadu:BuildRequires:	libgadu-devel}
%{?with_libgsm:BuildRequires:	libgsm-devel}
%{?with_gadugadu:BuildRequires:	libjpeg-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_python:BuildRequires:	python-devel}
BuildRequires:	sed >= 4.0
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_xosd:BuildRequires:	xosd-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multi-protocol instant messaging and chat client with many plugins.

%description -l pl
Wieloprotoko�owy, otwarty komunikator internetowy z wieloma pluginami.

%package plugin-protocol-gg
Summary:	Gadu-gadu protocol plugin for ekg2
Summary(pl):	Wtyczka protoko�u Gadu-gadu dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-gg
Gadu-gadu protocol plugin for ekg2.

%description plugin-protocol-gg -l pl
Wtyczka protoko�u gadu-gadu dla ekg2.

%package plugin-protocol-gsm
Summary:	GSM VoIP protocol plugin for ekg2
Summary(pl):	Wtyczka protoko�u GSM VoIP dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-gsm
GSM VoIP protocol plugin for ekg2.

%description plugin-protocol-gsm -l pl
Wtyczka protoko�u GSM VoIP dla ekg2.

%package plugin-protocol-irc
Summary:	IRC protocol plugin for ekg2
Summary(pl):	Wtyczka protoko�u IRC dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-irc
IRC protocol plugin for ekg2.

%description plugin-protocol-irc -l pl
Wtyczka protoko�u IRC dla ekg2.

%package plugin-protocol-jabber
Summary:	Jabber protocol plugin for ekg2
Summary(pl):	Wtyczka protoko�u Jabber dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-jabber
Jabber protocol plugin for ekg2.

%description plugin-protocol-jabber -l pl
Wtyczka protoko�u Jabber dla ekg2.

%package plugin-scripting-python
Summary:	Python scripting plugin for ekg2
Summary(pl):	Wtyczka j�zyka Python dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripting-python
Python scripting plugin for ekg2.

%description plugin-scripting-python -l pl
Wtyczka skrypt�w Pythona dla ekg2.

%package plugin-ioctld
Summary:	Ioctld plugin for ekg2
Summary(pl):	Wtyczka ioctld dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ioctld
Ioctld plugin for ekg2 (contains suid root binary!).

%description plugin-ioctld -l pl
Plugin ioctld dla ekg2 (zawiera program z ustawionym suid root!).

%package plugin-logsqlite
Summary:	SQLite log plugin for ekg2
Summary(pl):	Wtyczka logowania do SQLite dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-logsqlite
SQLite log plugin for ekg2.

%description plugin-logsqlite -l pl
Wtyczka logowania do bazy SQLite dla ekg2.

%package plugin-sim
Summary:	Encryption plugin for ekg2
Summary(pl):	Wtyczka szyfruj�ca dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sim
Message encryption plugin for ekg2.

%description plugin-sim -l pl
Wtyczka szyfruj�ca wiadomo�ci dla ekg2.

%package plugin-xosd
Summary:	xosd plugin for ekg2
Summary(pl):	Wtyczka xosd dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xosd
xosd plugin for ekg2.

%description plugin-xosd -l pl
Wtyczka xosd dla ekg2.

%prep
%setup -q -n %{name}-%{_snap}
sed -i -e 's/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/' configure.ac

%build
%{__libtoolize} --ltdl
cd libltdl
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with%{!?with_aspell:out}-aspell \
	--with%{!?with_jabber:out}-expat \
	--with%{!?with_gadugadu:out}-libgadu \
	--with%{!?with_libgsm:out}-libgsm \
	--with%{!?with_python:out}-python \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_xosd:out}-xosd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf docs/{CVS,.cvsignore,Makefile*}
mv -f README README-main

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS* README-main docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/logs.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/mail.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/ncurses.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/pcm.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/rc.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/sms.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/plugins/rc
%{_datadir}/%{name}/plugins/sms
%{_datadir}/%{name}/plugins/logs
%{_datadir}/%{name}/plugins/ncurses

%files plugin-protocol-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gg.so
%{_datadir}/%{name}/plugins/gg

%if %{with libgsm}
%files plugin-protocol-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gsm.so
%endif

%files plugin-protocol-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/irc.so
%{_datadir}/%{name}/plugins/irc

%if %{with jabber}
%files plugin-protocol-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/jabber.so
%{_datadir}/%{name}/plugins/jabber
%endif

%if %{with python}
%files plugin-scripting-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so
# %{_datadir}/%{name}/plugins/jabber
%endif

%files plugin-ioctld
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/ioctld.so
%{_datadir}/%{name}/plugins/ioctld
%attr(4755,root,root) %{_libdir}/ioctld

%if %{with sqlite}
%files plugin-logsqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/logsqlite.so
%{_datadir}/%{name}/plugins/logsqlite
%endif

%files plugin-sim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sim.so
%{_datadir}/%{name}/plugins/sim

%if %{with xosd}
%files plugin-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/xosd.so
%{_datadir}/%{name}/plugins/xosd
%endif
