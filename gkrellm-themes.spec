Summary:	GKrellM - themes
Summary(pl):	GKrellM - tematy
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
Addotional themes for GKrellM.

%description -l pl
Dodtatkowe tematy dla GKrellM.

%package -n gkrellm-theme-MonkeyLovers
Summary:	MonkeyLovers theme
Summary(pl):	Temat MonkeyLovers
Group:		X11/Applications

%description -n gkrellm-theme-MonkeyLovers
MonkeyLovers theme.

%description -n gkrellm-theme-MonkeyLovers -l pl
Temat MonkeyLovers.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}

gzip -dc %{SOURCE0} | tar -x -C $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n gkrellm-theme-MonkeyLovers
%defattr(644,root,root,755)
%{_themedir}/MonkeyLovers

%files
%defattr(644,root,root,755)
%{_themedir}/*
