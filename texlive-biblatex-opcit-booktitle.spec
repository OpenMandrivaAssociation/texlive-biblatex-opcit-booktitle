Name:		texlive-biblatex-opcit-booktitle
Version:	48983
Release:	2
Summary:	Use op. cit. for the booktitle of a subentry
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-opcit-booktitle
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-opcit-booktitle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-opcit-booktitle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The default citation styles verbose-trad1+; verbose-trad2 ;
verbose-trad3 use the op. cit. form in order to have a shorter
reference when a title has already been cited. However, when
you cite two entries which share the same booktitle but not the
same title, the op. cit. mechanism does not work. This package
enables to obtain references like this: Author1, Title, in
Booktitle, Location, Publisher, Year, pages xxx Author2,
Title2, in Booktitle, op. cit, pages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-opcit-booktitle
%doc %{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
