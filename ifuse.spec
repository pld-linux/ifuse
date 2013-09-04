Summary:	Mount Apple iPhone and iPod touch devices
Summary(pl.UTF-8):	Montowanie urządzeń Apple iPhone i iPod touch
Name:		ifuse
Version:	1.1.2
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	4152526b2ac3c505cb41797d997be14d
URL:		http://www.libimobiledevice.org/
BuildRequires:	libfuse-devel >= 2.7.0
BuildRequires:	libimobiledevice-devel >= 1.0.0
BuildRequires:	libplist-devel
BuildRequires:	pkgconfig
Requires:	libfuse >= 2.7.0
Requires:	libimobiledevice >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fuse filesystem for mounting iPhone and iPod touch devices.

%description -l pl.UTF-8
System plików FUSE do montowania urządzeń iPhone i iPod touch.

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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ifuse
%{_mandir}/man1/ifuse.1*
