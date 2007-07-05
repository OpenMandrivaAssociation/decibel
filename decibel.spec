%define lib_name_orig %mklibname %name
%define lib_major 4
%define lib_name %lib_name_orig%lib_major

Summary:	Decibel: Realtime communications framework
Name:		decibel
Version:	0.4.0
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://decibel.kde.org/
Source0:	%name-%version.tar.gz
Requires:	%lib_name = %version
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

#--------------------------------------------------------------------

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
%_kde_libdir/libdecibel.so.0.4.0
%_kde_libdir/Decibel/decibel_chatstarter_demo
%_kde_libdir/Decibel/decibel_defaultcmfor_demo
%_kde_libdir/Decibel/decibel_deleteaccount_demo
%_kde_libdir/Decibel/decibel_listaccounts_demo
%_kde_libdir/Decibel/decibel_listcms_demo
%_kde_libdir/Decibel/decibel_listcmsfor_demo
%_kde_libdir/Decibel/decibel_phonestarter_demo
%_kde_libdir/Decibel/decibel_registeraccount_demo
%_kde_libdir/Decibel/decibel_setdefaultcmfor_demo
%_kde_libdir/Decibel/decibel_setpresence_demo
%_kde_libdir/Decibel/decibel_simpleclient_demo
%_kde_libdir/Decibel/decibel_supportedprotocols_demo

#--------------------------------------------------------------------

%package  -n    %lib_name-devel
Requires:       %{lib_name} = %{version}
Summary:        %{name} development files
Group:          Development/Other
Provides:       decibel-devel

%description -n %lib_name-devel
%{name} development files.

%files  -n %lib_name-devel
%defattr(-,root,root)

%_kde_includedir/Decibel/AccountData
%_kde_includedir/Decibel/AccountManager
%_kde_includedir/Decibel/ChannelHandler
%_kde_includedir/Decibel/ComponentManager
%_kde_includedir/Decibel/ContactManager
%_kde_includedir/Decibel/DBusNames
%_kde_includedir/Decibel/Errors
%_kde_includedir/Decibel/ProtocolManager
%_kde_includedir/Decibel/Types
%_kde_includedir/Decibel/accountdata.h
%_kde_includedir/Decibel/accountmanager.h
%_kde_includedir/Decibel/channelhandler.h
%_kde_includedir/Decibel/componentmanager.h
%_kde_includedir/Decibel/contactmanager.h
%_kde_includedir/Decibel/dbusnames.h
%_kde_includedir/Decibel/decibel_export.h
%_kde_includedir/Decibel/errors.h
%_kde_includedir/Decibel/protocolmanager.h
%_kde_includedir/Decibel/types.h
%_kde_libdir/libdecibel.so
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
