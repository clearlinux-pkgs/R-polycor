#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-polycor
Version  : 0.7.9
Release  : 10
URL      : https://cran.r-project.org/src/contrib/polycor_0.7-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/polycor_0.7-9.tar.gz
Summary  : Polychoric and Polyserial Correlations
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mvtnorm
BuildRequires : R-mvtnorm
BuildRequires : clr-R-helpers

%description
optionally with standard errors; tetrachoric and biserial correlations are special cases.

%prep
%setup -q -c -n polycor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521229051

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521229051
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polycor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polycor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polycor
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library polycor|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/polycor/CHANGES
/usr/lib64/R/library/polycor/DESCRIPTION
/usr/lib64/R/library/polycor/INDEX
/usr/lib64/R/library/polycor/Meta/Rd.rds
/usr/lib64/R/library/polycor/Meta/features.rds
/usr/lib64/R/library/polycor/Meta/hsearch.rds
/usr/lib64/R/library/polycor/Meta/links.rds
/usr/lib64/R/library/polycor/Meta/nsInfo.rds
/usr/lib64/R/library/polycor/Meta/package.rds
/usr/lib64/R/library/polycor/NAMESPACE
/usr/lib64/R/library/polycor/R/polycor
/usr/lib64/R/library/polycor/R/polycor.rdb
/usr/lib64/R/library/polycor/R/polycor.rdx
/usr/lib64/R/library/polycor/help/AnIndex
/usr/lib64/R/library/polycor/help/aliases.rds
/usr/lib64/R/library/polycor/help/paths.rds
/usr/lib64/R/library/polycor/help/polycor.rdb
/usr/lib64/R/library/polycor/help/polycor.rdx
/usr/lib64/R/library/polycor/html/00Index.html
/usr/lib64/R/library/polycor/html/R.css
