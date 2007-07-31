Name:		decibel
Version:	0.5.0
Release:	%mkrel 1
Summary:	Decibel: Realtime communications framework
License:	LGPL
Group:		System/Libraries
URL:		http://decibel.kde.org/
Source0:	%name-%version.tar.gz
BuildRequires:  kde4-macros
BuildRequires:  telepathy-qt-devel 
BuildRequires:  libtapioca-qt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description

Decibel is a realtime communications framework, meant to integrate services
like CTI (Computer Telephone Integration), VoIP (Voice over IP), text based
chat and instant messaging.

End users find in Decibel one central place to manage all realtime
communication settings and can easily configure and change responses to
communication requests.

By providing a simple, DBus-based API to the services like communication
account management, connection to contacts, etc. Decibel reduces the
complexity and effort of accessing realtime communication technologies in
applications. This allows for integration of realtime communication
technologies into  applications that are not focused on communication.

Decibel consists of the desktop neutral policy daemon and desktop dependent
components. These components interact with the user and his desktop
environment by providing GUIs for common tasks like eg. creating a new
communication account, storing passwords or contacting a friend. Using the
Telepathy specification (http://telepathy.freedesktop.org/) the Decibel
daemon manages Telepathy compliant connection managers (implementing the
various communication protocols) and connects them to Decibel components as
required by the users communication needs.

%files 
%defattr(-,root,root)
%_kde_bindir/decibel
%_kde_datadir/dbus-1/services/de.basyskom.simpleclient.service
%_kde_datadir/Decibel/components/de.basyskom.simpleclient.textchannel.component
%_kde_docdir/Decibel/demos.html
%_kde_libdir/Decibel

#--------------------------------------------------------------------

%define lib_name %mklibname decibel 6


%package -n %lib_name
Summary:        Headers files for %{name}
Group:          Development/Other
Provides:       libdecibel

%description -n %lib_name
Libraries for %name

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%_kde_libdir/libdecibel.so.*

#--------------------------------------------------------------------

%define develname %mklibname decibel -d

%package  -n    %develname
Requires:       %{lib_name} = %{version}
Summary:        %{name} development files
Group:          Development/Other
Provides:       decibel-devel

%description -n %develname
%{name} development files.

%files  -n %develname
%defattr(-,root,root)

%_kde_includedir/*
%_kde_libdir/libdecibel.*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 


%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%clean
rm -rf %{buildroot}

