Summary:	Poker Hand Evaluator Library
Summary(pl):	Biblioteka do gry w pokera
Name:		poker-eval
Version:	126.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.gna.org/underware/dists/%{name}-%{version}.tar.gz
# Source0-md5:	eae76bc3d4987748cf014a6b12599ea3
URL:		http://pokersource.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is loosely based on the Cliff's poker hand evaluator
library, circa 1993. It has recently been completely rewritten, to
provide improved performance, to be applicable to a wider variety of
games (including games with nonstandard decks or nonstandard rules),
and to be portable across a larger collection of platforms. The
primary audience for this package is programmers - it provides a rich
framework for writing programs about poker games, including
hypothetical games.

%description -l pl
Biblioteka bazuj�ca na bibliotece rozgrywaj�cej gr� w pokera Cliffa,
napisanej w 1993 roku. Zosta�a kompletnie przepisana aby udost�pni�
lepsz� wydajno�� i umo�liwi� korzystanie z niej w wielu grach
(w��czaj�c gry z niestandardowymi uk�adami i zasadami), oraz zwi�kszy�
przeno�no�� na wi�ksz� liczb� platform. G��wnymi u�ytkownikami tego
pakietu s� programi�ci - udost�pnia bogaty zestaw procedur do pisania
program�w o grze w pokera, w��czaj�c w to teoretyczne rozdania.

%package devel
Summary:	Headers for pokereval
Summary(pl):	Pliki nag��wkowe do pokereval
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pokereval programs.

%description devel -l pl
Pliki nag��wkowe potrzebne przy budowaniu program�w opartych na
pokereval.

%package static
Summary:	Poker-eval static library
Summary(pl):	Statyczna biblioteka Poker-eval
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Poker-eval static library.

%description static -l pl
Biblioteka Poker-eval do konsolidacji statycznej.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README TODO WHATS-HERE
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
