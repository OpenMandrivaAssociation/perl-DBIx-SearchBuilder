%define module	DBIx-SearchBuilder
%define name	perl-%{module}
%define version 1.49
%define rel     1

%define _requires_exceptions perl(DBD::Oracle)

Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Summary:	Database-independent schema objects
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Encapsulate SQL queries and rows in simple perl object
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/DBIx/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Want)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(Class::ReturnValue)
BuildRequires:	perl(Cache::Simple::TimedExpiry)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Clone)
BuildRequires:	perl(DBIx::DBSchema)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
find -name \*.pm | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/DBIx
%{_mandir}/*/*

