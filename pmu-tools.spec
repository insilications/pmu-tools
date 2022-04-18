#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : pmu-tools
Version  : 1.0.0
Release  : 4
URL      : file:///aot/build/clearlinux/packages/pmu-tools/pmu-tools-v1.0.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/pmu-tools/pmu-tools-v1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : bash
BuildRequires : buildreq-cmake
BuildRequires : ca-certs
BuildRequires : cpio-bin
BuildRequires : curl
BuildRequires : curl-bin
BuildRequires : curl-dev
BuildRequires : curl-lib
BuildRequires : findutils
BuildRequires : mlocate
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : p11-kit
BuildRequires : pcre-dev
BuildRequires : pcre-extras
BuildRequires : sd
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n pmu-tools-clr
cd %{_builddir}/pmu-tools-clr

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650289510
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
%cmake ..
make  %{?_smp_mflags}    V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1650289510
rm -rf %{buildroot}
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
pushd clr-build
%make_install
popd
## install_append content
pushd %{buildroot}/usr/share/pmu-tools
rm -rf .gitignore || :
rm -rf .git/ || :
rm -rf .github/ || :
popd
mkdir -p %{buildroot}/usr/bin || :
pushd %{buildroot}/usr/bin
ln -sf ../share/pmu-tools/ocperf.py %{buildroot}/usr/bin/ocperf
chmod +x ./ocperf
popd
## install_append end

%files
%defattr(-,root,root,-)
