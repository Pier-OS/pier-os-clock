# Build Instructions

## Building PyPI Package

### 1. Install Required Tools

```bash
pip install build twine
```

### 2. Build the Package

```bash
python3 -m build
```

This command creates `.whl` and `.tar.gz` files in the `dist/` directory.

### 3. Upload to PyPI

```bash
twine upload dist/*
```

Note: To test before uploading to PyPI:

```bash
twine upload --repository testpypi dist/*
```

## Building Debian Package

### 1. Make Script Executable

```bash
chmod +x BUILD_DEB.sh
```

### 2. Build the Package

```bash
./BUILD_DEB.sh
```

This command creates the `pier-os-clock_1.0.0.deb` file.

### 3. Test the Package

```bash
sudo dpkg -i pier-os-clock_1.0.0.deb
```

### 4. Run

```bash
pier-os-clock
```

## Manual Debian Package Building

If you prefer not to use the script:

```bash
# Create directories
mkdir -p pier-os-clock_1.0.0/DEBIAN
mkdir -p pier-os-clock_1.0.0/usr/bin

# Copy program
cp pier_os_clock.py pier-os-clock_1.0.0/usr/bin/pier-os-clock
chmod +x pier-os-clock_1.0.0/usr/bin/pier-os-clock

# Create DEBIAN/control file
cat > pier-os-clock_1.0.0/DEBIAN/control << EOF
Package: pier-os-clock
Version: 1.0.0
Section: utils
Priority: optional
Architecture: all
Depends: python3
Maintainer: Dogukan Sahil <dogukansahil@protonmail.com>
Description: Minimal TTY clock tool
 A simple terminal clock that displays a centered HH:MM:SS.
EOF

# Build package
dpkg-deb --build pier-os-clock_1.0.0
```
