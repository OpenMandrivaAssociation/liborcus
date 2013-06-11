%define api	0.6
%define major	0
%define libname	%mklibname orcus %{api} %{major}
%define devname	%mklibname -d orcus

Summary:	Standalone file import filter library for spreadsheet documents
Name:		liborcus
Version:	0.5.1
Release:	1
Group:		Office/Spreadsheet
License:	MIT
Url:		http://gitorious.org/orcus
Source0:	http://kohei.us/files/orcus/src/%{name}-%{version}.tar.bz2
Patch0:		liborcus_0.3.0-boost.patch
Patch1:		fix-linking.diff
BuildRequires:	boost-devel
BuildRequires:	mdds-devel
BuildRequires:	pkgconfig(libixion-0.6)
BuildRequires:	pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{libname}
Summary:	Standalone file import filter library for spreadsheet documents
Group:		Office/Spreadsheet

%description -n %{libname}
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools for working with Orcus
Group:		Office/Spreadsheet
Requires:	%{libname} = %{version}-%{release}

%description tools
Tools for working with Orcus.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-debug \
	--disable-static \
	--disable-werror \
	--with-pic \
	--without-libzip
%make

%install
%makeinstall_std

%files tools
%doc AUTHORS
%{_bindir}/orcus-*

%files -n %{libname}
%{_libdir}/%{name}*-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}*-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

