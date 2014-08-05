%define Werror_cflags %nil

%define build_modules 1
%define enable_jasper 1
%define enable_graphwiz 1

%define oname GraphicsMagick
%define major 3
%define wand_major 2
%define libname %mklibname %{name} %{major}
%define libnamepp %mklibname %{name}++ %{major}
%define libwandname %mklibname graphicsmagickwand %{wand_major}
%define devname %mklibname %{name} -d
%define qlev Q8

%define __noautoprov '.*\.so$'

Summary:	An X application for displaying and manipulating images
Name:		graphicsmagick
Version:	1.3.19
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		http://www.graphicsmagick.org/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{oname}-%{version}.tar.xz
Patch0:		GraphicsMagick-1.3.14-linkage.patch
Patch1:		GraphicsMagick-1.3.19-clang.patch

BuildRequires:	bzip2-devel
BuildRequires:	ghostscript-devel
BuildRequires:	jbigkit-devel
BuildRequires:	jpeg-devel
BuildRequires:	libtool-devel
BuildRequires:	libwmf-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
Buildrequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(zlib)

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
%doc ChangeLog *.txt
%{_bindir}/gm
%dir %{_libdir}/GraphicsMagick-%{version}/config
%{_libdir}/GraphicsMagick-%{version}/config/*.mgk
%dir %{_datadir}/GraphicsMagick-%{version}/config
%{_datadir}/GraphicsMagick-%{version}/config/*.mgk
%if %{build_modules}
%dir %{_libdir}/%{oname}-%{version}/modules-%{qlev}
%{_libdir}/%{oname}-%{version}/modules-%{qlev}/filters
%dir %{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders
%{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders/*.so
%endif
%{_mandir}/man1/GraphicsMagick++-config.1.*
%{_mandir}/man1/GraphicsMagick-config.1.*
%{_mandir}/man1/GraphicsMagickWand-config.1.*
%{_mandir}/man1/gm.1.*
%{_mandir}/man4/miff.4.*
%{_mandir}/man5/quantize.5.*

#--------------------------------------------------------------

%package -n %{libname}
Summary:	%{oname} libraries
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%files -n %{libname}
%{_libdir}/libGraphicsMagick.so.%{major}*

#--------------------------------------------------------------

%package -n %{libnamepp}
Summary:	%{oname} libraries
Group:		System/Libraries
Conflicts:	%{_lib}graphicsmagick3 < 1.3.18-2

%description -n %{libnamepp}
This package contains a shared library for %{name}.

%files -n %{libnamepp}
%{_libdir}/libGraphicsMagick++.so.%{major}*

#--------------------------------------------------------------

%package -n %{libwandname}
Summary:	%{oname} libraries
Group:		System/Libraries

%description -n %{libwandname}
This package contains a shared library for %{name}.

%files -n %{libwandname}
%{_libdir}/libGraphicsMagickWand.so.%{wand_major}*

#--------------------------------------------------------------

%package -n %{devname}
Summary:	Header files for %{oname} app development
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{libnamepp} = %{version}
Requires:	%{libwandname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}.

%files -n %{devname}
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
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#--------------------------------------------------------------

%package -n perl-Graphics-Magick
Summary:	Libraries and modules for access to %{oname} from perl
Group:		Development/Perl
Requires:	%{name} = %{version}
%if %{enable_graphwiz}
Requires:	graphviz
%endif

%description -n perl-Graphics-Magick
This is the %{oname} perl support package. It includes perl modules
and support files for access to %{oname} library from perl.

%files -n perl-Graphics-Magick
%{_mandir}/man3*/*::*.3pm*
%{perl_vendorarch}/Graphics
%{perl_vendorarch}/auto

#--------------------------------------------------------------

%package doc
Summary:	%{name} Documentation
Group:		Books/Other

%description doc
This package contains HTML/PDF documentation of %{name}.

%files doc
%{_datadir}/doc/GraphicsMagick

#--------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure \
	--without-lcms \
	--enable-fast-install \
	--disable-ltdl-install \
	--without-dps \
%if %{build_modules}
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
%makeinstall_std
%makeinstall_std -C PerlMagick
rm -f %{buildroot}%{_datadir}/GraphicsMagick-%{version}/{ChangeLog,NEWS.txt}

