Summary:	RPM.CGI is a CGI interface to the Redhat Package Management System
Summary(pl.UTF-8):   Interfejs CGI do zarządcy pakietów RPM
Name:		rpm.cgi
Version:	0.27
Release:	1
License:	GPL v2
Group:		Applications/WWW
Vendor:		Abdul-Wahid Paterson <eesa@webstar.co.uk>
#ftp://eesa.webstar.co.uk/pub/rpm_cgi doesn't work
Source0:	http://rpmfind.net/linux/linuxPPC/contrib/unpackaged/%{name}-%{version}.tar.gz
# Source0-md5:	8d4b6f4a4b578e646ef111e21eac63e8
URL:		http://eesa.webstar.co.uk/rpm_cgi/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	webserver = apache
BuildArch:	noarch

%define		_rpmcgihtml	/home/services/httpd/html/rpm_cgi
%define		_rpmcgiscripts	/home/services/httpd/cgi-bin/rpm_cgi

%description
RPM.CGI is a CGI frontend to the Redhat Package Mangement System. It
provides a means to browse information about packages that are
installed on the system and to look at the information that is stored
about the package in the RPM database. It also allows browsing of the
files to see if md5 checksums, file size, file ownership etc. have
been changed since install time.

%description -l pl.UTF-8
RPM.CGI jest frontendem CGI na RPM. Pozwala przeglądać informacje o
zainstalowanych pakietach w systemie, a także sprawdzać, czy od czasu
zainstalowania nie zmieniły się pliki (sumy MD5, rozmiary,
właściciele).

%prep
%setup -q -n rpm_cgi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_rpmcgiscripts},%{_rpmcgihtml}}

sed 's/home\/httpd/home\/services\/httpd/' config.pm > config.pm.tmp
mv -f config.pm.tmp config.pm
install rpm.cgi text_conv.pm config.pm $RPM_BUILD_ROOT%{_rpmcgiscripts}
install images/*.{jpg,gif} $RPM_BUILD_ROOT%{_rpmcgihtml}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README ChangeLog BUGS
%dir %{_rpmcgiscripts}
%attr(755,root,root) %{_rpmcgiscripts}/rpm.cgi
%{_rpmcgiscripts}/text_conv.pm
%config(noreplace) %verify(not md5 mtime size) %{_rpmcgiscripts}/config.pm
%dir %{_rpmcgihtml}
%{_rpmcgihtml}/*
