#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yaml-cpp
Version  : 0.5.3
Release  : 6
URL      : https://github.com/jbeder/yaml-cpp/archive/release-0.5.3.tar.gz
Source0  : https://github.com/jbeder/yaml-cpp/archive/release-0.5.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: yaml-cpp-lib
BuildRequires : boost-dev
BuildRequires : cmake
Patch1: 0001-fix-libdir-install.patch

%description
Google C++ Mocking Framework
============================
http://code.google.com/p/googlemock/

%package dev
Summary: dev components for the yaml-cpp package.
Group: Development
Requires: yaml-cpp-lib
Provides: yaml-cpp-devel

%description dev
dev components for the yaml-cpp package.


%package lib
Summary: lib components for the yaml-cpp package.
Group: Libraries

%description lib
lib components for the yaml-cpp package.


%prep
%setup -q -n yaml-cpp-release-0.5.3
%patch1 -p1

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir}
make V=1  %{?_smp_mflags}
popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ; popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/yaml-cpp/anchor.h
/usr/include/yaml-cpp/binary.h
/usr/include/yaml-cpp/contrib/anchordict.h
/usr/include/yaml-cpp/contrib/graphbuilder.h
/usr/include/yaml-cpp/dll.h
/usr/include/yaml-cpp/emitfromevents.h
/usr/include/yaml-cpp/emitter.h
/usr/include/yaml-cpp/emitterdef.h
/usr/include/yaml-cpp/emittermanip.h
/usr/include/yaml-cpp/emitterstyle.h
/usr/include/yaml-cpp/eventhandler.h
/usr/include/yaml-cpp/exceptions.h
/usr/include/yaml-cpp/mark.h
/usr/include/yaml-cpp/node/convert.h
/usr/include/yaml-cpp/node/detail/bool_type.h
/usr/include/yaml-cpp/node/detail/impl.h
/usr/include/yaml-cpp/node/detail/iterator.h
/usr/include/yaml-cpp/node/detail/iterator_fwd.h
/usr/include/yaml-cpp/node/detail/memory.h
/usr/include/yaml-cpp/node/detail/node.h
/usr/include/yaml-cpp/node/detail/node_data.h
/usr/include/yaml-cpp/node/detail/node_iterator.h
/usr/include/yaml-cpp/node/detail/node_ref.h
/usr/include/yaml-cpp/node/emit.h
/usr/include/yaml-cpp/node/impl.h
/usr/include/yaml-cpp/node/iterator.h
/usr/include/yaml-cpp/node/node.h
/usr/include/yaml-cpp/node/parse.h
/usr/include/yaml-cpp/node/ptr.h
/usr/include/yaml-cpp/node/type.h
/usr/include/yaml-cpp/noncopyable.h
/usr/include/yaml-cpp/null.h
/usr/include/yaml-cpp/ostream_wrapper.h
/usr/include/yaml-cpp/parser.h
/usr/include/yaml-cpp/stlemitter.h
/usr/include/yaml-cpp/traits.h
/usr/include/yaml-cpp/yaml.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
