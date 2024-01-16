#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : R-timeSeries
Version  : 4032.109
Release  : 50
URL      : https://cran.r-project.org/src/contrib/timeSeries_4032.109.tar.gz
Source0  : https://cran.r-project.org/src/contrib/timeSeries_4032.109.tar.gz
Summary  : Financial Time Series Objects (Rmetrics)
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-timeSeries-license = %{version}-%{release}
Requires: R-timeDate
BuildRequires : R-timeDate
BuildRequires : R-xts
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Basic functions such as scaling and sorting, subsetting,
  mathematical operations and statistical functions.

%package license
Summary: license components for the R-timeSeries package.
Group: Default

%description license
license components for the R-timeSeries package.


%prep
%setup -q -n timeSeries
pushd ..
cp -a timeSeries buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705423361

%install
export SOURCE_DATE_EPOCH=1705423361
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-timeSeries
cp %{_builddir}/timeSeries/inst/COPYING %{buildroot}/usr/share/package-licenses/R-timeSeries/e393cdc6b44acda4c324a5214d468691b0a42119 || :
cp %{_builddir}/timeSeries/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-timeSeries/d68b853a7d0c0fd56da8701d27266ea7f161a542 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/timeSeries/COPYING
/usr/lib64/R/library/timeSeries/COPYRIGHTS
/usr/lib64/R/library/timeSeries/DESCRIPTION
/usr/lib64/R/library/timeSeries/INDEX
/usr/lib64/R/library/timeSeries/Meta/Rd.rds
/usr/lib64/R/library/timeSeries/Meta/data.rds
/usr/lib64/R/library/timeSeries/Meta/features.rds
/usr/lib64/R/library/timeSeries/Meta/hsearch.rds
/usr/lib64/R/library/timeSeries/Meta/links.rds
/usr/lib64/R/library/timeSeries/Meta/nsInfo.rds
/usr/lib64/R/library/timeSeries/Meta/package.rds
/usr/lib64/R/library/timeSeries/Meta/vignette.rds
/usr/lib64/R/library/timeSeries/NAMESPACE
/usr/lib64/R/library/timeSeries/NEWS.md
/usr/lib64/R/library/timeSeries/R/timeSeries
/usr/lib64/R/library/timeSeries/R/timeSeries.rdb
/usr/lib64/R/library/timeSeries/R/timeSeries.rdx
/usr/lib64/R/library/timeSeries/README
/usr/lib64/R/library/timeSeries/THANKS
/usr/lib64/R/library/timeSeries/_pkgdown.yml
/usr/lib64/R/library/timeSeries/data/Rdata.rdb
/usr/lib64/R/library/timeSeries/data/Rdata.rds
/usr/lib64/R/library/timeSeries/data/Rdata.rdx
/usr/lib64/R/library/timeSeries/doc/index.html
/usr/lib64/R/library/timeSeries/doc/timeSeriesPlot.R
/usr/lib64/R/library/timeSeries/doc/timeSeriesPlot.Rnw
/usr/lib64/R/library/timeSeries/doc/timeSeriesPlot.pdf
/usr/lib64/R/library/timeSeries/doc/timeSeriesRefCard.pdf
/usr/lib64/R/library/timeSeries/extdata/msft.csv
/usr/lib64/R/library/timeSeries/extensionsTests/aggregateWrappers.R
/usr/lib64/R/library/timeSeries/extensionsTests/alignWrappers.R
/usr/lib64/R/library/timeSeries/extensionsTests/attributesExtension.R
/usr/lib64/R/library/timeSeries/extensionsTests/chicPlots.R
/usr/lib64/R/library/timeSeries/extensionsTests/endpointsWrappers.R
/usr/lib64/R/library/timeSeries/extensionsTests/xtsWrappers.R
/usr/lib64/R/library/timeSeries/help/AnIndex
/usr/lib64/R/library/timeSeries/help/aliases.rds
/usr/lib64/R/library/timeSeries/help/paths.rds
/usr/lib64/R/library/timeSeries/help/timeSeries.rdb
/usr/lib64/R/library/timeSeries/help/timeSeries.rdx
/usr/lib64/R/library/timeSeries/html/00Index.html
/usr/lib64/R/library/timeSeries/html/R.css
/usr/lib64/R/library/timeSeries/pkgdown.yml
/usr/lib64/R/library/timeSeries/tests/doRUnit.R
/usr/lib64/R/library/timeSeries/tests/msft.dat.csv
/usr/lib64/R/library/timeSeries/unitTests/Makefile
/usr/lib64/R/library/timeSeries/unitTests/runTests.R
/usr/lib64/R/library/timeSeries/unitTests/runit.NA.R
/usr/lib64/R/library/timeSeries/unitTests/runit.Omit.R
/usr/lib64/R/library/timeSeries/unitTests/runit.TimeSeriesClass.R
/usr/lib64/R/library/timeSeries/unitTests/runit.TimeSeriesCoercion.R
/usr/lib64/R/library/timeSeries/unitTests/runit.TimeSeriesData.R
/usr/lib64/R/library/timeSeries/unitTests/runit.TimeSeriesPositions.R
/usr/lib64/R/library/timeSeries/unitTests/runit.aggregate.R
/usr/lib64/R/library/timeSeries/unitTests/runit.align.R
/usr/lib64/R/library/timeSeries/unitTests/runit.apply.R
/usr/lib64/R/library/timeSeries/unitTests/runit.as.R
/usr/lib64/R/library/timeSeries/unitTests/runit.attach.R
/usr/lib64/R/library/timeSeries/unitTests/runit.bind.R
/usr/lib64/R/library/timeSeries/unitTests/runit.colCum.R
/usr/lib64/R/library/timeSeries/unitTests/runit.colStats.R
/usr/lib64/R/library/timeSeries/unitTests/runit.cor.R
/usr/lib64/R/library/timeSeries/unitTests/runit.cumulated.R
/usr/lib64/R/library/timeSeries/unitTests/runit.daily.R
/usr/lib64/R/library/timeSeries/unitTests/runit.dim.R
/usr/lib64/R/library/timeSeries/unitTests/runit.drawdowns.R
/usr/lib64/R/library/timeSeries/unitTests/runit.durations.R
/usr/lib64/R/library/timeSeries/unitTests/runit.lag.R
/usr/lib64/R/library/timeSeries/unitTests/runit.mathOps.R
/usr/lib64/R/library/timeSeries/unitTests/runit.merge.R
/usr/lib64/R/library/timeSeries/unitTests/runit.methods-plot.R
/usr/lib64/R/library/timeSeries/unitTests/runit.methods-print.R
/usr/lib64/R/library/timeSeries/unitTests/runit.methods-summary.R
/usr/lib64/R/library/timeSeries/unitTests/runit.model.frame.R
/usr/lib64/R/library/timeSeries/unitTests/runit.monthly.R
/usr/lib64/R/library/timeSeries/unitTests/runit.na.contiguous.R
/usr/lib64/R/library/timeSeries/unitTests/runit.order.R
/usr/lib64/R/library/timeSeries/unitTests/runit.periodical.R
/usr/lib64/R/library/timeSeries/unitTests/runit.rank.R
/usr/lib64/R/library/timeSeries/unitTests/runit.returns.R
/usr/lib64/R/library/timeSeries/unitTests/runit.rowCum.R
/usr/lib64/R/library/timeSeries/unitTests/runit.signalCounts.R
/usr/lib64/R/library/timeSeries/unitTests/runit.spreads.R
/usr/lib64/R/library/timeSeries/unitTests/runit.subset.R
/usr/lib64/R/library/timeSeries/unitTests/runit.time.R
/usr/lib64/R/library/timeSeries/unitTests/runit.timeSeries.R

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-timeSeries/d68b853a7d0c0fd56da8701d27266ea7f161a542
/usr/share/package-licenses/R-timeSeries/e393cdc6b44acda4c324a5214d468691b0a42119
