%global pypi_name tomli_w

Name:           python-tomli-w
Version:        1.0.0
Release:        1
Summary:        A Python library for writing TOML
Group:		Development/Python
License:        MIT
URL:            https://github.com/hukkin/tomli-w
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
#BuildRequires:  pyproject-rpm-macros
BuildRequires:  python-flit-core
#BuildRequires:  python-tox
#BuildRequires:  python3dist(tox-current-env)
BuildRequires:  python3dist(tomli)
#BuildRequires:  python3dist(pytest-randomly)
#BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python-pip

%description
Tomli-W is a Python library for writing TOML. It is a write-only counterpart
to Tomli, which is a read-only TOML parser. Tomli-W is fully compatible
with TOML v1.0.0.}

%prep
%autosetup -p1 -n tomli_w-%{version}

mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl


%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE

