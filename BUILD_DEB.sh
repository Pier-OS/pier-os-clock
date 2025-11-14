#!/bin/bash
# Debian package build script

VERSION="1.0.0"
PACKAGE_NAME="pier-os-clock"
PACKAGE_DIR="${PACKAGE_NAME}_${VERSION}"

# Create directories
mkdir -p "${PACKAGE_DIR}/DEBIAN"
mkdir -p "${PACKAGE_DIR}/usr/bin"

# Copy program
cp pier_os_clock.py "${PACKAGE_DIR}/usr/bin/pier-os-clock"
chmod +x "${PACKAGE_DIR}/usr/bin/pier-os-clock"

# Add shebang if missing
if ! head -n1 "${PACKAGE_DIR}/usr/bin/pier-os-clock" | grep -q "^#!/"; then
    sed -i '1i#!/usr/bin/env python3' "${PACKAGE_DIR}/usr/bin/pier-os-clock"
fi

# Create DEBIAN/control file
cat > "${PACKAGE_DIR}/DEBIAN/control" << EOF
Package: ${PACKAGE_NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: all
Depends: python3
Maintainer: Dogukan Sahil <dogukansahil@protonmail.com>
Description: Minimal TTY clock tool
 A simple terminal clock that displays a centered HH:MM:SS.
EOF

# Build package
dpkg-deb --build "${PACKAGE_DIR}"

echo "Package created: ${PACKAGE_DIR}.deb"
