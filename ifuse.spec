Summary:	Mount Apple iPhone and iPod touch devices
Summary(pl.UTF-8):	Montowanie urządzeń Apple iPhone i iPod touch
Name:		ifuse
Version:	1.1.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/ifuse/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	cd31fbd0ea945b2ff1e39eac8d198fdd
URL:		https://libimobiledevice.org/
BuildRequires:	libfuse-devel >= 2.7.0
BuildRequires:	libimobiledevice-devel >= 1.3.0
BuildRequires:	libplist-devel >= 2.2.0
BuildRequires:	pkgconfig
Requires:	libfuse >= 2.7.0
Requires:	libimobiledevice >= 1.3.0
Requires:	libplist >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fuse filesystem for mounting iPhone and iPod touch devices.

%description -l pl.UTF-8
System plików FUSE do montowania urządzeń iPhone i iPod touch.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/ifuse
%{_mandir}/man1/ifuse.1*
