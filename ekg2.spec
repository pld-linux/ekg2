#
# Conditional build:
%bcond_with	yesterday_snapshot	# Build most current ekg2 snapshot
					# (must use ./builder -n5 or plain rpmbuild)
%bcond_without	gadugadu		# Don't build gg plugin
%bcond_without	jabber			# Don't build jabber plugin
%bcond_without	aspell			# Don't build in spell-checking support with aspell
%bcond_without	sqlite			# Don't build logsqlite plugin
%bcond_without	python			# Don't build Python plugin
%bcond_without	libgsm			# Don't build libgsm plugin
%bcond_without	xosd			# Don't build xosd plugin

%if %{with yesterday_snapshot}
%define		_snap %(date +%%Y%%m%%d -d yesterday)
%else
%define		_snap 20050129
%endif

Summary:	Multi-protocol instant messaging and chat client
Summary(pl):	Wieloprotoko³owy komunikator internetowy
Name:		ekg2
Version:	1.0
Release:	0.%{_snap}.1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.ekg2.org/archive/%{name}-%{_snap}.tar.gz
# Source0-md5:	66c87ecef5a4643ee364544201b32dc3
URL:		http://www.ekg2.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gpm-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	sed >= 4.0
%{?with_gadugadu:BuildRequires:	libgadu-devel}
%{?with_gadugadu:BuildRequires:	libjpeg-devel}
%{?with_jabber:BuildRequires:	expat-devel}
%{?with_jabber:BuildRequires:	gnutls-devel >= 1.0.0}
%{?with_aspell:BuildRequires:	aspell-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_python:BuildRequires:	python-devel}
%{?with_libgsm:BuildRequires:	libgsm-devel}
%{?with_xosd:BuildRequires:	xosd-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multi-protocol instant messaging and chat client with many plugins.

%description -l pl
Wieloprotoko³owy, otwarty komunikator internetowy z wieloma pluginami.

%if %{with gadugadu}
%package plugin-protocol-gg
Summary:	Gadu-gadu protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u Gadu-gadu dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-protocol-gg
Gadu-gadu protocol plugin for ekg2.

%description plugin-protocol-gg -l pl
Wtyczka protoko³u gadu-gadu dla ekg2.
%endif

%if %{with jabber}
%package plugin-protocol-jabber
Summary:	Jabber protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u Jabber dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-protocol-jabber
Jabber protocol plugin for ekg2.

%description plugin-protocol-jabber -l pl
Wtyczka protoko³u Jabber dla ekg2.
%endif


%package plugin-protocol-irc
Summary:	IRC protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u IRC dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-protocol-irc
IRC protocol plugin for ekg2.

%description plugin-protocol-irc -l pl
Wtyczka protoko³u IRC dla ekg2.


%if %{with libgsm}
%package plugin-protocol-gsm
Summary:	GSM VoIP protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u GSM VoIP dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-protocol-gsm
GSM VoIP protocol plugin for ekg2.

%description plugin-protocol-gsm -l pl
Wtyczka protoko³u GSM VoIP dla ekg2.
%endif


%if %{with python}
%package plugin-scripting-python
Summary:	Python scripting plugin for ekg2
Summary(pl):	Wtyczka jêzyka Python dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-scripting-python
Python scripting plugin for ekg2.

%description plugin-scripting-python -l pl
Wtyczka skryptów Pythona dla ekg2.
%endif


%package plugin-sim
Summary:	Encryption plugin for ekg2
Summary(pl):	Wtyczka szyfruj±ca dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-sim
Message encryption plugin for ekg2.

%description plugin-sim -l pl
Wtyczka szyfruj±ca wiadomo¶ci dla ekg2.


%package plugin-ioctld
Summary:	Ioctld plugin for ekg2
Summary(pl):	Wtyczka ioctld dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-ioctld
Ioctld plugin for ekg2 (contains suid binary!)

%description plugin-ioctld -l pl
Plugin ioctld dla ekg2 (zawiera program z ustawionym suid!)


%if %{with sqlite}
%package plugin-logsqlite
Summary:	SQLite log plugin for ekg2
Summary(pl):	Wtyczka logowania do SQLite dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-logsqlite
SQLite log plugin for ekg2.

%description plugin-logsqlite -l pl
Wtyczka logowania do bazy SQLite dla ekg2.
%endif


%if %{with xosd}
%package plugin-xosd
Summary:	xosd plugin for ekg2
Summary(pl):	Wtyczka xosd dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description plugin-xosd
xosd plugin for ekg2.

%description plugin-xosd -l pl
Wtyczka xosd dla ekg2.
%endif


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
	--with%{!?with_gadugadu:out}-libgadu \
	--with%{!?with_jabber:out}-expat \
	--with%{!?with_aspell:out}-aspell \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_python:out}-python \
	--with%{!?with_libgsm:out}-libgsm \
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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/logs.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/mail.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/ncurses.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/pcm.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/rc.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/sms.so
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/plugins/rc
%{_datadir}/%{name}/plugins/sms
%{_datadir}/%{name}/plugins/logs
%{_datadir}/%{name}/plugins/ncurses

%if %{with gadugadu}
%files plugin-protocol-gg
%attr(755,root,root) %{_libdir}/%{name}/plugins/gg.so
%{_datadir}/%{name}/plugins/gg
%endif

%if %{with jabber}
%files plugin-protocol-jabber
%attr(755,root,root) %{_libdir}/%{name}/plugins/jabber.so
%{_datadir}/%{name}/plugins/jabber
%endif

%files plugin-protocol-irc
%attr(755,root,root) %{_libdir}/%{name}/plugins/irc.so
%{_datadir}/%{name}/plugins/irc

%if %{with libgsm}
%files plugin-protocol-gsm
%attr(755,root,root) %{_libdir}/%{name}/plugins/gsm.so
%endif

%if %{with python}
%files plugin-scripting-python
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so
# %{_datadir}/%{name}/plugins/jabber
%endif

%files plugin-sim
%attr(755,root,root) %{_libdir}/%{name}/plugins/sim.so
%{_datadir}/%{name}/plugins/sim

%files plugin-ioctld
%attr(755,root,root) %{_libdir}/%{name}/plugins/ioctld.so
%{_datadir}/%{name}/plugins/ioctld
%attr(4755,root,root) %{_libdir}/ioctld

%if %{with sqlite}
%files plugin-logsqlite
%attr(755,root,root) %{_libdir}/%{name}/plugins/logsqlite.so
%{_datadir}/%{name}/plugins/logsqlite
%endif

%if %{with xosd}
%files plugin-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/xosd.so
%{_datadir}/%{name}/plugins/xosd
%endif
