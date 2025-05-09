Summary:	The official implementation library for the hypr config language
Name:		hyprlang
Version:	0.6.3
Release:	1
License:	LGPL v3
Group:		Libraries
#Source0Download: https://github.com/hyprwm/hyprlang/releases
Source0:	https://github.com/hyprwm/hyprlang/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	6cc669d84793588263acedab5ef451a3
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	cmake >= 3.19
BuildRequires:	hyprutils-devel >= 0.7.1
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	hyprutils >= 0.7.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The hypr configuration language is an extremely efficient, yet easy to
work with, configuration language for linux applications.

It's user-friendly, easy to grasp, and easy to implement.

%package devel
Summary:	Header files for hyprlang
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for hyprlang.

%prep
%setup -q
%patch -P0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libhyprlang.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhyprlang.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhyprlang.so
%{_includedir}/hyprlang.hpp
%{_pkgconfigdir}/hyprlang.pc
