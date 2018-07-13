%define upstream_name    Crypt-SmbHash
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	15

Summary:	Crypt::SmbHash Perl module - generate LM/NT hashes like smbpasswd
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Crypt-SmbHash/
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides functions to generate LM/NT hashes used in
Samba's 'password' files, like smbpasswd.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
%{!?_without_tests:make test}

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/SmbHash.pm
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-4mdv2012.0
+ Revision: 765137
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-3
+ Revision: 763651
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-2
+ Revision: 667063
- mass rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 408945
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.12-4mdv2009.0
+ Revision: 223584
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.12-3mdv2008.1
+ Revision: 180376
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.12-2mdv2008.0
+ Revision: 23416
- rebuild


* Thu Feb 10 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.12-1mdk
- initial package (PLD import) for new smbldap-tools in samba-3.0.11

