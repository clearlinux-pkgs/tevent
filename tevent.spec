#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tevent
Version  : 0.10.0
Release  : 11
URL      : https://www.samba.org/ftp/tevent/tevent-0.10.0.tar.gz
Source0  : https://www.samba.org/ftp/tevent/tevent-0.10.0.tar.gz
Summary  : An event system based on the talloc memory management library
Group    : Development/Tools
License  : LGPL-3.0+
Requires: tevent-lib = %{version}-%{release}
Requires: tevent-python = %{version}-%{release}
Requires: tevent-python3 = %{version}-%{release}
BuildRequires : python3-dev
BuildRequires : talloc-dev
Patch1: 0001-add-mock-disable-static-option.patch

%description
This subsystem ensures that we can always use a certain core set of
functions and types, that are either provided by the OS or by replacement
functions / definitions in this subsystem. The aim is to try to stick
to POSIX functions in here as much as possible. Convenience functions
that are available on no platform at all belong in other subsystems
(such as LIBUTIL).

%package dev
Summary: dev components for the tevent package.
Group: Development
Requires: tevent-lib = %{version}-%{release}
Provides: tevent-devel = %{version}-%{release}
Requires: tevent = %{version}-%{release}

%description dev
dev components for the tevent package.


%package lib
Summary: lib components for the tevent package.
Group: Libraries

%description lib
lib components for the tevent package.


%package python
Summary: python components for the tevent package.
Group: Default
Requires: tevent-python3 = %{version}-%{release}

%description python
python components for the tevent package.


%package python3
Summary: python3 components for the tevent package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tevent package.


%prep
%setup -q -n tevent-0.10.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553363595
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static --disable-rpath --disable-rpath-install
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1553363595
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libtevent.so
/usr/lib64/pkgconfig/tevent.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtevent.so.0
/usr/lib64/libtevent.so.0.10.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
