%define dir /usr/libexec/argo-monitoring/probes/midmon

Summary: Nagios plugins for EGI midmon tests
Name: nagios-plugins-midmon
Version: 2.0.0
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: nagios-common

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 src/*  ${RPM_BUILD_ROOT}%{dir}
install --directory --mode 770 ${RPM_BUILD_ROOT}/var/spool/nagios/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}

%changelog
* Wed Aug 14 2024 Katarina Zailac <kzailac@srce.hr> - 2.0.0-1%{?dist}
- ARGO-4602 Build nagios-plugins-midmon package for Rocky 9
* Tue Oct 18 2016 Emir Imamagic <eimamagi@srce.hr> - 1.0.0-1%{?dist}
- Initial version of Nagios plugins for EGI midmon tests
