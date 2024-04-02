# Maintainer: Matthew Phillip Cooper <coopertronics@gmail.com>

pkgname=welcome
pkgver=1
pkgrel=1
pkgdesc="This is the Coopertronic OS Welcome screen. It givs a breif overview of what Coopertronic OS is all about."
arch=('any')
url="https://coopertronic-ws.ddns.net/ctos-assets/"
license=('LGPL3')
depends=('python' 'pyside6' 'about')
source=("$url$pkgname/$pkgname-v$pkgver.zip")
md5sums=('04efc012488e4f483931ed5a8325594e')

package() {
  ##  Install documentation
  #install -D -m644 $srcdir/README $pkgdir/usr/share/doc/$pkgname/README

  ##  Install licenses
  install -d $pkgdir/usr/share/licenses/$pkgname
  install -m644 $srcdir/LICENSE $pkgdir/usr/share/licenses/$pkgname/

  ##  Install binaries
  install -d $pkgdir/usr/share/$pkgname
  install -D -m644 $srcdir/scripts/* $pkgdir/usr/share/$pkgname/
  install -d $pkgdir/usr/share/$pkgname/assets
  install -D -m755 $srcdir/assets/$pkgname.sh $pkgdir/usr/bin/$pkgname
  install -D -m755 $srcdir/assets/$pkgname.svg $pkgdir/usr/share/$pkgname/assets/

  ##  Install game icon
  #install -d $pkgdir/usr/share/icons/hicolor/scalable/apps
  #install -D -m644 org.$pkgname.$pkgname.svg $pkgdir/usr/share/icons/hicolor/scalable/apps/org.$pkgname.$pkgname.svg

  ##  Install Application desktop launcher
  install -d $pkgdir/usr/share/applications
  install -D -m644 $srcdir/assets/org.$pkgname.$pkgname.desktop $pkgdir/usr/share/applications/org.$pkgname.$pkgname.desktop
}
