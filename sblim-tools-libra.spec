
Name:           sblim-tools-libra
Version:        1.0
Release:        1%{?dist}
Summary:        SBLIM Common Resource Access Library for WBEM-SMT tasks

Group:          System Environment/Libraries
License:        EPL
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       tog-pegasus

%description
The tools-libra package provides common functionality required by
the task-specific resource access layers of wbem-smt tasks such as
cmpi-dns and cmpi-samba.

%package devel
Summary:        SBLIM Common Resource Access Library for WBEM-SMT tasks Header Devel Files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       tog-pegasus

%description devel
The tools-libra package provides common functionality required by
the task-specific resource access layers of the wbem-smt tasks such as
cmpi-dns and cmpi-samba.
This package includes the header files and link libraries for dependent
provider packages.

%prep
%setup -q

%build
%ifarch s390 s390x ppc ppc64
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%else
export CFLAGS="$RPM_OPT_FLAGS" 
%endif
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%docdir %{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}-%{version}
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Jun 30 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0-1
- Update to sblim-tools-libra-1.0

* Tue May 26 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 0.2.3-1
- Initial support
