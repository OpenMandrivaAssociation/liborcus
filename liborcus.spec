%define api 0.6
%define major 0

%define libname %mklibname orcus %api %major
%define develname %mklibname -d orcus

Name: liborcus
Version: 0.5.1
Release: %mkrel 7
Summary: Standalone file import filter library for spreadsheet documents
Group: Office/Spreadsheet
License: MIT
URL: http://gitorious.org/orcus
# https://gitorious.org/orcus/pages/Download :
Source: http://kohei.us/files/orcus/src/%{name}-%{version}.tar.bz2
Patch0: liborcus_0.3.0-boost.patch
Patch1: fix-linking.diff
BuildRequires: boost-devel
BuildRequires: mdds-devel
BuildRequires: zlib-devel
# Temporary for cauldron:
Obsoletes: liborcus0.4

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libname}
Summary: Standalone file import filter library for spreadsheet documents
Group: Office/Spreadsheet
Obsoletes: %{name} < %{version}-%{release}
# Temporary for cauldron:
Obsoletes: liborcus0.4 %{mklibname orcus 0.4 %major}

%description -n %{libname}
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{name}-devel < %{version}-%{release}
# Temporary for cauldron:
Obsoletes: %{_lib}orcus0.4-devel

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools for working with Orcus
Group: Office/Spreadsheet
Requires: %{libname} = %{version}-%{release}
# Temporary for cauldron:
Obsoletes: liborcus0.4-tools

%description tools
Tools for working with Orcus.

%prep
%setup -q
%apply_patches

%build
# TODO spreadsheet-model requires ixion
%configure2_5x --disable-debug --disable-static --disable-werror --with-pic \
    --disable-spreadsheet-model --without-libzip
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make

%install
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS
%{_libdir}/%{name}*-%{api}.so.%{major}*


%files -n %{develname}
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}*-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

%files tools
%{_bindir}/orcus-*


%changelog
* Sat Jun 08 2013 tv <tv> 0.5.1-7.mga4
+ Revision: 440697
- fix obsoletes

* Sat Jun 08 2013 tv <tv> 0.5.1-6.mga4
+ Revision: 440661
- more obsolete for temporary liborcus0.4

* Sat Jun 08 2013 tv <tv> 0.5.1-4.mga4
+ Revision: 440632
- obsolete temporary liborcus0.4 package

* Sat May 25 2013 tv <tv> 0.5.1-2.mga4
+ Revision: 426989
- adjust file list
- bump library api
- further fix linking
- further fix linking
- patch 1: fix linking with boost
- new release
- new release

* Thu Apr 11 2013 ennael <ennael> 0.3.0-5.mga3
+ Revision: 409490
- rebuild for boost 1.53

* Sat Jan 12 2013 umeabot <umeabot> 0.3.0-4.mga3
+ Revision: 357937
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Thu Dec 20 2012 fwang <fwang> 0.3.0-3.mga3
+ Revision: 333080
- fix obsoletes

* Thu Dec 20 2012 fwang <fwang> 0.3.0-2.mga3
+ Revision: 333001
- fix missing includes
- use configure2_5x
- rebuild for new boost

* Mon Dec 17 2012 tv <tv> 0.3.0-1.mga3
+ Revision: 331976
- fix new release
- fix new release

* Mon Dec 17 2012 tv <tv> 0.1.0-1.mga3
+ Revision: 331938
- fix group
- fix group
- imported package liborcus

