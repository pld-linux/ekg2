#
# Conditional build:
%bcond_with	yesterday_snapshot	# Build most current ekg2 snapshot
					# (must use ./builder -n5 or plain rpmbuild)
%bcond_without	aspell			# build without spell-checking support with aspell
%bcond_without	feed			# don't build feed plugin
%bcond_without	gadugadu		# don't build gg plugin
%bcond_without	gpg			# don't build gpg plugin
%bcond_without	gtk			# don't build gtk plugin
%bcond_without	jabber			# don't build jabber plugin
%bcond_without	gnutls			# build jabber plugin without libgnutls
%bcond_without	libgsm			# don't build libgsm plugin
%bcond_without	perl			# don't build Perl plugin
%bcond_without	python			# don't build Python plugin
%bcond_without	readline		# don't build readline interface
%bcond_with	sqlite			# build logsqlite plugin based on sqlite (conflicts with sqlite3)
%bcond_without	sqlite3			# don't build logsqlite plugin based on sqlite3
%bcond_without	xosd			# don't build xosd plugin

%if %{without yesterday_snapshot}
%define		_snap 0.1.1
%define		_ver 0.1.1
%define		_tarballformat gz
%else
%define		_snap %(date +%%Y%%m%%d -d yesterday)
%define		_ver 0.0.%{_snap}
%define		_tarballformat bz2
%endif

%if %{without jabber}
%undefine with_gnutls
%endif

%if %{with sqlite}
%undefine sqlite3
%endif

Summary:	Multi-protocol instant messaging and chat client
Summary(pl.UTF-8):	Wieloprotokołowy komunikator internetowy
Name:		ekg2
Version:	%{_ver}
Release:	5
Epoch:		2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://pl.ekg2.org/%{name}-%{_snap}.tar.%{_tarballformat}
# Source0-md5:	8c64ab909687b9ac3798caa7736d7b2a
Patch0:		%{name}-perl-install.patch
#Patch1:	%{name}-no_scripts.patch
Patch2:		%{name}-missing-xwcslen.patch
URL:		http://ekg2.org/
%{?with_aspell:BuildRequires:	aspell-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with feed} || %{with jabber}
BuildRequires:	expat-devel
%endif
BuildRequires:	gettext-devel
%{?with_gadugadu:BuildRequires:	giflib-devel}
%{?with_gnutls:BuildRequires:	gnutls-devel >= 1.2.5}
%{?with_gpg:BuildRequires:	gpgme-devel}
BuildRequires:	gpm-devel
%{?with_gtk:BuildRequires:	gtk+2-devel}
%{?with_gadugadu:BuildRequires:	libgadu-devel}
%{?with_libgsm:BuildRequires:	libgsm-devel}
%{?with_gadugadu:BuildRequires:	libjpeg-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel}
%{?with_readline:BuildRequires:	readline-devel}
%{?with_perl:BuildRequires:	rpm-perlprov}
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	sed >= 4.0
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
%{?with_xosd:BuildRequires:	xosd-devel}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multi-protocol instant messaging and chat client with many plugins.

%description -l pl.UTF-8
Wieloprotokołowy, otwarty komunikator internetowy z wieloma wtyczkami.

%package devel
Summary:	ekg2 header files
Summary(pl.UTF-8):	Pliki nagłówkowe ekg2
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for ekg2.

%description devel -l pl.UTF-8
Pliki nagłówkowe ekg2.

%package plugin-feed
Summary:	feed plugin for ekg2
Summary(pl.UTF-8):	Wtyczka feed dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-feed
feed plugin for ekg2.

%description plugin-feed -l pl.UTF-8
Wtyczka feed dla ekg2.

%package plugin-gpg
Summary:	gpg plugin for ekg2
Summary(pl.UTF-8):	Wtyczka gpg dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gpg
gpg plugin for ekg2.

%description plugin-gpg -l pl.UTF-8
Wtyczka gpg dla ekg2.

%package plugin-gtk
Summary:	gtk plugin for ekg2
Summary(pl.UTF-8):	Wtyczka gtk dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2

%description plugin-gtk
gtk plugin for ekg2.

%description plugin-gtk -l pl.UTF-8
Wtyczka gtk dla ekg2.

%package plugin-ioctld
Summary:	Ioctld plugin for ekg2
Summary(pl.UTF-8):	Wtyczka ioctld dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ioctld
Ioctld plugin for ekg2 (contains suid root binary!).

%description plugin-ioctld -l pl.UTF-8
Wtyczka ioctld dla ekg2 (zawiera program z ustawionym suid root!).

%package plugin-jogger
Summary:	Jogger plugin for ekg2
Summary(pl.UTF-8):	Wtyczka jogger dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-jogger
Jogger plugin for ekg2.

%description plugin-jogger -l pl.UTF-8
Wtyczka jogger dla ekg2.

%package plugin-logsqlite
Summary:	SQLite log plugin for ekg2
Summary(pl.UTF-8):	Wtyczka logowania do SQLite dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
%if %{with sqlite3}
Requires:	sqlite3
%else
Requires:	sqlite
%endif

%description plugin-logsqlite
SQLite log plugin for ekg2.

%description plugin-logsqlite -l pl.UTF-8
Wtyczka logowania do bazy SQLite dla ekg2.

%package plugin-protocol-gg
Summary:	Gadu-gadu protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu Gadu-gadu dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-gg
Gadu-gadu protocol plugin for ekg2.

%description plugin-protocol-gg -l pl.UTF-8
Wtyczka protokołu gadu-gadu dla ekg2.

