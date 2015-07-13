%define _disable_ld_no_undefined 1
%define api	0.8
%define major	0
%define libname	%mklibname orcus %{api} %{major}
%define libmso %mklibname orcus-mso %{api} %{major}
%define libparser %mklibname orcus-parser %{api} %{major}
%define libspreadsheet %mklibname orcus-spreadsheet-model %{api} %{major}
%define devname	%mklibname -d orcus
%bcond_with spreadsheet_model

Summary:	Standalone file import filter library for spreadsheet documents
Name:		liborcus
Version:	0.7.1
Release:	2
Group:		Office
License:	MIT
Url:		http://gitorious.org/orcus
Source0:	http://kohei.us/files/orcus/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	mdds-devel
BuildRequires:	pkgconfig(libixion-0.10)
BuildRequires:	pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libname}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office

%description -n %{libname}
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libmso}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office

%description -n %{libmso}
This package contains a shared library library for %{name}.

%package -n %{libparser}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office

%description -n %{libparser}
This package contains a shared library library for %{name}.

%if %{with spreadsheet_model}
%package -n %{libspreadsheet}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office

%description -n %{libspreadsheet}
This package contains a shared library library for %{name}.
%endif

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libmso} = %{version}-%{release}
Requires:	%{libparser} = %{version}-%{release}
%if %{with spreadsheet_model}
Requires:	%{libspreadsheet} = %{version}-%{release}
%endif

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools for working with Orcus
Group:		Office
Requires:	%{libname} = %{version}-%{release}

%description tools
Tools for working with Orcus.

%prep
%setup -q
%apply_patches

%build
%configure -disable-debug --disable-silent-rules --disable-static \
    --disable-werror --with-pic \
%if %{with spreadsheet_model}
    --enable-spreadsheet-model
%else
    --disable-spreadsheet-model
%endif
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make

%install
%makeinstall_std

%files tools
%doc AUTHORS
%{_bindir}/orcus-*

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{libmso}
%{_libdir}/%{name}-mso-%{api}.so.%{major}*

%files -n %{libparser}
%{_libdir}/%{name}-parser-%{api}.so.%{major}*

%if %{with spreadsheet_model}
%files -n %{libspreadsheet}
%{_libdir}/%{name}-spreadsheet-model-%{api}.so.%{major}*
%endif

%files -n %{devname}
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}*-%{api}.so
%{_libdir}/pkgconfig/%{name}*-%{api}.pc

