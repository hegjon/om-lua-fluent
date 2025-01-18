%global forgeurl https://github.com/alerque/fluent-lua
%global tag v%{version}

%define lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%define lua_pkgdir %{_datadir}/lua/%{lua_version}

Name:      lua-fluent
Version:   0.2.0
Release:   1
Summary:   Lua implementation of Project Fluent
Group:     Development/Other
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildArch:     noarch
BuildRequires: lua-devel
Requires:      lua-cldr
Requires:      lua-epnf
Requires:      lua-penlight

# Tests
BuildRequires: lua-cldr
BuildRequires: lua-epnf
BuildRequires: lua-penlight

%description
A Lua implementation of Project Fluent, a localization paradigm designed to
unleash the entire expressive power of natural language translations.
Fluent is a family of localization specifications, implementations and good
practices developed by Mozilla who extracted parts of their 'l20n' solution
(used in Firefox and other apps) into a re-usable specification.


%prep
%forgesetup


%build
# Nothing to do here


%install
install -dD %{buildroot}%{lua_pkgdir}
cp -av fluent/ %{buildroot}%{lua_pkgdir}


%check
# Smoke test for now, missing dependency busted for test suite
LUA_PATH="%{buildroot}%{lua_pkgdir}/?.lua;%{buildroot}%{lua_pkgdir}/?/init.lua;;" \
lua -e '
local FluentBundle = require("fluent")
local bundle = FluentBundle()

bundle:add_messages([[
hello = Hello { $name }!
foo = bar
    .attr = baz
]])

print(bundle:format("foo"))
print(bundle:format("foo.attr"))
print(bundle:format("hello", { name = "World" }))
'


%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{lua_pkgdir}/fluent/
