%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1
%define api %(echo %{version} |cut -d. -f1-2)
%define oldapi 0.14
%define major 0
%define libname %mklibname orcus %{api} %{major}
%define libmso %mklibname orcus-mso %{api} %{major}
%define libparser %mklibname orcus-parser %{api} %{major}
%define libspreadsheet %mklibname orcus-spreadsheet-model %{api} %{major}
%define devname %mklibname -d orcus
%define oldlibname %mklibname orcus %{oldapi} %{major}
%define oldlibmso %mklibname orcus-mso %{oldapi} %{major}
%define oldlibparser %mklibname orcus-parser %{oldapi} %{major}
%define oldlibspreadsheet %mklibname orcus-spreadsheet-model %{oldapi} %{major}
%bcond_without spreadsheet_model

Summary:	Standalone file import filter library for spreadsheet documents
Name:		liborcus
Version:	0.15.4
Release:	3
Group:		Office
License:	MIT
Url:		http://gitlab.com/orcus/orcus
Source0:	http://kohei.us/files/orcus/src/liborcus-%{version}.tar.xz
BuildRequires:	boost-devel >= 1.72
BuildRequires:	mdds-devel
BuildRequires:	pkgconfig(libixion-0.15)
BuildRequires:	pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libname}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libmso}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
Obsoletes:	%{oldlibmso} < %{EVRD}

%description -n %{libmso}
This package contains a shared library library for %{name}.

%package -n %{libparser}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
Obsoletes:	%{oldlibparser} < %{EVRD}

%description -n %{libparser}
This package contains a shared library library for %{name}.

%if %{with spreadsheet_model}
%package -n %{libspreadsheet}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
Obsoletes:	%{oldlibspreadsheet} < %{EVRD}

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
%autosetup -p1

%build
%configure \
	--disable-debug --disable-silent-rules --disable-static \
	--disable-werror --with-pic \
	--disable-python \
%if %{with spreadsheet_model}
	--enable-spreadsheet-model
%else
	--disable-spreadsheet-model
%endif

sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool

%make_build

%install
%make_install

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
