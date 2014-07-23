Summary:	Command line interface for Virtual Instrument Software Architecture
Summary(pl.UTF-8):	Interfejs linii poleceń do Virtual Instrument Software Architecture
Name:		vish
Version:	0.0.20130714
Release:	1
License:	GPL v3+
Group:		Libraries
# upstream (pre)releases
Source0:	http://www.librevisa.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c0b1f953948453e371096ea30613d0d7
URL:		http://www.librevisa.org/
BuildRequires:	autoconf >= 2.67
BuildRequires:	automake >= 1:1.10
BuildRequires:	librevisa-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VISA API provides a common interface to test and measurement
equipment that can be accessed via GPIB, USB or VXI-11 interfaces.

This package contains a command line interface that can be used to
send raw commands.

%description -l pl.UTF-8
VISA API zapewnia ogólny interfejs do urządzeń testowych i
pomiarowych, z którymi można łączyć się przez interfejsy GPIB, USB
albo VXI-11.

Ten pakiet zawiera interfejs linii poleceń, który można wykorzystywać
do wysyłania surowych poleceń.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_bindir}/vish
%{_mandir}/man1/vish.1*
