# revision 19717
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/automata
# catalog-date 2010-09-13 12:42:36 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-automata
Version:	0.3
Release:	2
Summary:	Finite state machines, graphs and trees in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/automata
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/automata.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/automata.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a collection of macros for MetaPost to make
easier to draw finite-state machines, automata, labelled
graphs, etc. The user defines nodes, which may be isolated or
arranged into matrices or trees; edges connect pairs of nodes
through arbitrary paths. Parameters, that specify the shapes of
nodes and the styles of edges, may be adjusted.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/automata/automata.mp
%doc %{_texmfdistdir}/doc/metapost/automata/README
%doc %{_texmfdistdir}/doc/metapost/automata/example.mp
%doc %{_texmfdistdir}/doc/metapost/automata/example.pdf
%doc %{_texmfdistdir}/doc/metapost/automata/example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 749439
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 717873
- texlive-automata
- texlive-automata
- texlive-automata
- texlive-automata
- texlive-automata

