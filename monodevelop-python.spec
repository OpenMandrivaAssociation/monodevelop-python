Name:     	monodevelop-python
Version:	2.8.5.1
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://download.mono-project.com/sources/%name/%name-%version.tar.bz2
BuildRequires:  monodevelop >= %version
BuildRequires:  mono-addins-devel
Summary:	Monodevelop Python Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       python

%description
Monodevelop Python Addin


%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf "$RPM_BUILD_ROOT" %name.lang
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%_prefix/share/pkgconfig
mv $RPM_BUILD_ROOT%_prefix/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%_prefix/share/pkgconfig
#gw fix pkgconfig file
sed -i -e "s/Version: $/Version: %version/" -e "s/Requires: $//" %buildroot%_datadir/pkgconfig/monodevelop-pybinding.pc

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
%_datadir/pkgconfig/monodevelop-pybinding.pc
%_prefix/lib/monodevelop/AddIns/PyBinding/

