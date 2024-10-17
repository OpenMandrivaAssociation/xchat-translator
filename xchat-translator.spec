Summary:	An auto-translate plugin for xchat
Name:		xchat-translator
Version:	0.1
Release:	3
License:	GPL
Group:		Networking/IRC
URL:		https://code.google.com/p/gtranslatecmd/downloads/detail?name=translator.py&can=2&q=
Source0:	http://gtranslatecmd.googlecode.com/files/translator.py
Requires:	xchat
Requires:	xchat-python
Requires:	python-json
BuildArch:	noarch

%description
Translate the messages of a given user to a specified language.

Uses Google translate to do the actual magic.

Load it as so:
/LOAD %{_datadir}/xchat/translator.py


%prep

%setup -c -T

%build

%install

install -d %{buildroot}%{_datadir}/xchat
install -m0755 %{SOURCE0} %{buildroot}%{_datadir}/xchat/translator.py

%clean

%files
%{_datadir}/xchat/translator.py



