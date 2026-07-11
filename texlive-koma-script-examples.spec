%global tl_name koma-script-examples
%global tl_revision 63833

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Examples from the KOMA-Script book
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/KOMA-Script-6
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script-examples.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script-examples.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains some examples from the 6th edition of the book
>>KOMA-Script<<, >>Eine Sammlung von Klassen und Paketen fur LaTeX2e<<
by Markus Kohm, published by Lehmanns Media. There are no further
descriptions of these examples.

