%global tl_name biblatex-opcit-booktitle
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.0
Release:	%{tl_revision}.1
Summary:	Use op. cit. for the booktitle of a subentry
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-opcit-booktitle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-opcit-booktitle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-opcit-booktitle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The default citation styles verbose-trad1+; verbose-trad2 ; verbose-
trad3 use the op. cit. form in order to have a shorter reference when a
title has already been cited. However, when you cite two entries which
share the same booktitle but not the same title, the op. cit. mechanism
does not work. This package enables to obtain references like this:
Author1, Title, in Booktitle, Location, Publisher, Year, pages xxx
Author2, Title2, in Booktitle, op. cit, pages.

