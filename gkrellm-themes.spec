Summary:	GKrellM - themes
Summary(pl):	GKrellM - motywy
Name:		gkrellm-themes
Version:	0.10
Release:	0.1
License:	distributable
Group:		X11/Applications
Source0:	http://www.muhri.net/gkrellm/MonkeyLovers.tar.gz
# Source0-md5:	ff726c78469b5fcb6e9e243b6f62625d
URL:		http://www.gkrellm.net/
Requires:	gkrellm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir	%{_prefix}/share/gkrellm2/themes

%description
Additional themes for GKrellM.

%description -l pl
Dodatkowe motywy dla GKrellM.

%package -n gkrellm-theme-MonkeyLovers
Summary:	MonkeyLovers theme
Summary(pl):	Motyw MonkeyLovers
Group:		X11/Applications

%description -n gkrellm-theme-MonkeyLovers
MonkeyLovers theme.

%description -n gkrellm-theme-MonkeyLovers -l pl
Motyw MonkeyLovers.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}

gzip -dc %{SOURCE0} | tar -x -C $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

# XXX: (partially???) duplicates subpackage with no Obsoletes/Conflicts
%files
%defattr(644,root,root,755)
%{_themedir}/*

%files -n gkrellm-theme-MonkeyLovers
%defattr(644,root,root,755)
%{_themedir}/MonkeyLovers
