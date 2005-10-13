Summary:	GKrellM - themes
Summary(pl):	GKrellM - motywy
Name:		gkrellm-themes
Version:	0.10
Release:	3	
License:	distributable
Group:		X11/Applications
Source0:	http://www.muhri.net/gkrellm/MonkeyLovers.tar.gz
# Source0-md5:	ff726c78469b5fcb6e9e243b6f62625d
Source1:	http://www.muhri.net/gkrellm/Yellow.tar.gz
# Source1-md5:	d3207003bc97fb869fd59c5c8bfea6e0
Source2:	http://www.muhri.net/gkrellm/niumx.tar.gz
# Source2-md5:	681703107d566ffd1c36adcb1aec7ebf
Source3:	http://www.muhri.net/gkrellm/milk.tar.gz
# Source3-md5:	692084816a4f3c782f272bb9317de814
Source4:	http://www.muhri.net/gkrellm/keramik.tar.gz
# Source4-md5:	6367a8e8cc17f1a05d0081a084b69f86
Source5:	http://www.muhri.net/gkrellm/yummiyogurt.tar.gz
# Source5-md5:	31f7115b80dc2184685225a5684fef42
Source6:	http://www.muhri.net/gkrellm/prime23.tar.gz
# Source6-md5:	68b1e9d8dad1389950e254bf7946599d
Source7:	http://www.muhri.net/gkrellm/minE-Gkrellm.tar.gz
# Source7-md5:	2e83a086214b4fa2990355957a1e5a5f
Source8:	http://freshmeat.net/redir/klearllm/42537/url_tgz/klearllm-default-0.9.1.tar.gz
# Source8-md5:	f5a260040d4a88e5803b9289c5e63ad1
URL:		http://www.gkrellm.net/
Requires:	gkrellm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gkrellm-theme

%define		_themedir	%{_prefix}/share/gkrellm2/themes

%description
Additional themes for GKrellM.

%description -l pl
Dodatkowe motywy dla GKrellM.

%package -n gkrellm-theme-MonkeyLovers
Summary:	MonkeyLovers theme
Summary(pl):	Motyw MonkeyLovers
Group:		X11/Applications
Requires:	gkrellm
Provides:	gkrellm-theme
Obsoletes:	gkrellm-themes

%description -n gkrellm-theme-MonkeyLovers
MonkeyLovers theme.

%description -n gkrellm-theme-MonkeyLovers -l pl
Motyw MonkeyLovers.

%package -n gkrellm-theme-Yellow
Summary:	Yellow theme
Summary(pl):	Motyw Yellow
Group:		X11/Applications
Requires:	gkrellm
Provides:	gkrellm-theme
Obsoletes:	gkrellm-themes

%description -n gkrellm-theme-Yellow
Yellow theme.

%description -n gkrellm-theme-Yellow -l pl
Motyw Yellow.

%package -n gkrellm-theme-niumx
Summary:        Niumx theme
Summary(pl):    Motyw Niumx
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-niumx
Niumx theme.   

%description -n gkrellm-theme-niumx -l pl
Motyw Niumx.

%package -n gkrellm-theme-Milk
Summary:        Milk theme
Summary(pl):    Motyw Milk
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-Milk
Milk theme.

%description -n gkrellm-theme-Milk -l pl
Motyw Milk.

%package -n gkrellm-theme-keramik
Summary:        Keramik theme
Summary(pl):    Motyw keramik
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-keramik
Keramik theme.

%description -n gkrellm-theme-keramik -l pl
Motyw Keramik.

%package -n gkrellm-theme-yummiyogurt
Summary:        Yummiyogurt theme
Summary(pl):    Motyw Yummiyogurt
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-yummiyogurt
Yummiyogurt theme.

%description -n gkrellm-theme-yummiyogurt -l pl
Motyw Yummiyogurt.

%package -n gkrellm-theme-prime_23
Summary:        Prime23 theme
Summary(pl):    Motyw prime23
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-prime_23
Prime23 theme.

%description -n gkrellm-theme-prime_23 -l pl
Motyw prime23.

%package -n gkrellm-theme-minE-Gkrellm
Summary:        minE-Gkrellm theme
Summary(pl):    Motyw minE-Gkrellm
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-minE-Gkrellm
minE-Gkrellm theme.

%description -n gkrellm-theme-minE-Gkrellm -l pl
Motyw minE-Gkrellm.

%package -n gkrellm-theme-klearllm                                                                                
Summary:        Klearllm is a simple, transparent skin for Gkrellm
Summary(pl):    Klearllm jest prostym, prze¼roczystym motywem dla Gkrellm
Group:          X11/Applications
Requires:       gkrellm
Provides:       gkrellm-theme
Obsoletes:      gkrellm-themes

%description -n gkrellm-theme-klearllm
Klearllm is a simple, transparent skin for Gkrellm that has 3 different
text color schemes.

%description -n gkrellm-theme-klearllm -l pl
Klearllm jest prostym, prze¼roczystym motywem dla Gkrellm, który posiada
3 ró¿ne zestawy kolorów tekstu.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}

gzip -dc %{SOURCE0} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE1} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE2} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE3} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE4} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE5} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE6} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE7} | tar -x -C $RPM_BUILD_ROOT%{_themedir}
gzip -dc %{SOURCE8} | tar -x -C $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themedir}/*

%files -n gkrellm-theme-MonkeyLovers
%defattr(644,root,root,755)
%{_themedir}/MonkeyLovers

%files -n gkrellm-theme-Yellow
%defattr(644,root,root,755)
%{_themedir}/Yellow

%files -n gkrellm-theme-niumx
%defattr(644,root,root,755)
%{_themedir}/niumx

%files -n gkrellm-theme-Milk
%defattr(644,root,root,755)
%{_themedir}/Milk

%files -n gkrellm-theme-keramik
%defattr(644,root,root,755)
%{_themedir}/keramik

%files -n gkrellm-theme-yummiyogurt
%defattr(644,root,root,755)
%{_themedir}/yummiyogurt

%files -n gkrellm-theme-prime_23
%defattr(644,root,root,755)
%{_themedir}/prime_23

%files -n gkrellm-theme-minE-Gkrellm
%defattr(644,root,root,755)
%{_themedir}/minE-Gkrellm

%files -n gkrellm-theme-klearllm
%defattr(644,root,root,755)
%{_themedir}/klearllm
