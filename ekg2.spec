#
# Conditional build:
%bcond_without	aspell		# spell-checking support with aspell
%bcond_without	rss		# rss plugin
%bcond_without	gadugadu	# gg plugin
%bcond_without	gpg		# gpg plugin
%bcond_without	gtk		# gtk plugin
%bcond_without	jabber		# jabber plugin
%bcond_without	gnutls		# TLS support in jabber plugin
%bcond_with	libgsm		# gsm plugin (not supported by build system)
%bcond_without	perl		# Perl plugin
%bcond_without	python		# Python plugin
%bcond_without	readline	# readline interface
%bcond_with	sqlite		# SQLite 2 support in logsqlite plugin (conflicts with sqlite3)
%bcond_without	sqlite3		# SQLite 3 support in logsqlite plugin
%bcond_with	xosd		# xosd plugin (not supported by build system)
%bcond_with	git		# checkout git master instead of Source0 - requested by ekg2 developer
%bcond_with	irckeepalive	# patch that check irc connection and disconnect when server dies

%if %{with git}
%define		subver git.%(date +%Y%m%d)
%else
%define	gitref	f427d083ee899d42532c046100490a915b0e8a82
%define	subver	20190316
%endif

%if %{with sqlite}
%undefine sqlite3
%endif

Summary:	Multi-protocol instant messaging and chat client
Summary(pl.UTF-8):	Wieloprotokołowy komunikator internetowy
Name:		ekg2
Version:	0.4
%define	rel	2
Release:	0.%{subver}.%{rel}
Epoch:		2
License:	GPL v2+
Group:		Applications/Communications
%if %{without git}
Source0:	https://github.com/ekg2/ekg2/archive/%{gitref}/%{name}-%{subver}.tar.gz
# Source0-md5:	8229554ddeeda23d2a83c0ed35325453
%endif
Patch0:		%{name}-perl-install.patch
Patch1:		%{name}-gtk.patch
Patch2:		%{name}-bug-63.patch
Patch3:		%{name}-keepalive_irc.patch
Patch4:		%{name}-types.patch
URL:		https://github.com/ekg2/ekg2
%{?with_aspell:BuildRequires:	aspell-devel}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.6
%if %{with rss} || %{with jabber}
BuildRequires:	expat-devel >= 1.95
%endif
BuildRequires:	gettext-tools >= 0.17-8
%{?with_gadugadu:BuildRequires:	giflib-devel}
%{?with_git:BuildRequires:	git-core}
BuildRequires:	glib2-devel >= 1:2.24
%{?with_gnutls:BuildRequires:	gnutls-devel >= 1.2.5}
%{?with_gpg:BuildRequires:	gpgme-devel}
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.14.1}
%{?with_gadugadu:BuildRequires:	libgadu-devel}
%{?with_libgsm:BuildRequires:	libgsm-devel}
%{?with_gadugadu:BuildRequires:	libjpeg-devel}
BuildRequires:	libltdl-devel >= 2:2
BuildRequires:	libtool >= 2:2
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel >= 1:2.4}
%{?with_readline:BuildRequires:	readline-devel}
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	sed >= 4.0
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel >= 3}
%{?with_xosd:BuildRequires:	xosd-devel}
BuildRequires:	zlib-devel
Obsoletes:	ekg2-plugin-ioctld < 2:0.4-0.20110305
Obsoletes:	ekg2-plugin-remote < 2:0.4-0.20110305
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multi-protocol instant messaging and chat client with many plugins.

%description -l pl.UTF-8
Wieloprotokołowy, otwarty komunikator internetowy z wieloma wtyczkami.

%package plugin-rss
Summary:	rss plugin for ekg2
Summary(pl.UTF-8):	Wtyczka rss dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	ekg2-plugin-feed < 2:0.20110305

%description plugin-rss
rss plugin for ekg2.

