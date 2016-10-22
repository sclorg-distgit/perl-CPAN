%{?scl:%scl_package perl-CPAN}

%global base_version 2.10

Name:           %{?scl_prefix}perl-CPAN
Version:        2.11
Release:        368%{?dist}
Summary:        Query, download and build perl modules from CPAN sites
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CPAN/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDK/CPAN-%{base_version}.tar.gz
# Unbundled from perl 5.21.11
Patch0:         CPAN-2.10-Upgrade-to-2.11.patch
# Create site paths for the first time, bug #1158873, CPAN RT#99905
Patch1:         CPAN-2.11-Attemp-to-create-site-library-directories-on-first-t.patch
# Change configuration directory name
Patch2:         CPAN-2.11-Replace-configuration-directory-string-with-a-marke.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  sed
# Optional:
BuildRequires:  %{?scl_prefix}perl(File::Spec)
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(YAML::Syck)
%endif

# Run-time:
# Prefer Archive::Tar and Compress::Zlib over tar and gzip
BuildRequires:  %{?scl_prefix}perl(Archive::Tar) >= 1.50
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Archive::Zip)
%endif
BuildRequires:  %{?scl_prefix}perl(autouse)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Compress::Zlib)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
# Devel::Size not used at tests
BuildRequires:  %{?scl_prefix}perl(DirHandle)
BuildRequires:  %{?scl_prefix}perl(Dumpvalue)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# ExtUtils::Manifest not used at tests
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Find)
# File::HomeDir 0.65 not used at tests
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.16
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(Getopt::Std)
# HTTP::Date is optional, prefer in-core Time::Local
# HTTP::Request is optional
BuildRequires:  %{?scl_prefix}perl(HTTP::Tiny) >= 0.005
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(lib)
# local::lib is optional
# LWP is optional, prefer HTTP::Tiny and Net::FTP
# LWP::UserAgent is optional
# Mac::BuildTools not needed
# Mac::Files not needed
# Module::Signature is optional
# Net::Config not used at tests
# Net::FTP not used at tests
BuildRequires:  %{?scl_prefix}perl(Net::Ping)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Safe)
BuildRequires:  %{?scl_prefix}perl(Sys::Hostname)
BuildRequires:  %{?scl_prefix}perl(Term::ReadLine)
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
BuildRequires:  %{?scl_prefix}perl(Text::Wrap)
# Time::Local not used at tests
# URI not used at tests
# URI::Escape not used at tests
# URI::URL 0.08 is optional 
# User::pwent not used at tests
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional:
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.110350
# Crypt::OpenPGP not used at tests
# Digest::MD5 not used at tests
BuildRequires:  %{?scl_prefix}perl(Digest::SHA)
# Keep MIME::Base64 optional
BuildRequires:  %{?scl_prefix}perl(Module::Build)

# Tests:
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(Pod::Usage)
BuildRequires:  %{?scl_prefix}perl(Test::More)

# Optional tests:
BuildRequires:  %{?scl:%{_root_bindir}}%{?!scl:%{_bindir}}/gpg
# Digest::SHA1 not needed if Digest::SHA is available
# Digest::SHA::PurePerl not needed if Digest::SHA is available
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Expect)
%endif
BuildRequires:  %{?scl_prefix}perl(Hash::Util)
%if !%{defined perl_bootstrap} && !%{defined perl_small}
# Kwalify not yet packaged
BuildRequires:  %{?scl_prefix}perl(Module::Signature) >= 0.66
BuildRequires:  %{?scl_prefix}perl(Perl::Version)
%endif
BuildRequires:  %{?scl_prefix}perl(Socket)
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Sort::Versions)
# Test::MinimumVersion not used
# Test::Perl::Critic not used
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 0.18
BuildRequires:  %{?scl_prefix}perl(YAML) >= 0.60
%endif

