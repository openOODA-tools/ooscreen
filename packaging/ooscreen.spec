Name:           ooscreen
Version:        0.1.0
Release:        1%{?dist}
Summary:        Lightweight background screen detacher with socket reconnect and credential isolation.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooscreen
Source0:        ooscreen-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooscreen is a sovereign, capability-bounded SESSION DETACHER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooscreen
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooscreen-uninstall

%files
/usr/bin/ooscreen
/usr/bin/ooscreen-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
