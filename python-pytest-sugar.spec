#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin changing default look and feel of pytest
Summary(pl.UTF-8):	Wtyczka pytesta zmieniająca domyślny wygląd i zachowanie
Name:		python-pytest-sugar
Version:	0.9.4
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-sugar/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-sugar/pytest-sugar-%{version}.tar.gz
# Source0-md5:	34d13e153527aff4442212465b3f2f89
URL:		https://pypi.org/project/pytest-sugar/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-packaging >= 14.1
BuildRequires:	python-pytest >= 2.9
BuildRequires:	python-termcolor >= 1.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-packaging >= 14.1
BuildRequires:	python3-pytest >= 2.9
BuildRequires:	python3-pytest-xdist
BuildRequires:	python3-termcolor >= 1.1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-sugar is a plugin for pytest that changes the default look and
feel of pytest (e.g. progressbar, show tests that fail instantly).

%description -l pl.UTF-8
pytest-sugar to wtyczka pytesta zmieniająca domyślny wygląd i
zachowanie pytesta (m.in. pasek postępu, natychmiastowe pokazywanie
testów zakończonych niepowodzeniem).

%package -n python3-pytest-sugar
Summary:	pytest plugin changing default look and feel of pytest
Summary(pl.UTF-8):	Wtyczka pytesta zmieniająca domyślny wygląd i zachowanie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-sugar
pytest-sugar is a plugin for pytest that changes the default look and
feel of pytest (e.g. progressbar, show tests that fail instantly).

%description -n python3-pytest-sugar -l pl.UTF-8
pytest-sugar to wtyczka pytesta zmieniająca domyślny wygląd i
zachowanie pytesta (m.in. pasek postępu, natychmiastowe pokazywanie
testów zakończonych niepowodzeniem).

%prep
%setup -q -n pytest-sugar-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_sugar" \
%{__python} -m pytest test_sugar.py -k 'not test_xdist and not test_xdist_verbose'
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_sugar,xdist.plugin" \
%{__python3} -m pytest test_sugar.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.rst LICENSE README.md
%{py_sitescriptdir}/pytest_sugar.py[co]
%{py_sitescriptdir}/pytest_sugar-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-sugar
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.rst LICENSE README.md
%{py3_sitescriptdir}/pytest_sugar.py
%{py3_sitescriptdir}/__pycache__/pytest_sugar.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_sugar-%{version}-py*.egg-info
%endif
