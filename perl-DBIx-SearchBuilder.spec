%define upstream_name	 DBIx-SearchBuilder
%define upstream_version 1.59

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBD::Oracle\\)'
%else
%define _requires_exceptions perl(DBD::Oracle)
%endif


Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Database-independent schema objects
License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Encapsulate SQL queries and rows in simple perl object
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Want)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Class::ReturnValue)
BuildRequires:	perl(Cache::Simple::TimedExpiry)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Clone)
BuildRequires:	perl(DBIx::DBSchema)
BuildArch:	noarch

%description
This module provides an object-oriented mechanism for retrieving and updating
data in a DBI-accesible database.

In order to use this module, you should create a subclass of
DBIx::SearchBuilder and a subclass of DBIx::SearchBuilder::Record for each
table that you wish to access. (See the documentation of
DBIx::SearchBuilder::Record for more information on subclassing it.)

Your DBIx::SearchBuilder subclass must override NewItem, and probably should
override at least _Init also; at the very least, _Init should probably call
_Handle and _Table to set the database handle (a DBIx::SearchBuilder::Handle
object) and table name for the class. You can try to override just about
every other method here, as long as you think you know what you are doing.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -name \*.pm | xargs chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/DBIx
%{_mandir}/*/*



%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.590.0-2mdv2011.0
+ Revision: 681362
- mass rebuild

* Sun Nov 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.590.0-1mdv2011.0
+ Revision: 599550
- update to new version 1.59
- update to new version 1.58

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2011.0
+ Revision: 396844
- update to 1.56
- using %%perl_convert_version
- fixed license field

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.55-1mdv2010.0
+ Revision: 373933
- new version

* Thu Jul 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.54-1mdv2009.0
+ Revision: 233396
- update to new version 1.54

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.53-1mdv2009.0
+ Revision: 193797
- update to new version 1.53

* Mon Jan 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.51-1mdv2008.1
+ Revision: 155668
- update to new version 1.51

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.50-1mdv2008.1
+ Revision: 112548
- update to new version 1.50
- don't check dependencies

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.49-1mdv2008.0
+ Revision: 52488
- update to new version 1.49

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 1.48-1mdv2008.0
+ Revision: 20898
- update to 1.48


* Sat Apr 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.43-1mdk
- New release 1.43

* Thu Apr 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-1mdk
- New release 1.42
- better source URL
- better buildrequires syntax

* Sun Mar 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-1mdk
- New release 1.40

* Fri Mar 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.39-1mdk
- New release 1.39
- spec cleanup

* Mon Jan 23 2006 Michael Scherer <misc@mandriva.org> 1.38-2mdk
- add missing buildRequires

* Wed Jan 04 2006 Michael Scherer <misc@mandriva.org> 1.38-1mdk
- New release 1.38

* Fri Dec 30 2005 Michael Scherer <misc@mandriva.org> 1.36-3mdk
- Do not ship empty dir

* Fri Dec 16 2005 Michael Scherer <misc@mandriva.org> 1.36-2mdk
- fix BuildRequires

* Wed Dec 07 2005 Michael Scherer <misc@mandriva.org> 1.36-1mdk
- New release 1.36

* Tue Nov 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.35-1mdk
- 1.35

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 1.33-2mdk
- do not requires perl-DBD-Oracle

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 1.33-1mdk
- First mandriva package