Requires:       make
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Archive::Tar) >= 1.50
Requires:       %{?scl_prefix}perl(CPAN::Meta::Requirements) >= 2.121
Requires:       %{?scl_prefix}perl(Data::Dumper)
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Devel::Size)
%endif
Requires:       %{?scl_prefix}perl(ExtUtils::Manifest)
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(File::HomeDir) >= 0.65
%endif
Requires:       %{?scl_prefix}perl(File::Temp) >= 0.16
Requires:       %{?scl_prefix}perl(lib)
Requires:       %{?scl_prefix}perl(Net::Config)
Requires:       %{?scl_prefix}perl(Net::FTP)
Requires:       %{?scl_prefix}perl(POSIX)
Requires:       %{?scl_prefix}perl(Term::ReadLine)
Requires:       %{?scl_prefix}perl(Time::Local)
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(URI)
Requires:       %{?scl_prefix}perl(URI::Escape)
%endif
Requires:       %{?scl_prefix}perl(User::pwent)
# Optional but higly recommended:
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Archive::Zip)
Requires:       %{?scl_prefix}perl(Compress::Bzip2)
Requires:       %{?scl_prefix}perl(CPAN::Meta) >= 2.110350
%endif
Requires:       %{?scl_prefix}perl(Compress::Zlib)
Requires:       %{?scl_prefix}perl(Digest::MD5)
# CPAN encourages Digest::SHA strongly because of integrity checks
Requires:       %{?scl_prefix}perl(Digest::SHA)
Requires:       %{?scl_prefix}perl(Dumpvalue)
Requires:       %{?scl_prefix}perl(ExtUtils::CBuilder)
%if ! %{defined perl_bootstrap}
# Avoid circular deps local::lib -> Module::Install -> CPAN when bootstraping
# local::lib recommended by CPAN::FirstTime default choice, bug #1122498
Requires:       %{?scl_prefix}perl(local::lib)
%endif
Requires:       %{?scl_prefix}perl(Module::Build)
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Text::Glob)
%endif
Provides:       %{?scl_prefix}cpan = %{version}

%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
# Filter non-Linux dependencies
%filter_from_requires /^%{?scl_prefix}perl(Mac::BuildTools)/d
# Filter under-specified dependencies
%filter_from_requires /^%{?scl_prefix}perl(CPAN::Meta::Requirements)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
# Filter non-Linux dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Mac::BuildTools\\)
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(CPAN::Meta::Requirements\\)
%endif


%description
The CPAN module automates or at least simplifies the make and install of
perl modules and extensions. It includes some primitive searching
capabilities and knows how to use LWP, HTTP::Tiny, Net::FTP and certain
external download clients to fetch distributions from the net.

%prep
%setup -q -n CPAN-%{base_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
# Change configuration name
find -type f -exec sed -i -e 's/XCPANCONFIGNAMEX/cpan%{?scl:-%{scl}}/g' {} \;
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/inc\//d' MANIFEST

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes PAUSE*.pub README Todo
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sun Jul 24 2016 Petr Pisar <ppisar@redhat.com> - 2.11-368
- Rebuild without bootstrap

* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 2.11-367
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-349
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Petr Pisar <ppisar@redhat.com> - 2.11-348
- Require make package

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-345
- Increase release to favour standalone package

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.11-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 2.11-1
- 2.11 bump in order to dual-live with perl 5.22

* Fri Mar 13 2015 Petr Pisar <ppisar@redhat.com> - 2.10-1
- 2.10 bump

* Wed Jan 28 2015 Petr Pisar <ppisar@redhat.com> - 2.05-309
- Allow changing the configuration directory name

* Thu Oct 30 2014 Petr Pisar <ppisar@redhat.com> - 2.05-308
- Create site paths for the first time (bug #1158873)

* Wed Sep 10 2014 Petr Pisar <ppisar@redhat.com> 2.05-307
- Synchronize to perl.spec modifications
- Disable non-core modules when bootstrapping

* Tue Apr 22 2014 Petr Pisar <ppisar@redhat.com> 2.05-1
- Specfile autogenerated by cpanspec 1.78.
