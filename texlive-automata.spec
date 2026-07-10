%global tl_name automata
%global tl_revision 19717

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Finite state machines, graphs and trees in MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/automata
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/automata.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/automata.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a collection of macros for MetaPost to make easier to
draw finite-state machines, automata, labelled graphs, etc. The user
defines nodes, which may be isolated or arranged into matrices or trees;
edges connect pairs of nodes through arbitrary paths. Parameters, that
specify the shapes of nodes and the styles of edges, may be adjusted.

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
%dir %{_datadir}/texmf-dist/metapost
%dir %{_datadir}/texmf-dist/doc/metapost
%dir %{_datadir}/texmf-dist/metapost/automata
%dir %{_datadir}/texmf-dist/doc/metapost/automata
%doc %{_datadir}/texmf-dist/doc/metapost/automata/README
%doc %{_datadir}/texmf-dist/doc/metapost/automata/example.mp
%doc %{_datadir}/texmf-dist/doc/metapost/automata/example.pdf
%doc %{_datadir}/texmf-dist/doc/metapost/automata/example.tex
%{_datadir}/texmf-dist/metapost/automata/automata.mp
