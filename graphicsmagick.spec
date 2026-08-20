%define Werror_cflags %nil

%define _disable_lto 1
%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1
# ImageMagick actually uses libtool to load its modules
%define dont_remove_libtool_files 1

%define build_modules 1
%define enable_jasper 1
%define enable_graphwiz 1

%define oname GraphicsMagick
%define major 3
%define ppmajor 12
%define wand_major 2
%define libname %mklibname %{name} %{major}
%define libnamepp %mklibname %{name}++ %{ppmajor}
%define libwandname %mklibname graphicsmagickwand %{wand_major}
%define devname %mklibname %{name} -d
%define qlev Q8

%define _disable_rebuild_configure 1

%global __provides_exclude_from ^%{_libdir}/GraphicsMagick-%{version}/.*\\.(la|so)$
%global optflags %{optflags} -O3

Summary:	An X application for displaying and manipulating images
Name:		graphicsmagick
Version:	1.3.48
Release:	3
License:	GPLv2+
Group:		Graphics
Url:		https://www.graphicsmagick.org/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{oname}-%{version}.tar.xz
Patch0:		GraphicsMagick-1.3.14-linkage.patch
Patch1:		graphicsmagick-1.3.40-clang.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	ghostscript-devel
BuildRequires:	jbigkit-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	libtool-devel
BuildRequires:	libwmf-devel
BuildRequires:	perl-devel
BuildRequires:	xdg-utils
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libxml-2.0)

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
%dir %{_libdir}/GraphicsMagick-%{version}
%dir %{_libdir}/GraphicsMagick-%{version}/config
%{_libdir}/GraphicsMagick-%{version}/config/*.mgk
%dir %{_datadir}/GraphicsMagick-%{version}
%dir %{_datadir}/GraphicsMagick-%{version}/config
%{_datadir}/GraphicsMagick-%{version}/config/*.mgk
%if %{build_modules}
%dir %{_libdir}/%{oname}-%{version}/modules-%{qlev}
%{_libdir}/%{oname}-%{version}/modules-%{qlev}/filters
%dir %{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders
%{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders/*.la
%{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders/*.so
%endif
%doc %{_mandir}/man1/GraphicsMagick++-config.1.*
%doc %{_mandir}/man1/GraphicsMagick-config.1.*
%doc %{_mandir}/man1/GraphicsMagickWand-config.1.*
%doc %{_mandir}/man1/gm.1.*
%doc %{_mandir}/man4/miff.4.*
%doc %{_mandir}/man5/quantize.5.*

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
%{_libdir}/libGraphicsMagick++.so.%{ppmajor}*

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
%doc %{_mandir}/man3*/*::*.3pm*
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
%autosetup -n %{oname}-%{version} -p1

%build
# Keep ${CFLAGS} so a %%pgo pass can inject -fprofile-generate/use
export CFLAGS="${CFLAGS:-%{optflags}}"
export CXXFLAGS="${CXXFLAGS:-%{optflags}}"

%configure \
	--with-lcms2 \
	--enable-openmp \
	--enable-fast-install \
	--without-dps \
%if %{build_modules}
	--with-modules \
%else
	--without-modules \
%endif
	--enable-shared \
	--disable-static \
	--with-threads \
	--with-pic \
%if %{enable_jasper}
	--with-jp2 \
%else
	--without-jp2 \
%endif
	--with-perl-options="INSTALLDIRS=vendor"  \
	--with-perl

# GNU libtool's export-symbols-regex path becomes "nm | | sed" when
# CFLAGS contain -fprofile-generate (empty global_symbol_pipe).
# Makefile uses $(SHELL) ./libtool, so override LIBTOOL rather than
# replacing the script with the slibtool binary.
%make_build LIBTOOL=slibtool
%make_build perl-build LIBTOOL=slibtool

# Train the instrumented gm on typical convert/identify/montage paths.
# Optional formats are skipped if the coder is missing. No X11.
# slibtool writes coder .so files to .libs/ but the .la dlname is just
# "foo.so", so lt_dlopen looks next to the .la (not in .libs/).
%pgo
set +e
export LLVM_PROFILE_FILE="%{_pgo_profile_dir}/graphicsmagick-%%m-%%p.profraw"

TOP="$PWD"
GM="$TOP/utilities/.libs/gm"
if [ ! -x "$GM" ]; then
	GM="$TOP/utilities/gm"
fi
if [ ! -x "$GM" ]; then
	echo "PGO: instrumented gm binary missing"
	exit 1
