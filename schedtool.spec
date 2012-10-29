%define		toolsched_version	0.16

Summary:	Tool for querying and altering scheduler parameters
Name:		schedtool
Version:	1.3.0
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://freequaos.host.sk/schedtool/%{name}-%{version}.tar.bz2
# Source0-md5:	0d968f05d3ad7675f1f33ef1f6d0a3fb
Source1:	http://ck.kolivas.org/apps/toolsched/toolsched-%{toolsched_version}.tar.bz2
# Source1-md5:	34f287b27e7f4798354b82cd7aee4034
URL:		http://freequaos.host.sk/schedtool/
# requires new sched_getaffinity prototype
BuildRequires:	glibc-devel
BuildRequires:	linux-libc-headers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schedtool can be used to query or alter scheduler parameters.

%prep
%setup -q -a1

%build
%{__make}		\
	CC="%{__cc}"	\
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install		\
	DESTDIR=$RPM_BUILD_ROOT \
	DESTPREFIX=%{_prefix}

install toolsched-%{toolsched_version}/toolsched.* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README SCHED_DESIGN TUNING toolsched-%{toolsched_version}/readme.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

