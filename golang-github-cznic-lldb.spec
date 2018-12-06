# https://github.com/cznic/lldb
%global goipath github.com/cznic/lldb
Version:        1.1.0

%gometa

Name:           golang-github-cznic-lldb
Release:        8%{?dist}
Summary:        Low-level database engine implementation in Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/cznic/fileutil)
BuildRequires:  golang(github.com/cznic/internal/buffer)
BuildRequires:  golang(github.com/cznic/internal/file)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/cznic/sortutil)
BuildRequires:  golang(github.com/cznic/zappy)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS README.md AUTHORS


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-8
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.1.0-7
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-6
- Update to use spec 3.0.
- Disable tests due to errors with "internal" package.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- First package for Fedora

