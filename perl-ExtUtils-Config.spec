#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Config
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::Config - A wrapper for perl's configuration
#Summary(pl.UTF-8):	
Name:		perl-ExtUtils-Config
Version:	0.007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2829c0dfa8a7e51b3f582efbee4bb128
URL:		http://search.cpan.org/dist/ExtUtils-Config/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::Config is an abstraction around the %Config hash.

# %description -l pl.UTF-8
# TODO

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
%{_mandir}/man3/*
