#
# Conditional build:
%bcond_with	yesterday_snapshot	# Build most current ekg2 snapshot
					# (must use ./builder -n5 or plain rpmbuild)
%bcond_without	aspell			# build without spell-checking support with aspell
%bcond_without	gadugadu		# don't build gg plugin
%bcond_without	jabber			# don't build jabber plugin
%bcond_without	gnutls			# build jabber plugin without libgnutls
%bcond_without	libgsm			# don't build libgsm plugin
%bcond_without	python			# don't build Python plugin
%bcond_without	perl			# don't build Perl plugin
%bcond_without	sqlite			# don't build logsqlite plugin based on sqlite (conflicts with sqlite3)
%bcond_with	sqlite3			# build logsqlite plugin based on sqlite3
%bcond_without	xosd			# don't build xosd plugin
%bcond_without  gtk			# don't build gtk plugin

%if %{with yesterday_snapshot}
%define		_snap %(date +%%Y%%m%%d -d yesterday)
%else
%define		_snap 20060625
%endif

%if %{without jabber}
%undefine with_gnutls
%endif

%if %{with sqlite3}
%undefine sqlite
%endif

Summary:	Multi-protocol instant messaging and chat client
Summary(pl):	Wieloprotoko³owy komunikator internetowy
Name:		ekg2
Version:	1.0
Release:	0.%{_snap}.1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dev.null.pl/ekg2/%{name}-%{_snap}.tar.gz
# Source0-md5:	9c4bf2a697472a88b1dddd8252047400
Patch0:		%{name}-perl-install.patch
Patch1:		%{name}-no_scripts.patch
URL:		http://dev.null.pl/ekg2/
%{?with_aspell:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_jabber:BuildRequires:	expat-devel}
BuildRequires:	gettext-devel
%{?with_gnutls:BuildRequires:	gnutls-devel >= 1.2.5}
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+2-devel}
%{?with_gadugadu:BuildRequires:	libgadu-devel}
%{?with_libgsm:BuildRequires:	libgsm-devel}
%{?with_gadugadu:BuildRequires:	libjpeg-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel}
%{?with_python:BuildRequires:   python}
%{?with_perl:BuildRequires:	perl-devel}
%{?with_perl:BuildRequires:	rpm-perlprov}

BuildRequires:	sed >= 4.0
%{?with_xosd:BuildRequires:	xosd-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
%{?with_gtk:BuildRequires:	gtk+2-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multi-protocol instant messaging and chat client with many plugins.

%description -l pl
Wieloprotoko³owy, otwarty komunikator internetowy z wieloma pluginami.

%package plugin-protocol-gg
Summary:	Gadu-gadu protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u Gadu-gadu dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-gg
Gadu-gadu protocol plugin for ekg2.

%description plugin-protocol-gg -l pl
Wtyczka protoko³u gadu-gadu dla ekg2.

%package plugin-protocol-gsm
Summary:	GSM VoIP protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u GSM VoIP dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-gsm
GSM VoIP protocol plugin for ekg2.

%description plugin-protocol-gsm -l pl
Wtyczka protoko³u GSM VoIP dla ekg2.

%package plugin-protocol-irc
Summary:	IRC protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u IRC dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-irc
IRC protocol plugin for ekg2.

%description plugin-protocol-irc -l pl
Wtyczka protoko³u IRC dla ekg2.

%package plugin-protocol-jabber
Summary:	Jabber protocol plugin for ekg2
Summary(pl):	Wtyczka protoko³u Jabber dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-jabber
Jabber protocol plugin for ekg2.

%description plugin-protocol-jabber -l pl
Wtyczka protoko³u Jabber dla ekg2.

%package plugin-scripting-python
Summary:	Python scripting plugin for ekg2
Summary(pl):	Wtyczka jêzyka Python dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripting-python
Python scripting plugin for ekg2.

%description plugin-scripting-python -l pl
Wtyczka skryptów Pythona dla ekg2.

%package plugin-scripting-perl
Summary:	Perl scripting plugin for ekg2
Summary(pl):	Wtyczka jêzyka Perl dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripting-perl
Python scripting Perl for ekg2.

%description plugin-scripting-perl -l pl
Wtyczka skryptów Perla dla ekg2.

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
%if %{with sqlite3}
Requires:	sqlite3
%else
Requires:	sqlite
%endif

%description plugin-logsqlite
SQLite log plugin for ekg2.

%description plugin-logsqlite -l pl
Wtyczka logowania do bazy SQLite dla ekg2.

%package plugin-readline
Summary:	readline
Summary(pl):	readline
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-readline
readline

%description plugin-readline -l pl
readline

%package plugin-sim
Summary:	Encryption plugin for ekg2
Summary(pl):	Wtyczka szyfruj±ca dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sim
Message encryption plugin for ekg2.

%description plugin-sim -l pl
Wtyczka szyfruj±ca wiadomo¶ci dla ekg2.

%package plugin-xosd
Summary:	xosd plugin for ekg2
Summary(pl):	Wtyczka xosd dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xosd
xosd plugin for ekg2.

%description plugin-xosd -l pl
Wtyczka xosd dla ekg2.

%package plugin-gtk
Summary:	gtk plugin for ekg2
Summary(pl):	Wtyczka gtk dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2

%description plugin-gtk
gtk plugin for ekg2.

%description plugin-gtk -l pl
Wtyczka gtk dla ekg2.

%package devel
Summary:	ekg2 header files
Summary(pl):	Pliki nag³ówkowe ekg2
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for ekg2.

%description devel -l pl
Pliki nag³ówkowe ekg2.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
sed -i -e 's/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/' configure.ac
sed -i -e '\#/opt/sqlite/lib#s#"$# /usr/lib64"#' m4/sqlite.m4
sed -i -e '/mkinstalldirs/s/=.*/= $(MKINSTALLDIRS)/' po/Makefile.in.in

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
	--with%{!?with_gnutls:out}-libgnutls \
	--with%{!?with_gadugadu:out}-libgadu \
	--with%{!?with_libgsm:out}-libgsm \
	--with%{!?with_python:out}-python \
	--with%{!?with_xosd:out}-xosd \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_sqlite3:out}-sqlite3 \
	--with%{!?with_gtk:out}-gtk

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
%attr(755,root,root) %{_bindir}/ekg2
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
%dir %{_datadir}/%{name}/scripts

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
%{_datadir}/%{name}/scripts/*.py
%endif

%if %{with perl}
%files plugin-scripting-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/perl.so
%{perl_vendorarch}/Ekg2.pm
%dir %{perl_vendorarch}/Ekg2
%{perl_vendorarch}/Ekg2/Irc.pm
%dir %{perl_vendorarch}/auto/Ekg2
%{perl_vendorarch}/auto/Ekg2/Ekg2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Ekg2/Ekg2.so
%dir %{perl_vendorarch}/auto/Ekg2/Irc
%{perl_vendorarch}/auto/Ekg2/Irc/Irc.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Ekg2/Irc/Irc.so
%{_datadir}/%{name}/scripts/*.pl
%endif

%files plugin-ioctld
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/ioctld.so
%{_datadir}/%{name}/plugins/ioctld
%attr(4755,root,root) %{_libexecdir}/ioctld

%if %{with sqlite} || %{with sqlite3}
%files plugin-logsqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/logsqlite.so
%{_datadir}/%{name}/plugins/logsqlite
%endif

%files plugin-readline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/readline.so
%{_datadir}/%{name}/plugins/readline

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

%if %{with gtk}
%files plugin-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gtk.so
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ekg2-config
%{_includedir}/ekg2
