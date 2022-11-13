Name:		texlive-koma-script-examples
Version:	63833
Release:	1
Summary:	Examples from the KOMA-Script book
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/KOMA-Script-5
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script-examples.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script-examples.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This package contains some examples from the 5th edition of the
book >>KOMA-Script<<, >>Eine Sammlung von Klassen und Paketen
fur LaTeX2e<< by Markus Kohm, published by Lehmanns Media.
There are no further descriptions of these examples.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/koma-script-examples

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
