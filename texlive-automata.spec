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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a collection of macros for MetaPost to make easier to
draw finite-state machines, automata, labelled graphs, etc. The user
defines nodes, which may be isolated or arranged into matrices or trees;
edges connect pairs of nodes through arbitrary paths. Parameters, that
specify the shapes of nodes and the styles of edges, may be adjusted.

