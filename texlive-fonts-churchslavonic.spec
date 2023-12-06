Name:		texlive-fonts-churchslavonic
Version:	67473
Release:	1
Summary:	Fonts for typesetting in Church Slavonic language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fonts-churchslavonic
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-churchslavonic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fonts-churchslavonic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides Unicode-encoded OpenType fonts for Church
Slavonic which are intended for Unicode TeX engines only.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic
%doc %{_texmfdistdir}/doc/fonts/fonts-churchslavonic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