fi
for d in "$TOP/coders" "$TOP/filters"; do
	if [ -d "$d/.libs" ]; then
		( cd "$d" && for so in .libs/*.so; do
			[ -e "$so" ] || continue
			ln -sfn "$so" "$(basename "$so")"
		done )
	fi
done
export LD_LIBRARY_PATH="$TOP/magick/.libs:$TOP/wand/.libs:$TOP/Magick++/lib/.libs${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export MAGICK_CODER_MODULE_PATH="$TOP/coders"
export MAGICK_FILTER_MODULE_PATH="$TOP/filters"
export MAGICK_CONFIGURE_PATH="$TOP/config"

im() {
	"$GM" convert "$@"
}
try() {
	im "$@"
	rc=$?
	if [ $rc -ne 0 ]; then
		echo "PGO: skipped (exit $rc): gm convert $*"
	fi
	return 0
}

WORKDIR="$PWD/pgo-train"
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"
cd "$WORKDIR"

im logo: logo.png || exit 1
im rose: rose.png || exit 1
try wizard: wizard.png
try granite: granite.png
try netscape: netscape.gif
try -size 1280x720 plasma:fractal photo.png
if [ ! -f photo.png ]; then
	im logo: -resize 1280x720 photo.png || exit 1
fi
try -size 640x360 gradient:black-white gradient.png
try -size 320x240 xc:'#224466' solid.png
try -size 400x80 -background white -fill black -font Helvetica -pointsize 28 \
	caption:'GraphicsMagick PGO' caption.png

for fmt in jpg png gif tiff bmp ppm miff; do
	try photo.png -quality 85 "enc.$fmt"
	try "enc.$fmt" "round.png"
done
try rose.png enc.ico
try enc.ico ico-round.png
try photo.png -quality 82 -sampling-factor 4:2:0 jpeg420.jpg
try photo.png -interlace Line -quality 80 jpegprog.jpg
try photo.png -colorspace GRAY jpeggray.jpg
try rose: -resize 400x PNG32:alpha.png
try -delay 8 -loop 0 logo: -resize 120x \
	\( +clone -roll +8+0 \) \( +clone -roll +0+8 \) anim.gif
try anim.gif -coalesce -resize 80x anim-opt.gif

try photo.png out.jp2
try photo.png pdf:out.pdf
try 'out.pdf[0]' pdfpage.png
if [ -f ../utilities/tests/sunrise.jpg ]; then
	try ../utilities/tests/sunrise.jpg sunrise.png
fi

try photo.png -auto-orient -resize '1024x1024>' -strip -quality 82 web.jpg
try photo.png -thumbnail 150x150 -gravity center -extent 150x150 thumb.jpg
try photo.png -crop 640x360+80+40 +repage crop.png
try photo.png -rotate 90 rot.png
try photo.png -flip -flop flip.png
try photo.png -resize 50% -unsharp 0x0.75+0.75+0.008 unsharp.jpg
try photo.png -gaussian-blur 0x1.2 blur.png
try photo.png -sharpen 0x1.0 sharp.png
try photo.png -modulate 105,110,100 mod.png
try photo.png -normalize norm.png
try photo.png -colorspace RGB srgb.png
try photo.png -colorspace GRAY gray.png
try photo.png -gamma 1.1 gamma.png
try photo.png -posterize 16 post.png
try photo.png -colors 64 +dither pal.png
try photo.png -trim +repage trim.png
try photo.png -bordercolor white -border 8 border.png
try photo.png -resize 800x -quality 70 -strip web-sm.jpg

try photo.png -gravity southeast -pointsize 22 -fill white \
	-draw "text 16,16 'PGO watermark'" annotated.jpg
try photo.png caption.png -gravity south -geometry +0+10 -compose over -composite marked.png
try -size 200x200 xc:none -fill '#cc3333' -draw 'circle 100,100 100,20' ball.png
try photo.png ball.png -gravity northeast -geometry +20+20 -compose over -composite badged.png

"$GM" identify -verbose photo.png
"$GM" identify jpeg420.jpg enc.png
"$GM" compare -metric rmse photo.png web.jpg diff.png
"$GM" montage logo.png rose.png -geometry 120x120+4+4 -tile 2x1 sheet.png
"$GM" mogrify -resize 320x -quality 80 jpeg420.jpg

cd "$TOP"
make %{?_smp_mflags} LIBTOOL=slibtool tests/drawtest \
	Magick++/tests/appendImages Magick++/tests/readWriteImages \
	Magick++/tests/attributes Magick++/tests/color \
	Magick++/tests/montageImages Magick++/tests/morphImages \
	Magick++/tests/averageImages Magick++/tests/coalesceImages
[ -x tests/drawtest ] && tests/drawtest
export SRCDIR="$TOP/Magick++/tests/"
for t in appendImages readWriteImages attributes color montageImages \
	morphImages averageImages coalesceImages; do
	if [ -x Magick++/tests/$t ]; then
		Magick++/tests/$t
	fi
done
# In-tree PerlMagick (php-imagick analogue for GM)
if [ -d PerlMagick/blib ]; then
	perl -IPerlMagick/blib/lib -IPerlMagick/blib/arch -e '
		use Graphics::Magick;
		my $i = Graphics::Magick->new;
		$i->Read("logo:");
		$i->Resize(geometry => "50%x50%");
		$i->Write("pgo-train/perl.png");
	'
fi

rm -rf "$WORKDIR"
exit 0

%install
%make_install LIBTOOL=slibtool
%make_install -C PerlMagick LIBTOOL=slibtool
rm -f %{buildroot}%{_datadir}/GraphicsMagick-%{version}/{ChangeLog,NEWS.txt}
# We only need *.la crap for modules
rm -f %{buildroot}%{_libdir}/*.la
# slibtool still installs convenience .a files despite --disable-static
rm -f %{buildroot}%{_libdir}/*.a
# slibtool --mode=install copies the .so but not the .la; GM loads
# modules via lt_dlopen of the .la sitting next to the .so.
install -m 644 -p coders/*.la %{buildroot}%{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders/
install -m 644 -p filters/*.la %{buildroot}%{_libdir}/%{oname}-%{version}/modules-%{qlev}/filters/
sed -i 's/^installed=no$/installed=yes/' \
	%{buildroot}%{_libdir}/%{oname}-%{version}/modules-%{qlev}/coders/*.la \
	%{buildroot}%{_libdir}/%{oname}-%{version}/modules-%{qlev}/filters/*.la
