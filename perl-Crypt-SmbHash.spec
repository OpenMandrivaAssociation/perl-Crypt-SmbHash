%define rel	1
Summary:	Crypt::SmbHash Perl module - generate LM/NT hashes like smbpasswd
Name:		perl-Crypt-SmbHash
URL:		http://search.cpan.org/dist/Crypt-SmbHash/
Version:	0.12
Release:	%mkrel %rel
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

%{!?_with_unstable:* %(LC_ALL=C date +"%a %b %d %Y") %{packager} %{version}-%{release}}
%{!?_with_unstable: - rebuild of %{version}-%{rel} for %{mdkversion}}
* Thu Feb 10 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.12-1mdk
- initial package (PLD import) for new smbldap-tools in samba-3.0.11
