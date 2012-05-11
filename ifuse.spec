Summary:	Mount Apple iPhone and iPod touch devices
Name:		ifuse
Version:	1.1.2
Release:	1
License:	GPL v2+
Group:		Libraries
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	4152526b2ac3c505cb41797d997be14d
BuildRequires:	libfuse-devel
BuildRequires:	libimobiledevice-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fuse filesystem for mounting iPhone and iPod touch devices.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/ifuse
%{_mandir}/man1/ifuse.1*
