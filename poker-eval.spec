Summary:	Poker Hand Evaluator Library
Summary(pl):	Biblioteka do gry w pokera
Name:		poker-eval
Version:	121
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/pokersource/%{name}-src-%{version}.tar.gz
# Source0-md5:	736a8df2735442c497c508c7ac57c6f5
Source1:	poker-eval.pc
Patch0:		%{name}-no_java.patch
Patch1:		%{name}-no_msdos.patch
Patch2:		%{name}-soname.patch
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
Biblioteka bazuj±ca na bibliotece rozgrywaj±cej grê w pokera Cliffa,
napisanej w 1993 roku. Zosta³a kompletnie przepisana aby udostêpniæ
lepsz± wydajno¶æ i umo¿liwiæ korzystanie z niej w wielu grach
(w³±czajac gry z niestandardowymi uk³adami i zasadami), oraz zwiêkszyæ
przeno¶no¶æ na wiêksz± liczbê platform. G³ównymi u¿ytkownikami tego
pakietu s± programi¶ci - udostêpnia bogaty zestaw procedur do pisania
programów o grze w pokera, w³±czajac w to teoretyczne rozdania.

%package devel
Summary:	Headers for pokereval
Summary(pl):	Pliki nag³ówkowe do pokereval
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pokereval programs.

%description devel -l pl
Pliki nag³ówkowe potrzebne przy budowaniu programów opartych na
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
%setup -q -n %{name}-src-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}

%configure \
	--disable-java

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/%{name}/inlines,%{_pkgconfigdir}}
install lib/libpoker.a $RPM_BUILD_ROOT%{_libdir}
install lib/libpoker.so.* $RPM_BUILD_ROOT%{_libdir}
ln -sf libpoker.so.0 $RPM_BUILD_ROOT%{_libdir}/libpoker.so
install include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install include/inlines/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/inlines
install %{SOURCE1} $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
