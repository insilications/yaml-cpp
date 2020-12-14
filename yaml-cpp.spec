#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yaml-cpp
Version  : 0.6.2
Release  : 17
URL      : https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.6.2.tar.gz
Source0  : https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.6.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: yaml-cpp-lib = %{version}-%{release}
Requires: yaml-cpp-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : python3
Patch1: yaml-cpp-fix-pie.patch
Patch2: 0001-Small-readability-improvements-in-Parser.patch
Patch3: 0002-Fix-stack-overflow-807.patch

%description
# yaml-cpp [![Build Status](https://travis-ci.org/jbeder/yaml-cpp.svg?branch=master)](https://travis-ci.org/jbeder/yaml-cpp) [![Documentation](https://codedocs.xyz/jbeder/yaml-cpp.svg)](https://codedocs.xyz/jbeder/yaml-cpp/)

%package dev
Summary: dev components for the yaml-cpp package.
Group: Development
Requires: yaml-cpp-lib = %{version}-%{release}
Provides: yaml-cpp-devel = %{version}-%{release}
Requires: yaml-cpp = %{version}-%{release}

%description dev
dev components for the yaml-cpp package.


%package lib
Summary: lib components for the yaml-cpp package.
Group: Libraries
Requires: yaml-cpp-license = %{version}-%{release}

%description lib
lib components for the yaml-cpp package.


%package license
Summary: license components for the yaml-cpp package.
Group: Default

%description license
license components for the yaml-cpp package.


%prep
%setup -q -n yaml-cpp-yaml-cpp-0.6.2
cd %{_builddir}/yaml-cpp-yaml-cpp-0.6.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586901521
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1586901521
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yaml-cpp
cp %{_builddir}/yaml-cpp-yaml-cpp-0.6.2/LICENSE %{buildroot}/usr/share/package-licenses/yaml-cpp/c417cfcd91cc771f0113d80b7e106d60c1e3afb7
cp %{_builddir}/yaml-cpp-yaml-cpp-0.6.2/test/gtest-1.8.0/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/yaml-cpp/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/yaml-cpp-yaml-cpp-0.6.2/test/gtest-1.8.0/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/yaml-cpp/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/yaml-cpp-yaml-cpp-0.6.2/test/gtest-1.8.0/googletest/LICENSE %{buildroot}/usr/share/package-licenses/yaml-cpp/5a2314153eadadc69258a9429104cd11804ea304
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/include/gmock/gmock-actions.h
rm -f %{buildroot}/usr/include/gmock/gmock-cardinalities.h
rm -f %{buildroot}/usr/include/gmock/gmock-generated-actions.h
rm -f %{buildroot}/usr/include/gmock/gmock-generated-actions.h.pump
rm -f %{buildroot}/usr/include/gmock/gmock-generated-function-mockers.h
rm -f %{buildroot}/usr/include/gmock/gmock-generated-function-mockers.h.pump
rm -f %{buildroot}/usr/include/gmock/gmock-generated-matchers.h
rm -f %{buildroot}/usr/include/gmock/gmock-generated-matchers.h.pump
rm -f %{buildroot}/usr/include/gmock/gmock-generated-nice-strict.h
rm -f %{buildroot}/usr/include/gmock/gmock-generated-nice-strict.h.pump
rm -f %{buildroot}/usr/include/gmock/gmock-matchers.h
rm -f %{buildroot}/usr/include/gmock/gmock-more-actions.h
rm -f %{buildroot}/usr/include/gmock/gmock-more-matchers.h
rm -f %{buildroot}/usr/include/gmock/gmock-spec-builders.h
rm -f %{buildroot}/usr/include/gmock/gmock.h
rm -f %{buildroot}/usr/include/gmock/internal/custom/gmock-generated-actions.h
rm -f %{buildroot}/usr/include/gmock/internal/custom/gmock-generated-actions.h.pump
rm -f %{buildroot}/usr/include/gmock/internal/custom/gmock-matchers.h
rm -f %{buildroot}/usr/include/gmock/internal/custom/gmock-port.h
rm -f %{buildroot}/usr/include/gmock/internal/gmock-generated-internal-utils.h
rm -f %{buildroot}/usr/include/gmock/internal/gmock-generated-internal-utils.h.pump
rm -f %{buildroot}/usr/include/gmock/internal/gmock-internal-utils.h
rm -f %{buildroot}/usr/include/gmock/internal/gmock-port.h
rm -f %{buildroot}/usr/include/gtest/gtest-death-test.h
rm -f %{buildroot}/usr/include/gtest/gtest-message.h
rm -f %{buildroot}/usr/include/gtest/gtest-param-test.h
rm -f %{buildroot}/usr/include/gtest/gtest-param-test.h.pump
rm -f %{buildroot}/usr/include/gtest/gtest-printers.h
rm -f %{buildroot}/usr/include/gtest/gtest-spi.h
rm -f %{buildroot}/usr/include/gtest/gtest-test-part.h
rm -f %{buildroot}/usr/include/gtest/gtest-typed-test.h
rm -f %{buildroot}/usr/include/gtest/gtest.h
rm -f %{buildroot}/usr/include/gtest/gtest_pred_impl.h
rm -f %{buildroot}/usr/include/gtest/gtest_prod.h
rm -f %{buildroot}/usr/include/gtest/internal/custom/gtest-port.h
rm -f %{buildroot}/usr/include/gtest/internal/custom/gtest-printers.h
rm -f %{buildroot}/usr/include/gtest/internal/custom/gtest.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-death-test-internal.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-filepath.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-internal.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-linked_ptr.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-param-util-generated.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-param-util-generated.h.pump
rm -f %{buildroot}/usr/include/gtest/internal/gtest-param-util.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-port-arch.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-port.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-string.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-tuple.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-tuple.h.pump
rm -f %{buildroot}/usr/include/gtest/internal/gtest-type-util.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-type-util.h.pump
rm -f %{buildroot}/usr/lib/libgmock.so
rm -f %{buildroot}/usr/lib/libgmock_main.so
rm -f %{buildroot}/usr/lib/libgtest.so
rm -f %{buildroot}/usr/lib/libgtest_main.so
rm -f %{buildroot}/usr/share/package-licenses/yaml-cpp/test_gtest-1.8.0_googlemock_LICENSE
rm -f %{buildroot}/usr/share/package-licenses/yaml-cpp/test_gtest-1.8.0_googlemock_scripts_generator_LICENSE
rm -f %{buildroot}/usr/share/package-licenses/yaml-cpp/test_gtest-1.8.0_googletest_LICENSE

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/yaml-cpp/anchor.h
/usr/include/yaml-cpp/binary.h
/usr/include/yaml-cpp/contrib/anchordict.h
/usr/include/yaml-cpp/contrib/graphbuilder.h
/usr/include/yaml-cpp/depthguard.h
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
/usr/lib64/cmake/yaml-cpp/yaml-cpp-config-version.cmake
/usr/lib64/cmake/yaml-cpp/yaml-cpp-config.cmake
/usr/lib64/cmake/yaml-cpp/yaml-cpp-targets-relwithdebinfo.cmake
/usr/lib64/cmake/yaml-cpp/yaml-cpp-targets.cmake
/usr/lib64/libyaml-cpp.so
/usr/lib64/pkgconfig/yaml-cpp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libyaml-cpp.so.0.6
/usr/lib64/libyaml-cpp.so.0.6.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yaml-cpp/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/yaml-cpp/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/yaml-cpp/c417cfcd91cc771f0113d80b7e106d60c1e3afb7
