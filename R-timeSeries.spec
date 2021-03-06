#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-timeSeries
Version  : 3062.100
Release  : 29
URL      : https://cran.r-project.org/src/contrib/timeSeries_3062.100.tar.gz
Source0  : https://cran.r-project.org/src/contrib/timeSeries_3062.100.tar.gz
Summary  : Financial Time Series Objects (Rmetrics)
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-timeDate
BuildRequires : R-timeDate
BuildRequires : R-xts
BuildRequires : buildreq-R

%description
Basic functions such as scaling and sorting, subsetting,
  mathematical operations and statistical functions.

%prep
%setup -q -c -n timeSeries
cd %{_builddir}/timeSeries

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616003009

%install
export SOURCE_DATE_EPOCH=1616003009
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library timeSeries
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library timeSeries
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library timeSeries
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc timeSeries || :


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
/usr/lib64/R/library/timeSeries/R/timeSeries
/usr/lib64/R/library/timeSeries/R/timeSeries.rdb
/usr/lib64/R/library/timeSeries/R/timeSeries.rdx
/usr/lib64/R/library/timeSeries/README
/usr/lib64/R/library/timeSeries/THANKS
/usr/lib64/R/library/timeSeries/data/Rdata.rdb
/usr/lib64/R/library/timeSeries/data/Rdata.rds
/usr/lib64/R/library/timeSeries/data/Rdata.rdx
/usr/lib64/R/library/timeSeries/doc/index.html
/usr/lib64/R/library/timeSeries/doc/timeSeriesPlot.R
/usr/lib64/R/library/timeSeries/doc/timeSeriesPlot.Rnw
/usr/lib64/R/library/timeSeries/doc/timeSeriesPlot.pdf
/usr/lib64/R/library/timeSeries/doc/timeSeriesRefCard.pdf
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
