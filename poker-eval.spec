Summary:	Poker Hand Evaluator Library
Summary(pl.UTF-8):	Biblioteka do gry w pokera
Name:		poker-eval
Version:	134.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.gna.org/pokersource/sources/%{name}-%{version}.tar.gz
# Source0-md5:	aa6d39fd3b9025fb47f25009cde60d9b
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

%description -l pl.UTF-8
Biblioteka bazująca na bibliotece rozgrywającej grę w pokera Cliffa,
napisanej w 1993 roku. Została kompletnie przepisana aby udostępnić
lepszą wydajność i umożliwić korzystanie z niej w wielu grach
(włączając gry z niestandardowymi układami i zasadami), oraz zwiększyć
przenośność na większą liczbę platform. Głównymi użytkownikami tego
pakietu są programiści - udostępnia bogaty zestaw procedur do pisania
programów o grze w pokera, włączając w to teoretyczne rozdania.

%package devel
Summary:	Headers for pokereval
Summary(pl.UTF-8):	Pliki nagłówkowe do pokereval
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pokereval programs.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne przy budowaniu programów opartych na
pokereval.

%package static
Summary:	Poker-eval static library
Summary(pl.UTF-8):	Statyczna biblioteka Poker-eval
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Poker-eval static library.

%description static -l pl.UTF-8
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
