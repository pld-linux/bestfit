Summary:	bestfit - optimally choose files to be put on a CD (or other media)
Summary(pl):	bestfit - optymalne wybieranie plików do umieszczenia na CD (lub innym no¶niku)
Name:		bestfit
Version:	0.2.0
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/System
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
# Source0-md5:	9549df4aaa20e624624409694940b35c
URL:		http://www.student.lu.se/~nbi98oli/bestfit.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bestfit is a small program to determine which files that should be put
on a CD (or other media), so that as little space as possible is
wasted. It is very easy to use: you specify files on the command line,
and bestfit prints the names of those that were selected.
Alternatively, bestfit can execute a command for each selected file
(e.g. to move them to a different directory).

%description -l pl
Bestfit jest ma³ym programem do okre¶lenia, które pliki powinny byæ
umieszczone na CD (lub innym no¶niku), tak, ¿eby jak najmniejsza,
mo¿liwa ilo¶æ miejsca zosta³a zmarnowana. Jest bardzo ³atwy w u¿yciu:
pliki wyszczególnia siê w linii komend, a bestfit wy¶wietla nazwy,
które zosta³y wyselekcjonowane. Ewentualnie, bestfit mo¿e wykonaæ
komendê dla ka¿dego wyselekcjonowanego pliku (np. przenie¶æ go do
innego katalogu).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
