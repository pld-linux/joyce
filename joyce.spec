Summary:	JOYCE - an Amstrad PCW emulator
Summary(pl):	JOYCE - emulator Amstrada PCW
Name:		joyce
Version:	2.0.2
Release:	5
License:	GPL
Group:		Applications
Source0:	http://www.seasip.demon.co.uk/Unix/Joyce/%{name}-%{version}.tar.gz
# Source0-md5:	09f2f6a01b441c0bfa3a544378f94555
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-gcc.patch
Patch3:		%{name}-am.patch
Patch4:		%{name}-sdl.patch
URL:		http://www.seasip.demon.co.uk/Unix/Joyce/
BuildRequires:	SDL-devel >= 1.0.8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpmredir-devel >= 1.1.0
BuildRequires:	lib765-devel >= 0.2.0
BuildRequires:	libdsk-devel >= 1.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Requires:	cpmredir >= 1.1.0
Requires:	lib765 >= 0.2.0
Requires:	libdsk >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JOYCE is an Amstrad PCW emulator for UNIX and Windows. It emulates the
PCW 8000, 9000 and 10 series computers, but not the PCW 16.

%description -l pl
JOYCE jest emulatorem Amstrada PCW dla uniksów i Windows. Emuluje
komputery PCW z serii 8000, 9000 i 10, ale nie PCW 16.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} `xml2-config --cflags`"
CXXFLAGS="%{rpmcflags} `xml2-config --cflags`"
%configure \
	--enable-floppy \
	--with-stl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO Docs/*.pdf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/Joyce
