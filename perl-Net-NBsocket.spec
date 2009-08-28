#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	NBsocket
Summary:	Net::NBsocket - Non-Blocking Sockets
Summary(pl.UTF-8):	Net::NBsocket - nieblokujące gniazda
Name:		perl-Net-NBsocket
Version:	0.15
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cf3fcbd091ac411287d2b38e5642382f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::NBsocket provides a wrapper for Socket to supply Non-Blocking
sockets of various flavors.

%description -l pl.UTF-8
Net::NBsocket to pakiet obudowujący Socket, aby udostępnić
nieblokujące gniazda różnych rodzajów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/NBsocket/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/*.pm
%dir %{perl_vendorlib}/auto/Net/NBsocket
%{perl_vendorlib}/auto/Net/NBsocket/_accept.al
%{perl_vendorlib}/auto/Net/NBsocket/_connect.al
%{perl_vendorlib}/auto/Net/NBsocket/accept_Blk.al
%{perl_vendorlib}/auto/Net/NBsocket/accept_NB.al
%{perl_vendorlib}/auto/Net/NBsocket/autosplit.ix
%{perl_vendorlib}/auto/Net/NBsocket/bind2pp.al
%{perl_vendorlib}/auto/Net/NBsocket/connectBlk.al
%{perl_vendorlib}/auto/Net/NBsocket/connect_NB.al
%{perl_vendorlib}/auto/Net/NBsocket/open_Listen.al
%{perl_vendorlib}/auto/Net/NBsocket/open_UDP.al
%{perl_vendorlib}/auto/Net/NBsocket/open_listenNB.al
%{perl_vendorlib}/auto/Net/NBsocket/open_udpNB.al
%{perl_vendorlib}/auto/Net/NBsocket/set_NB.al
%{perl_vendorlib}/auto/Net/NBsocket/set_so_linger.al
%{_mandir}/man3/*
