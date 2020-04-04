%{?scl:%scl_package perl-CPAN}

# Don not run gnupg1 tests by default, they need network access
# (Socket::inet_aton('pool.sks-keyservers.net')).
%bcond_with perl_CPAN_enables_gnupg_test
# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_CPAN_enables_optional_test
%else
%bcond_with perl_CPAN_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-CPAN
Version:        2.27
Release:        4%{?dist}
Summary:        Query, download and build perl modules from CPAN sites
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/CPAN
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDK/CPAN-%{version}.tar.gz
# Create site paths for the first time, bug #1158873, CPAN RT#99905
Patch0:         CPAN-2.18-Attemp-to-create-site-library-directories-on-first-t.patch
# Change configuration directory name
Patch1:         CPAN-2.18-Replace-configuration-directory-string-with-a-marke.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Path)
# Module::Signature not used
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  sed
# Optional:
BuildRequires:  %{?scl_prefix}perl(File::Spec)
# YAML::Syck is not used because @ST_PREFS is empty in Makefile.PL

# Run-time:
# Prefer Archive::Tar and Compress::Zlib over tar and gzip
BuildRequires:  %{?scl_prefix}perl(Archive::Tar) >= 1.50
%if !%{defined perl_bootstrap}
# Prefer Archive::Zip over unzip
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
BuildRequires:  %{?scl_prefix}perl(Errno)
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
# YAML::XS or YAML::Syck or JSON::PP, we already use YAML::Syck at a different
# place, keep JSON::PP optional
BuildRequires:  %{?scl_prefix}perl(lib)
# local::lib is optional
# LWP is optional, prefer HTTP::Tiny and Net::FTP
# LWP::UserAgent is optional
# Mac::BuildTools not needed
# Mac::Files not needed
# Module::Signature is optional
# Net::Config not used at tests
# Net::FTP not used at tests
# Net::Ping is required but >= 2.13 version is a soft dependency
BuildRequires:  %{?scl_prefix}perl(Net::Ping)
BuildRequires:  %{?scl_prefix}perl(overload)
# Pod::Perldoc is optional
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
#%%if !%%{defined perl_bootstrap}
# CPAN::DistnameInfo not used at tests
#%%endif
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.110350
# Crypt::OpenPGP not used at tests
# Digest::MD5 not used at tests
BuildRequires:  %{?scl_prefix}perl(Digest::SHA)
# Keep Log::Log4perl optional
# Keep MIME::Base64 optional
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Module::Build)
%endif

# Tests:
BuildRequires:  %{?scl_prefix}perl(blib)
# CPAN::Checksums not used
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(Pod::Usage)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(version)

%if %{with perl_CPAN_enables_optional_test}
# Optional tests:
%if %{with perl_CPAN_enables_gnupg_test}
BuildRequires:  %{_bindir}/gpg
# CPAN::Perl::Releases is helpfull only on RC or TRIAL Perl interpreters
# Digest::SHA1 not needed if Digest::SHA is available
# Digest::SHA::PurePerl not needed if Digest::SHA is available
%endif
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Expect)
%endif
BuildRequires:  %{?scl_prefix}perl(Hash::Util)
%if !%{defined perl_bootstrap}
# Kwalify not yet packaged
%if %{with perl_CPAN_enables_gnupg_test}
BuildRequires:  %{?scl_prefix}perl(Module::Signature) >= 0.66
%endif
BuildRequires:  %{?scl_prefix}perl(Perl::Version)
%endif
BuildRequires:  %{?scl_prefix}perl(Pod::Perldoc::ToMan)
%if %{with perl_CPAN_enables_gnupg_test}
BuildRequires:  %{?scl_prefix}perl(Socket)
%endif
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Sort::Versions)
# Test::MinimumVersion not used
# Test::Perl::Critic not used
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 0.18
BuildRequires:  %{?scl_prefix}perl(YAML) >= 0.60
%endif
%endif

