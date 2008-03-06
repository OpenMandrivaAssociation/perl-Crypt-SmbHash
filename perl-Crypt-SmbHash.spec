Summary:	Crypt::SmbHash Perl module - generate LM/NT hashes like smbpasswd
Name:		perl-Crypt-SmbHash
URL:		http://search.cpan.org/dist/Crypt-SmbHash/
Version:	0.12
Release:	%mkrel 3
License:	GPL
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/Crypt-SmbHash-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This module provides functions to generate LM/NT hashes used in
Samba's 'password' files, like smbpasswd.

%prep
%setup -q -n Crypt-SmbHash-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/SmbHash.pm
%{_mandir}/man3/*
