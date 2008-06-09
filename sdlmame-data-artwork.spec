Name:           sdlmame-data-artwork
Version:        0120
Release:        1%{?dist}
Summary:        Artwork used by the SDLMAME package

Group:          Amusements/Games
License:        Distributable
URL:            http://www.mameworld.net/mrdo/mame_artwork.html
Source0:        robby-artwork.zip
Source1:        http://www.mameworld.net/mrdo/mame_art/effect_files.zip
Source2:        %{name}-README.Artwork
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       sdlmame

%description
%{summary}.

%prep
%setup -qcT


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mame/artwork
install -d $RPM_BUILD_ROOT%{_datadir}/mame/effects
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/mame/artwork/robby.zip
unzip %{SOURCE1} -d $RPM_BUILD_ROOT%{_datadir}/mame/effects
install -pm 644 %{SOURCE2} ./README.Artwork


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.Artwork
%{_datadir}/mame


%changelog
* Sun Oct 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0120-1
- First attempt at breaking down the package into smaller pieces
