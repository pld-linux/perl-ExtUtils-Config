#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	ExtUtils
%define		pnam	Config
Summary:	ExtUtils::Config - A wrapper for Perl's configuration
Summary(pl.UTF-8):	Extutils::Cofnig - obudowanie konfiguracji Perla
Name:		perl-ExtUtils-Config
Version:	0.010
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f455b5743db7b73c80e88133effa3551
URL:		https://metacpan.org/dist/ExtUtils-Config
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::Config is an abstraction around the %%Config hash.

%description -l pl.UTF-8
ExtUtils::Config to abstrakcja wokół tablicy asocjacyjnej %%Config.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/Config.pm
%{perl_vendorlib}/ExtUtils/Config
%{_mandir}/man3/ExtUtils::Config.3pm*
%{_mandir}/man3/ExtUtils::Config::MakeMaker.3pm*
