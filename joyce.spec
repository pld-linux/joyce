Summary:	-
Summary(pl):	-
Name:		joyce
Version:	2.0.2
Release:	1
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://www.seasip.demon.co.uk/Unix/Joyce/%{name}-%{version}.tar.gz
# Source0-md5:	09f2f6a01b441c0bfa3a544378f94555
#tools source (z80 asm): http://www.seasip.demon.co.uk/Unix/Joyce/joyce-z80-2.1.1.tar.gz
URL:		http://www.seasip.demon.co.uk/Unix/Joyce/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
