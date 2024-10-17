%define svn 889077

Name: decibel
Version: 0.7.1
Release: %mkrel 0.%svn.3
Summary: Decibel: Realtime communications framework
License: LGPL
Group: System/Libraries
URL: https://decibel.kde.org/
Source0: %name-%version.%svn.tar.bz2
Patch0: decibel-0.7.1-gcc44.patch
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
%_kde_bindir/textchannelgui
%_kde_datadir/dbus-1/services/*
%_kde_datadir/Decibel
%_kde_docdir/Decibel/demos.html
%_kde_libdir/Decibel

#--------------------------------------------------------------------

%define  Decibel_major 0
%define  libDecibel %mklibname Decibel %Decibel_major


%package -n %libDecibel
Summary: Headers files for %{name}
Group: System/Libraries
Obsoletes:  %{_lib}decibel5 < 0.7.0-0.831027.1

%description -n %libDecibel
Libraries for %name

%files -n %libDecibel
%defattr(-,root,root)
%_kde_libdir/libDecibel.so.*

#--------------------------------------------------------------------

%define decibel_pluginhelper_major 0
%define libdecibel_pluginhelper %mklibname decibel_pluginhelper %decibel_pluginhelper_major

%package -n %libdecibel_pluginhelper
Summary: Headers files for %{name}
Group: System/Libraries

%description -n %libdecibel_pluginhelper
Libraries for %name

%files -n %libdecibel_pluginhelper
%defattr(-,root,root)
%_kde_libdir/libdecibel_pluginhelper.so.*

#--------------------------------------------------------------------

%package devel
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
%setup -q -n %name
%patch0 -p1 -b .gcc44

%build
%cmake_kde4 

%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%clean
rm -rf %{buildroot}

