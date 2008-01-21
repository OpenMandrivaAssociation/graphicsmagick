%define build_modules 1
%{?_with_modules: %global build_modules 1}

%define enable_jasper   1
%{?_with_jasper: %global enable_jasper 1}

%define enable_graphwiz 1
%{?_with_graphwiz: %global enable_graphwiz 1}

%define Name		GraphicsMagick
%define libname         %mklibname %name %{major}
%define version         1.1.10
%define major           %version
%define qlev            Q8

Summary:	An X application for displaying and manipulating images
Name:		graphicsmagick	
Version:	%{version}
Release:	%mkrel 2
License:	GPL
Group:		Graphics
URL:		http://www.graphicsmagick.org/
Source0:	http://kent.dl.sourceforge.net/sourceforge/graphicsmagick/%{Name}-%{version}.tar.bz2

BuildRequires:  x11-proto-devel
BuildRequires:  perl-devel

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
%{_bindir}/gm
%dir %{_libdir}/GraphicsMagick-1.1.10/config
%{_libdir}/GraphicsMagick-1.1.10/config/*.mgk
%if %build_modules
%dir %{_libdir}/%{Name}-%{version}/modules-%{qlev}
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/filters
%dir %{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders/*.so
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders/*.la
%{_libdir}/%{Name}-%{version}/modules-%{qlev}/coders/*.a
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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,755)
%{_libdir}/libGraphicsMagick++.so.1
%{_libdir}/libGraphicsMagick++.so.1.0.3
%{_libdir}/libGraphicsMagick.so.1
%{_libdir}/libGraphicsMagick.so.1.0.10
%{_libdir}/libGraphicsMagickWand.so.0
%{_libdir}/libGraphicsMagickWand.so.0.0.4

#--------------------------------------------------------------

%package -n     %{libname}-devel
Summary:        Static libraries and header files for %{Name} app development
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{Name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}
Requires:       libjbig-devel
%if %{enable_jasper}
Requires:       libjasper-devel
%endif
%if %{enable_graphwiz}
Requires:       libgraphviz-devel
%define _requires_exceptions devel(libcdt)\\|devel(libcircogen)\\|devel(libcommon)\\|devel(libdotgen)\\|devel(libdotneato)\\|devel(libfdpgen)\\|devel(libgraph)\\|devel(libgvrender)\\|devel(libneatogen)\\|devel(libpack)\\|devel(libpathplan)\\|devel(libtwopigen)\\|devel(libgvc)\\|devel(libgvgd)
%endif

%description -n %{libname}-devel
If you want to create applications that will use ImageMagick code or
APIs, you'll need to install these packages as well as
ImageMagick. These additional packages aren't necessary if you simply
want to use ImageMagick, however.

ImageMagick-devel is an addition to ImageMagick which includes static
libraries and header files necessary to develop applications.

%files -n %{libname}-devel
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
%{_libdir}/*.a
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
%dir %{_datadir}/GraphicsMagick-1.1.10
%{_datadir}/GraphicsMagick-1.1.10/Copyright.txt
%{_datadir}/GraphicsMagick-1.1.10/config/*.mgk
%{_datadir}/GraphicsMagick-1.1.10/images/*.png
%{_datadir}/GraphicsMagick-1.1.10/images/*.jpg
%{_datadir}/GraphicsMagick-1.1.10/*.html
%dir %{_datadir}/GraphicsMagick-1.1.10/www
%{_datadir}/GraphicsMagick-1.1.10/www/*.css
%{_datadir}/GraphicsMagick-1.1.10/www/*.c
%{_datadir}/GraphicsMagick-1.1.10/www/*.html
%dir %{_datadir}/GraphicsMagick-1.1.10/www/Magick++
%{_datadir}/GraphicsMagick-1.1.10/www/Magick++/*.html
%{_datadir}/GraphicsMagick-1.1.10/www/Magick++/*.jpg
%{_datadir}/GraphicsMagick-1.1.10/www/Magick++/*.fig
%{_datadir}/GraphicsMagick-1.1.10/www/Magick++/*.png
%{_datadir}/GraphicsMagick-1.1.10/www/Magick++/*.svg
%{_datadir}/GraphicsMagick-1.1.10/www/Magick++/*.txt
%dir %{_datadir}/GraphicsMagick-1.1.10/www/api
%{_datadir}/GraphicsMagick-1.1.10/www/api/*.html


#--------------------------------------------------------------

%prep

%setup -q -n %{Name}-%{version}

%build

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
    --with-pic \
%if %{enable_graphwiz}
    --with-dot \
%else
    --without-dot \
%endif
%if %{enable_jasper}
    --with-jp2 \
%else
    --without-jp2 \
%endif
    --with-perl-options="INSTALLDIRS=vendor" 

%make
%install
rm -rf %{buildroot}

%makeinstall_std


%clean
rm -rf %{buildroot}
