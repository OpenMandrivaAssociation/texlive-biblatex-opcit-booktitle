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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The default citation styles verbose-trad1+; verbose-trad2 ; verbose-
trad3 use the op. cit. form in order to have a shorter reference when a
title has already been cited. However, when you cite two entries which
share the same booktitle but not the same title, the op. cit. mechanism
does not work. This package enables to obtain references like this:
Author1, Title, in Booktitle, Location, Publisher, Year, pages xxx
Author2, Title2, in Booktitle, op. cit, pages.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-opcit-booktitle
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle-example.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/documentation/makefile
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-opcit-booktitle/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-opcit-booktitle/biblatex-opcit-booktitle.sty
