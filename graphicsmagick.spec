%define build_modules 1
%{?_with_modules: %global build_modules 1}

%define enable_jasper   1
%{?_with_jasper: %global enable_jasper 1}

%define enable_graphwiz 1
%{?_with_graphwiz: %global enable_graphwiz 1}

%define Name		GraphicsMagick
%define libname         %mklibname %name 3
%define libwandname	%mklibname graphicsmagickwand 2
%define develname	%mklibname %name -d
%define version         1.3.12
%define qlev            Q8

Summary:	An X application for displaying and manipulating images
Name:		graphicsmagick
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphics
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.graphicsmagick.org/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{Name}-%{version}.tar.lzma
Patch0: graphicsmagick-linkage_fix.diff
BuildRequires:  x11-proto-devel
BuildRequires:  perl-devel
BuildRequires:	freetype2-devel
Buildrequires:	tiff-devel
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRequires:	jasper-devel
BuildRequires:	libwmf-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	libxml2-devel
BuildRequires:	lcms-devel
BuildRequires:	libgs-devel
BuildRequires:	jbigkit-devel

%description
GraphicsMagick is the swiss army knife of image processing. It 
provides a robust collection of tools and libraries which support 
reading, writing, and manipulating an image in over 88 major formats 
including important formats like DPX, GIF, JPEG, JPEG-2000, PNG, PDF, 
SVG, and TIFF. GraphicsMagick supports huge images on systems that 
support large files, and has been tested with gigapixel-size images. 
GraphicsMagick can create new images on the fly, making it suitable 
for building dynamic Web applications. GraphicsMagick may be used to 
resize, rotate, sharpen, color reduce, or add special effects to an 
image and save the result in the same or differing image format. 
Image processing operations are available from the command line, as 
well as through C, C++, Perl, or Windows COM programming interfaces. 
Extensions are available from third-parties to support programming in 
Python, Tcl, and Ruby. With some modification, language extensions for 
ImageMagick may be used.

%files
%defattr(-,root,root)
%doc ChangeLog *.txt
%{_bindir}/gm
%dir %{_libdir}/GraphicsMagick-%{version}/config
%{_libdir}/GraphicsMagick-%{version}/config/*.mgk
%dir %{_datadir}/GraphicsMagick-%{version}/config
%{_datadir}/GraphicsMagick-%{version}/config/*.mgk
%if %build_modules
%dir %{_libdir}/%{Name}-%{version}/modules-%{qlev}
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/filters
%dir %{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders/*.so
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders/*.la
%endif
%{_mandir}/man1/GraphicsMagick++-config.1.*
%{_mandir}/man1/GraphicsMagick-config.1.*
%{_mandir}/man1/GraphicsMagickWand-config.1.*
%{_mandir}/man1/gm.1.*
%{_mandir}/man4/miff.4.*
%{_mandir}/man5/quantize.5.*

#--------------------------------------------------------------

%package -n     %{libname}
Summary:        %Name libraries
Group:          System/Libraries

%description -n %{libname}
This package contains the libraries needed to run programs dynamically
linked with ImageMagick libraries.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,755)
%{_libdir}/libGraphicsMagick++.so.3*
%{_libdir}/libGraphicsMagick.so.3*

#--------------------------------------------------------------

%package -n     %{libwandname}
Summary:        %Name libraries
Group:          System/Libraries

%description -n %{libwandname}
This package contains the libraries needed to run programs dynamically
linked with ImageMagick libraries.

%if %mdkversion < 200900
%post -n %{libwandname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libwandname} -p /sbin/ldconfig
%endif

%files -n %{libwandname}
%defattr(-,root,root,755)
%{_libdir}/libGraphicsMagickWand.so.2*

#--------------------------------------------------------------

%package -n     %{develname}
Summary: Static libraries and header files for %{Name} app development
Group: Development/C
Provides: %{name}-devel = %{version}-%{release}
Provides: %{Name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d graphicsmagick 1.1.10
Requires:  %{libname} = %{version}
Requires: %{libwandname} = %{version}
Requires:  jbig-devel
%if %{enable_jasper}
Requires: jasper-devel
%endif
%if %{enable_graphwiz}
Requires: graphviz-devel
%define _requires_exceptions devel(libcdt)\\|devel(libcircogen)\\|devel(libcommon)\\|devel(libdotgen)\\|devel(libdotneato)\\|devel(libfdpgen)\\|devel(libgraph)\\|devel(libgvrender)\\|devel(libneatogen)\\|devel(libpack)\\|devel(libpathplan)\\|devel(libtwopigen)\\|devel(libgvc)\\|devel(libgvgd)
%endif

%description -n %{develname}
If you want to create applications that will use ImageMagick code or
APIs, you'll need to install these packages as well as
ImageMagick. These additional packages aren't necessary if you simply
want to use ImageMagick, however.

imagemagick-devel is an addition to ImageMagick which includes static
libraries and header files necessary to develop applications.

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/GraphicsMagick++-config
%{_bindir}/GraphicsMagick-config
%{_bindir}/GraphicsMagickWand-config
%dir %{_includedir}/GraphicsMagick
%{_includedir}/GraphicsMagick/Magick++.h
%dir %{_includedir}/GraphicsMagick/magick
%{_includedir}/GraphicsMagick/magick/*.h
%dir %{_includedir}/GraphicsMagick/Magick++
%{_includedir}/GraphicsMagick/Magick++/*.h
%dir %{_includedir}/GraphicsMagick/wand
%{_includedir}/GraphicsMagick/wand/*.h
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#--------------------------------------------------------------

%package -n     perl-Graphics-Magick
Summary:        Libraries and modules for access to %Name from perl
Group:          Development/Perl
Requires:       %{name} = %{version}
%if %{enable_graphwiz}
Requires:       graphviz
%endif

%description -n perl-Graphics-Magick
This is the %Name perl support package. It includes perl modules
and support files for access to ImageMagick library from perl.

%files -n perl-Graphics-Magick
%defattr(-,root,root)
%{_mandir}/man3*/*::*.3pm*
%{perl_vendorarch}/Graphics
%{perl_vendorarch}/auto

#--------------------------------------------------------------

%package        doc
Summary:        %{name} Documentation
Group:          Books/Other

%description    doc
This package contains HTML/PDF documentation of %{name}.


%files doc
%defattr(-,root,root)
%_datadir/doc/GraphicsMagick

#--------------------------------------------------------------

%prep
%setup -q -n %{Name}-%{version}
%patch0 -p0 -b .linkage_fix

%build
%define Werror_cflags %nil
%configure2_5x \
    --enable-fast-install \
    --disable-ltdl-install \
    --without-dps \
%if %build_modules
    --with-modules \
%else
    --without-modules \
%endif
    --enable-shared \
    --disable-static \
    --with-pic \
%if %{enable_jasper}
    --with-jp2 \
%else
    --without-jp2 \
%endif
    --with-perl-options="INSTALLDIRS=vendor"  \
    --with-perl

%make
%make perl-build

%install
rm -rf %{buildroot}

%makeinstall_std
%makeinstall_std -C PerlMagick
rm -f %buildroot%{_datadir}/GraphicsMagick-%{version}/{ChangeLog,NEWS.txt}

%clean
rm -rf %{buildroot}
