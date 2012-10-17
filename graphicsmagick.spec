%define	Werror_cflags	%nil

%define	build_modules	1
%define	enable_jasper	1
%define	enable_graphwiz	1

%define	major		3
%define	wand_major	2
%define	oname		GraphicsMagick
%define	libname		%mklibname %{name} %{major}
%define	libwandname	%mklibname graphicsmagickwand %{wand_major}
%define	develname	%mklibname %{name} -d
%define	qlev		Q8

Summary:	An X application for displaying and manipulating images
Name:		graphicsmagick
Version:	1.3.17
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		http://www.graphicsmagick.org/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{oname}-%{version}.tar.xz
Patch0:		GraphicsMagick-1.3.14-linkage.patch
BuildRequires:	libtool
BuildRequires:	bzip2-devel
BuildRequires:	freetype2-devel
BuildRequires:	ghostscript-devel
BuildRequires:	jasper-devel
BuildRequires:	jbigkit-devel
BuildRequires:	jpeg-devel
BuildRequires:	lcms-devel
BuildRequires:	libwmf-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl-devel
BuildRequires:	png-devel
Buildrequires:	tiff-devel
BuildRequires:	x11-proto-devel
BuildRequires:	zlib-devel

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
This package contains the libraries needed to run programs dynamically
linked with ImageMagick libraries.

%files -n %{libname}
%{_libdir}/libGraphicsMagick++.so.%{major}*
%{_libdir}/libGraphicsMagick.so.%{major}*

#--------------------------------------------------------------

%package -n %{libwandname}
Summary:	%{oname} libraries
Group:		System/Libraries

%description -n %{libwandname}
This package contains the libraries needed to run programs dynamically
linked with ImageMagick libraries.

%files -n %{libwandname}
%{_libdir}/libGraphicsMagickWand.so.%{wand_major}*

#--------------------------------------------------------------

%package -n %{develname}
Summary:	Header files for %{oname} app development
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{libwandname} = %{version}

%description -n %{develname}
If you want to create applications that will use ImageMagick code or
APIs, you'll need to install these packages as well as
ImageMagick. These additional packages aren't necessary if you simply
want to use ImageMagick, however.

imagemagick-devel is an addition to ImageMagick which includes static
libraries and header files necessary to develop applications.

%files -n %{develname}
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
%define __noautoprov Magic.so

%description -n perl-Graphics-Magick
This is the %{oname} perl support package. It includes perl modules
and support files for access to ImageMagick library from perl.

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
%patch0 -p1 -b .linkage

%build
%configure2_5x \
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
%__rm -rf %{buildroot}

%makeinstall_std
%makeinstall_std -C PerlMagick
%__rm -f %{buildroot}%{_datadir}/GraphicsMagick-%{version}/{ChangeLog,NEWS.txt}

# cleanup
%__rm -f %{buildroot}%{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders/*.*a

