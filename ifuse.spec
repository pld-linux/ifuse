Summary:	Mount Apple iPhone and iPod touch devices
Name:		ifuse
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Libraries
URL:		http://www.libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	325d58abe182afa95187e6c55f2bba5f
BuildRequires:	glib2-devel
BuildRequires:	libfuse-devel
BuildRequires:	libimobiledevice-devel
Requires:	hal
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
