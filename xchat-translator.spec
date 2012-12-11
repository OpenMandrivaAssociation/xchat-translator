Summary:	An auto-translate plugin for xchat
Name:		xchat-translator
Version:	0.1
Release:	%mkrel 2
License:	GPL
Group:		Networking/IRC
URL:		http://code.google.com/p/gtranslatecmd/downloads/detail?name=translator.py&can=2&q=
Source0:	http://gtranslatecmd.googlecode.com/files/translator.py
Requires:	xchat
Requires:	xchat-python
Requires:	python-json
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Translate the messages of a given user to a specified language.

Uses Google translate to do the actual magic.

Load it as so:
/LOAD %{_datadir}/xchat/translator.py


%prep

%setup -c -T

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/xchat
install -m0755 %{SOURCE0} %{buildroot}%{_datadir}/xchat/translator.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/xchat/translator.py



%changelog
* Mon Sep 12 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdv2012.0
+ Revision: 699509
- fix bork by OmGnH

* Tue Sep 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-1
+ Revision: 698429
- import xchat-translator


* Tue Sep 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdv2010.2
- initial Mandriva package