Requires:       make
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Archive::Tar) >= 1.50
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(CPAN::DistnameInfo)
%endif
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
# YAML::XS or YAML::Syck or JSON::PP, we already use YAML::Syck at a different
# place, keep JSON::PP optional
Requires:       %{?scl_prefix}perl(lib)
%if !%{defined perl_bootstrap} && ! (0%{?scl:1})
Suggests:       %{?scl_prefix}perl(Log::Log4perl)
%endif
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
# Optional but highly recommended:
%if !%{defined perl_bootstrap}
# Prefer Archive::Zip over unzip
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
%if ! %{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Module::Build)
%endif
Requires:       %{?scl_prefix}perl(Pod::Perldoc)
%if ! %{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Term::ReadKey)
Requires:       %{?scl_prefix}perl(Text::Glob)
# Text::Levenshtein::XS or Text::Levenshtein::Damerau::XS or Text::Levenshtein
# or Text::Levenshtein::Damerau::PP
%if ! (0%{?scl:1})
Suggests:       %{?scl_prefix}perl(Text::Levenshtein::Damerau::XS)
# YAML::Syck or YAML or Data::Dumper or overload
Suggests:       %{?scl_prefix}perl(YAML::Syck)
%endif
%endif
Provides:       %{?scl_prefix}cpan = %{version}

# Filter non-Linux dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Mac::BuildTools\\)
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(CPAN::Meta::Requirements\\)


%description
The CPAN module automates or at least simplifies the make and install of
perl modules and extensions. It includes some primitive searching
capabilities and knows how to use LWP, HTTP::Tiny, Net::FTP and certain
external download clients to fetch distributions from the net.

%prep
%setup -q -n CPAN-%{version}
%patch0 -p1
%patch1 -p1
# Change configuration name
find -type f -exec sed -i -e 's/XCPANCONFIGNAMEX/cpan/g' {} \;
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/inc\//d' MANIFEST

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TEST CPAN_EXPECT_TIMEOUT CPAN_RUN_SHELL_TEST_WITHOUT_EXPECT \
    ftp_proxy http_proxy no_proxy \
    PERL5_CPAN_IS_RUNNING PERL5_CPAN_IS_RUNNING_IN_RECURSION PERL_CORE VERBOSE
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes PAUSE*.pub README Todo
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.27-4
- Re-rebuild of bootstrapped packages

* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.27-3
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Petr Pisar <ppisar@redhat.com> - 2.27-1
- 2.27 bump

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-2
- Perl 5.30 rebuild

* Tue Mar 19 2019 Petr Pisar <ppisar@redhat.com> - 2.26-1
- 2.26 bump

* Mon Mar 04 2019 Petr Pisar <ppisar@redhat.com> - 2.25-1
- 2.25 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Petr Pisar <ppisar@redhat.com> - 2.22-1
- 2.22 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-416
- Increase release to favour standalone package

* Wed May 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-1
- Upgrade to 2.20 as provided in perl-5.28.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-397
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Petr Pisar <ppisar@redhat.com> - 2.18-396
- Rebase patches to prevent from installing back-up files

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-393
- Perl 5.26 rebuild

* Fri May 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-2
- Don't BR: perl(Module::Build) when bootstrapping

* Wed May 10 2017 Petr Pisar <ppisar@redhat.com> - 2.18-1
- Upgrade to CPAN-2.18 as provided in perl-5.25.12

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 2.16-1
- 2.16 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Petr Pisar <ppisar@redhat.com> - 2.14-4
- Use Perl porter's fix for searching cpan -j file (CPAN RT#116507)
- Fix logging fatal errors (https://github.com/andk/cpanpm/pull/104)

* Tue Oct 18 2016 Petr Pisar <ppisar@redhat.com> - 2.14-3
- Apply remains of CVE-2016-1238 fix from perl (CPAN RT#116507)
- Do not search cpan -j file in @INC (CPAN RT#116507)

* Wed Oct 12 2016 Petr Pisar <ppisar@redhat.com> - 2.14-2
- Fix CVE-2016-1238 properly (CPAN RT#116507)

* Mon Jun 27 2016 Petr Pisar <ppisar@redhat.com> - 2.14-1
- 2.14 bump
- Fix installation from a working directory (CPAN RT#115734)
- Fix "cpan -O" invocation (CPAN RT#115786)
- Do not use Net::FTP if ftp_proxy variable points to an HTTP server
  (CPAN RT#110833)
- Recognize URL schemata disregarding the case
- Fix CVE-2016-1238 (loading optional modules from current working directory)
- Recognize exact version dependency operator (CPAN RT#47934)
- Cope with non-digit version strings

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
