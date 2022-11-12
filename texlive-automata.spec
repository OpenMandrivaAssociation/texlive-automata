Name:		texlive-automata
Version:	19717
Release:	1
Summary:	Finite state machines, graphs and trees in MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/automata
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/automata.r19717.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/automata.doc.r19717.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
