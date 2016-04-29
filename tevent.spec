#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tevent
Version  : 0.9.28
Release  : 3
URL      : https://www.samba.org/ftp/tevent/tevent-0.9.28.tar.gz
Source0  : https://www.samba.org/ftp/tevent/tevent-0.9.28.tar.gz
Summary  : An event system library
Group    : Development/Tools
License  : LGPL-3.0+
Requires: tevent-lib
Patch1: 0001_fix_default_install_path.patch
Patch2: 0002_fix_waf_options.patch

%description
See http://code.google.com/p/waf/ for more information on waf
You can get a svn copy of the upstream source with:

%package dev
Summary: dev components for the tevent package.
Group: Development
Requires: tevent-lib
Provides: tevent-devel

%description dev
dev components for the tevent package.


%package lib
Summary: lib components for the tevent package.
Group: Libraries

%description lib
lib components for the tevent package.


%prep
%setup -q -n tevent-0.9.28
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib/*.so.*
/usr/lib/tevent/libtalloc.so.2
/usr/lib/tevent/libtalloc.so.2.1.5