%description plugin-rss -l pl.UTF-8
Wtyczka rss dla ekg2.

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
Requires:	gtk+2 >= 2:2.14.1

%description plugin-gtk
gtk plugin for ekg2.

%description plugin-gtk -l pl.UTF-8
Wtyczka gtk dla ekg2.

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

%package plugin-protocol-icq
Summary:	ICQ protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu ICQ dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-icq
ICQ protocol plugin for ekg2.

%description plugin-protocol-icq -l pl.UTF-8
Wtyczka protokołu ICQ dla ekg2.

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
Summary:	Jabber and Tlen protocols plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołów Jabber i Tlen dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-jabber
Jabber and Tlen protocols plugin for ekg2.

%description plugin-protocol-jabber -l pl.UTF-8
Wtyczka protokołów Jabber i Tlen dla ekg2.

%package plugin-protocol-polchat
Summary:	Polchat protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu polchat dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-polchat
Polchat protocol plugin for ekg2.

%description plugin-protocol-polchat -l pl.UTF-8
Wtyczka protokołu polchat dla ekg2.

%package plugin-protocol-rivchat
Summary:	Rivchat protocol plugin for ekg2
Summary(pl.UTF-8):	Wtyczka protokołu rivchat dla ekg2
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-protocol-rivchat
Rivchat protocol plugin for ekg2.

%description plugin-protocol-rivchat -l pl.UTF-8
Wtyczka protokołu rivchat dla ekg2.

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
Requires:	python-modules

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
%if %{with git}
%setup -q -T -c -n %{name}-%{subver}
repo="%ekg2repo"
branch="%ekg2branch"
if [ "$repo" = "%%ekg2repo" ]; then
repo="git://github.com/leafnode/ekg2.git"
fi
if [ "$branch" = "%%ekg2branch" ]; then
branch="master"
fi
git init
git fetch $repo $branch
git checkout FETCH_HEAD
%else
%setup -q -n %{name}-%{gitref}
%endif

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0
%patch -P4 -p1

%if %{with irckeepalive}
%patch -P3 -p1
%endif

touch po/Makefile.in.in
find -name *.c > po/POTFILES.in

%{__rm} m4/gpgme.m4

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}

# for hostent.h_addr (should be in CPPFLAGS, but it's overridden in plugins/jabber)
CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
CPPFLAGS="%{rpmcppflags} -DNCURSES_INTERNALS"
%configure \
	--disable-nntp \
	--with-aspell%{!?with_aspell:=no} \
%if %{with rss} || %{with jabber}
	--with-expat \
%else
	--without-expat \
