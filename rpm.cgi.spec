Summary:	RPM.CGI is a CGI interface to the Redhat Package Management System
Summary(pl):	Interfejs CGI do zarz±dcy pakietów RPM
Name:		rpm.cgi
Version:	0.27
Release:	1
License:	GPL v2
Group:		Applications/Console
Vendor:		Abdul-Wahid Paterson <eesa@webstar.co.uk>
#ftp://eesa.webstar.co.uk/pub/rpm_cgi doesn't work
Source0:	http://rpmfind.net/linux/linuxPPC/contrib/unpackaged/%{name}-%{version}.tar.gz
URL:		http://eesa.webstar.co.uk/rpm_cgi/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	apache

%define		_rpmcgihtml	/home/services/httpd/html/rpm_cgi
%define		_rpmcgiscripts	/home/services/httpd/cgi-bin/rpm_cgi

%description
RPM.CGI is a CGI frontend to the Redhat Package Mangement System. It
provides a means to browse information about packages that are
installed on the system and to look at the information that is stored
about the package in the RPM database. It also allows browsing of the
files to see if md5 checksums, file size, file ownership etc. have
been changed since install time.

%description -l pl
RPM.CGI jest frontendem CGI na RPM. Pozwala przegl±daæ informacje o
zainstalowanych pakietach w systemie, a tak¿e sprawdzaæ, czy od czasu
zainstalowania nie zmieni³y siê pliki (sumy MD5, rozmiary,
w³a¶ciciele).

%prep
%setup -q -n rpm_cgi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_rpmcgiscripts},%{_rpmcgihtml}}

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
%config(noreplace) %verify(not size mtime md5) %{_rpmcgiscripts}/config.pm
%dir %{_rpmcgihtml}
%{_rpmcgihtml}/*
