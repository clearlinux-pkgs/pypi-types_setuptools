#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-types_setuptools
Version  : 57.4.9
Release  : 5
URL      : https://files.pythonhosted.org/packages/65/8a/67c6299b90c7b3d97d674fb62af19a363a1f92c5eb64ddd0451e4eb04868/types-setuptools-57.4.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/8a/67c6299b90c7b3d97d674fb62af19a363a1f92c5eb64ddd0451e4eb04868/types-setuptools-57.4.9.tar.gz
Summary  : Typing stubs for setuptools
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_setuptools-python = %{version}-%{release}
Requires: pypi-types_setuptools-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the pypi-types_setuptools package.
Group: Default
Requires: pypi-types_setuptools-python3 = %{version}-%{release}

%description python
python components for the pypi-types_setuptools package.


%package python3
Summary: python3 components for the pypi-types_setuptools package.
Group: Default
Requires: python3-core
Provides: pypi(types_setuptools)

%description python3
python3 components for the pypi-types_setuptools package.


%prep
%setup -q -n types-setuptools-57.4.9
cd %{_builddir}/types-setuptools-57.4.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644250904
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
