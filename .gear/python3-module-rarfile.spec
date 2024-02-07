%global pypi_name rarfile

Name:           python3-module-%{pypi_name}
Version:        4.1
Release:        alt1
Summary:        RAR archive reader for Python
Group:          Development/Python3

License:        ISC
URL:            https://github.com/markokr/rarfile
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch:     noarch

%{?python_provide:%python_provide python3-module-%{pypi_name}}
%py3_provides %pypi_name

%description
This is Python module for RAR archive reading. The interface is made as
zipfile like as possible.

%prep
%setup -v

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE


%files
%doc README.rst
%_licensedir/%name/LICENSE
%python3_sitelibdir/*

%changelog
* Wed Feb 7 2024 Aleksandr A. Voyt <vojtaa@basealt.ru> 4.1-alt1 Update to latest upstream release 4.1 (closes rhbz#2239354)
- Initial build for Sisyphus
