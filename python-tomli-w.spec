%global pypi_name tomli_w

Name:           python-tomli-w
Version:        1.2.0
Release:        1
Summary:        A Python library for writing TOML
Group:		Development/Python
License:        MIT
URL:            https://github.com/hukkin/tomli-w
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	python
BuildSystem:	python
BuildRequires:  python%{pyver}dist(tomli)

%description
Tomli-W is a Python library for writing TOML. It is a write-only counterpart
to Tomli, which is a read-only TOML parser. Tomli-W is fully compatible
with TOML v1.0.0.

%files
%doc README.md
%license LICENSE
%{python_sitelib}/tomli_w-%{version}.dist-info
%{python_sitelib}/tomli_w/
