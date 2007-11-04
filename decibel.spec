Name: decibel
Version: 0.5.0
Release: %mkrel 3
Summary: Decibel: Realtime communications framework
License: LGPL
Group: System/Libraries
URL: http://decibel.kde.org/
Source0: %name-%version.tar.gz
BuildRequires: kde4-macros >= 3.92
BuildRequires: qt4-devel
BuildRequires: kdelibs4-devel
BuildRequires: telepathy-qt-devel 
BuildRequires: libtapioca-qt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
Obsoletes: %{_lib}decibel4

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
%_kde_bindir/decibel_logger
%_kde_bindir/minigui
%_kde_datadir/dbus-1/services/*
%_kde_datadir/Decibel
%_kde_datadir/kde4/services/*
%_kde_docdir/Decibel/demos.html
%_kde_libdir/Decibel
%_kde_libdir/kde4/*

#--------------------------------------------------------------------

%define lib_name %mklibname decibel 5

%package -n %lib_name
Summary: Headers files for %{name}
Group: System/Libraries

%description -n %lib_name
Libraries for %name

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%_kde_libdir/libdecibel.so.*

#--------------------------------------------------------------------

%package devel
Requires: %{lib_name} = %{version}
Summary: %{name} development files
Group: Development/Other
Provides: libdecibel-devel = %version
Obsoletes: %{_lib}decibel-devel
Obsoletes: %{_lib}decibel4-devel

%description devel
%{name} development files.

%files devel
%defattr(-,root,root)
%_kde_includedir/*
%_kde_libdir/*.so
%_kde_libdir/pkgconfig/*

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

