#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jsch.agentproxy.usocket-nc
Version  : 0.0.7
Release  : 1
URL      : https://repo1.maven.org/maven2/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7/jsch.agentproxy.usocket-nc-0.0.7.jar
Source0  : https://repo1.maven.org/maven2/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7/jsch.agentproxy.usocket-nc-0.0.7.jar
Source1  : https://repo1.maven.org/maven2/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7/jsch.agentproxy.usocket-nc-0.0.7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-jsch.agentproxy.usocket-nc-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jsch.agentproxy.usocket-nc package.
Group: Data

%description data
data components for the mvn-jsch.agentproxy.usocket-nc package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7/jsch.agentproxy.usocket-nc-0.0.7.jar
/usr/share/java/.m2/repository/com/jcraft/jsch.agentproxy.usocket-nc/0.0.7/jsch.agentproxy.usocket-nc-0.0.7.pom