%package plugin-protocol-gsm
Summary:	GSM VoIP protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu GSM VoIP dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-gsm
GSM VoIP protocol plugin for ekg2.

%description plugin-protocol-gsm -l pl.UTF-8
Wtyczka protokołu GSM VoIP dla ekg2.

%package plugin-protocol-irc
Summary:	IRC protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu IRC dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-irc
IRC protocol plugin for ekg2.

%description plugin-protocol-irc -l pl.UTF-8
Wtyczka protokołu IRC dla ekg2.

%package plugin-protocol-jabber
Summary:	Jabber protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu Jabber dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-jabber
Jabber protocol plugin for ekg2.

%description plugin-protocol-jabber -l pl.UTF-8
Wtyczka protokołu Jabber dla ekg2.

%package plugin-protocol-polchat
Summary:	Polchat protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu polchat dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-polchat
Polchat protocol plugin for ekg2.

%description plugin-protocol-polchat -l pl.UTF-8
Wtyczka protokołu polchat dla ekg2.

%package plugin-readline
Summary:	readline interface
Summary(pl.UTF-8):	Interfejs readline
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-readline
readline interface.

%description plugin-readline -l pl.UTF-8
Interfejs readline.

%package plugin-scripting-perl
Summary:	Perl scripting plugin for ekg2
Summary(pl.UTF-8):	Wtyczka języka Perl dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripting-perl
Python scripting Perl for ekg2.

%description plugin-scripting-perl -l pl.UTF-8
Wtyczka skryptów Perla dla ekg2.

%package plugin-scripting-python
Summary:	Python scripting plugin for ekg2
Summary(pl.UTF-8):	Wtyczka języka Python dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripting-python
Python scripting plugin for ekg2.

%description plugin-scripting-python -l pl.UTF-8
Wtyczka skryptów Pythona dla ekg2.

%package plugin-sim
Summary:	Encryption plugin for ekg2
Summary(pl.UTF-8):	Wtyczka szyfrująca dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sim
Message encryption plugin for ekg2.

%description plugin-sim -l pl.UTF-8
Wtyczka szyfrująca wiadomości dla ekg2.

%package plugin-xosd
Summary:	xosd plugin for ekg2
Summary(pl.UTF-8):	Wtyczka xosd dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xosd
xosd plugin for ekg2.

%description plugin-xosd -l pl.UTF-8
Wtyczka xosd dla ekg2.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
#%patch1 -p1
%patch2 -p1
sed -i -e 's/AC_LIBLTDL_CONVENIENCE/AC_LIBLTDL_INSTALLABLE/' configure.ac
sed -i -e '\#/opt/sqlite/lib#s#"$# /usr/lib64"#' m4/sqlite.m4

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
# for hostent.h_addr (should be in CPPFLAGS, but it's overridden in plugins/jabber)
CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
%configure \
	--enable-unicode \
	--with%{!?with_aspell:out}-aspell \
	--with%{!?with_gadugadu:out}-libgadu \
	%{!?with_gpg:--without-gpg} \
	--with%{!?with_gtk:out}-gtk \
	--with%{!?with_gnutls:out}-libgnutls \
%if %{with feed} || %{with jabber}
		--with-expat \
%else
		--without-expat \
%endif
	--with%{!?with_libgsm:out}-libgsm \
	%{!?with_perl:--without-perl} \
	--with%{!?with_python:out}-python \
	--with%{!?with_readline:out}-readline \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_sqlite3:out}-sqlite3 \
	--with%{!?with_xosd:out}-xosd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f README README-main || true

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS* README-main docs/ekg2book* docs/README docs/TODO docs/*.txt
%attr(755,root,root) %{_bindir}/ekg2
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/autoresponder.so
%{_datadir}/%{name}/plugins/autoresponder
%attr(755,root,root) %{_libdir}/%{name}/plugins/httprc_xajax.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/logs.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/mail.so
%{_datadir}/%{name}/plugins/mail
%attr(755,root,root) %{_libdir}/%{name}/plugins/ncurses.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/pcm.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/rc.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/rot13.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/sms.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/xmsg.so
%{_datadir}/%{name}/plugins/xmsg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/plugins/httprc_xajax
%{_datadir}/%{name}/plugins/logs
%{_datadir}/%{name}/plugins/ncurses
%{_datadir}/%{name}/plugins/rc
%{_datadir}/%{name}/plugins/sms
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}/themes

%if %{without yesterday_snapshot}
%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ekg2-config
%{_includedir}/ekg2
%endif

%if %{with yesterday_snapshot}
%files plugin-feed
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/feed.so
%endif

%if %{with gpg}
%files plugin-gpg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gpg.so
%endif

%if %{with gtk}
%files plugin-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gtk.so
%endif

%files plugin-ioctld
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/ioctld.so
%{_datadir}/%{name}/plugins/ioctld
%attr(4755,root,root) %{_libexecdir}/ioctld

%if %{with yesterday_snapshot}
%files plugin-jogger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/jogger.so
%endif

%if %{with sqlite} || %{with sqlite3}
%files plugin-logsqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/logsqlite.so
%{_datadir}/%{name}/plugins/logsqlite
%endif

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

%if %{with yesterday_snapshot}
%files plugin-protocol-polchat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/polchat.so
%endif

%if %{with readline}
%files plugin-readline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/readline.so
%{_datadir}/%{name}/plugins/readline
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

%if %{with python}
%files plugin-scripting-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so
%{_datadir}/%{name}/scripts/*.py
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
