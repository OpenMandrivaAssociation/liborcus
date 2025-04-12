%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1
%define api 0.18
# Usually, but not always:
# %(echo %{version} |cut -d. -f1-2)
%define oldapi 0.14
%define major 0
%define oldlibname %mklibname orcus 0.18 0
%define oldlibmso %mklibname orcus-mso 0.18 0
%define oldlibparser %mklibname orcus-parser 0.18 0
%define oldlibspreadsheet %mklibname orcus-spreadsheet-model 0.18 0
%define libname %mklibname orcus
%define libmso %mklibname orcus-mso
%define libparser %mklibname orcus-parser
%define libspreadsheet %mklibname orcus-spreadsheet-model
%define devname %mklibname -d orcus
%bcond_without spreadsheet_model

Summary:	Standalone file import filter library for spreadsheet documents
Name:		liborcus
Version:	0.19.2
Release:	8
Group:		Office
License:	MIT
Url:		https://gitlab.com/orcus/orcus
Source0:	http://kohei.us/files/orcus/src/liborcus-%{version}.tar.xz
BuildRequires:	boost-devel >= 1.72
BuildRequires:	pkgconfig(mdds-2.1)
BuildRequires:	pkgconfig(libixion-0.18) >= 0.19
BuildRequires:	pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libname}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
%rename %{oldlibname}

%description -n %{libname}
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libmso}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
%rename %{oldlibmso}

%description -n %{libmso}
This package contains a shared library library for %{name}.

%package -n %{libparser}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
%rename %{oldlibparser}

%description -n %{libparser}
This package contains a shared library library for %{name}.

%if %{with spreadsheet_model}
%package -n %{libspreadsheet}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office
%rename %{oldlibspreadsheet}

%description -n %{libspreadsheet}
This package contains a shared library library for %{name}.
%endif

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libmso} = %{EVRD}
Requires:	%{libparser} = %{EVRD}
%if %{with spreadsheet_model}
Requires:	%{libspreadsheet} = %{EVRD}
%endif

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools for working with Orcus
Group:		Office
Requires:	%{libname} = %{EVRD}

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
