Name:       python-distro
Version:    0
Release:    1
Summary:    Renewed alternative implementation for Python's platform.linux_distribution()
Group:      Development/Tools
License:    Apache-2.0
URL:        http://sphinx.pocoo.org/
Source0:    %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel >= 2.4
BuildRequires:  python-setuptools
Requires:       python-setuptools

%description
distro (for: Linux Distribution) provides information about the Linux
distribution it runs on, such as a reliable machine-readable ID, or version
information.

It is a renewed alternative implementation for Python's original
platform.linux_distribution function, but it also provides much more
functionality which isn't necessarily Python bound like a command-line
interface.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/distro
%{python_sitelib}/*