%endif
	%{!?with_gpg:--without-gpg} \
	--with-gnutls%{!?with_gnutls:=no} \
	--with-gtk%{!?with_gtk:=no} \
	--with-libgadu%{!?with_gadugadu:=no} \
	%{?with_libgsm:--with-libgsm} \
	%{!?with_perl:--without-perl} \
	--with-python%{!?with_python:=no} \
	--with-readline%{!?with_readline:=no} \
	--with-sqlite%{!?with_sqlite:=no} \
	--with-sqlite3%{!?with_sqlite3:=no} \
	%{?with_xosd:--with-xosd}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md docs/ekg2book* docs/README docs/TODO docs/*.txt
%attr(755,root,root) %{_bindir}/ekg2
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/autoresponder.so
%{_libdir}/%{name}/plugins/autoresponder.la
%{_datadir}/%{name}/plugins/autoresponder
%attr(755,root,root) %{_libdir}/%{name}/plugins/logs.so
%{_libdir}/%{name}/plugins/logs.la
%attr(755,root,root) %{_libdir}/%{name}/plugins/mail.so
%{_libdir}/%{name}/plugins/mail.la
%{_datadir}/%{name}/plugins/mail
%attr(755,root,root) %{_libdir}/%{name}/plugins/ncurses.so
%{_libdir}/%{name}/plugins/ncurses.la
%attr(755,root,root) %{_libdir}/%{name}/plugins/rc.so
%{_libdir}/%{name}/plugins/rc.la
%attr(755,root,root) %{_libdir}/%{name}/plugins/sms.so
%{_libdir}/%{name}/plugins/sms.la
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/plugins/logs
%{_datadir}/%{name}/plugins/ncurses
%{_datadir}/%{name}/plugins/sms
%{_datadir}/%{name}/plugins/rc
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}/themes

%files plugin-rss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/rss.so
%{_libdir}/%{name}/plugins/rss.la

%if %{with gpg}
%files plugin-gpg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gpg.so
%{_libdir}/%{name}/plugins/gpg.la
%dir %{_datadir}/ekg2/plugins/gpg
%{_datadir}/ekg2/plugins/gpg/commands-en.txt
%{_datadir}/ekg2/plugins/gpg/commands-pl.txt
%endif

%if %{with gtk}
%files plugin-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gtk.so
%{_libdir}/%{name}/plugins/gtk.la
%endif

%files plugin-jogger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/jogger.so
%{_libdir}/%{name}/plugins/jogger.la

%if %{with sqlite} || %{with sqlite3}
%files plugin-logsqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/logsqlite.so
%{_libdir}/%{name}/plugins/logsqlite.la
%{_datadir}/%{name}/plugins/logsqlite
%endif

%files plugin-protocol-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gg.so
%{_libdir}/%{name}/plugins/gg.la
%{_datadir}/%{name}/plugins/gg

%if %{with libgsm}
%files plugin-protocol-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/gsm.so
%{_libdir}/%{name}/plugins/gsm.la
%endif

%files plugin-protocol-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/icq.so
%{_libdir}/%{name}/plugins/icq.la

%files plugin-protocol-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/irc.so
%{_libdir}/%{name}/plugins/irc.la
%{_datadir}/%{name}/plugins/irc

%if %{with jabber}
%files plugin-protocol-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/jabber.so
%{_libdir}/%{name}/plugins/jabber.la
%{_datadir}/%{name}/plugins/jabber
%endif

%files plugin-protocol-polchat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/polchat.so
%{_libdir}/%{name}/plugins/polchat.la

%files plugin-protocol-rivchat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/rivchat.so
%{_libdir}/%{name}/plugins/rivchat.la

%if %{with readline}
%files plugin-readline
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/readline.so
%{_libdir}/%{name}/plugins/readline.la
%{_datadir}/%{name}/plugins/readline
%endif

%if %{with perl}
%files plugin-scripting-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/perl.so
%{_libdir}/%{name}/plugins/perl.la
%{perl_vendorarch}/Ekg2.pm
%dir %{perl_vendorarch}/Ekg2
%{perl_vendorarch}/Ekg2/Irc.pm
%dir %{perl_vendorarch}/auto/Ekg2
%attr(755,root,root) %{perl_vendorarch}/auto/Ekg2/Ekg2.so
%dir %{perl_vendorarch}/auto/Ekg2/Irc
%attr(755,root,root) %{perl_vendorarch}/auto/Ekg2/Irc/Irc.so
%{_datadir}/%{name}/scripts/*.pl
%endif

%if %{with python}
%files plugin-scripting-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so
%{_libdir}/%{name}/plugins/python.la
%{_datadir}/%{name}/scripts/*.py
%dir %{_datadir}/ekg2/plugins/python
%{_datadir}/ekg2/plugins/python/commands-en.txt
%{_datadir}/ekg2/plugins/python/commands-pl.txt
%endif

%files plugin-sim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sim.so
%{_libdir}/%{name}/plugins/sim.la
%{_datadir}/%{name}/plugins/sim

%if %{with xosd}
%files plugin-xosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/xosd.so
%{_libdir}/%{name}/plugins/xosd.la
%{_datadir}/%{name}/plugins/xosd
%endif
