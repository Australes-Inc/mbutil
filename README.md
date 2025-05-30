# mbutil

> A modernized fork of mbutil tool create by (c) Mapbox. 

mbutil is a utility for importing and exporting the [MBTiles](http://mbtiles.org/) format, typically created with [Mapbox](http://mapbox.com/) [TileMill](http://mapbox.com/tilemill/).

This is an enhanced fork of the original [mapbox/mbutil](https://github.com/mapbox/mbutil) project, updated for modern Python environments and packaging standards.

Before exporting tiles to disk, consider if there's a [Mapbox Hosting plan](http://mapbox.com/plans/) or an open source [MBTiles server implementation](https://github.com/mapbox/mbtiles-spec/wiki/Implementations) that works for you - tiles on disk are notoriously difficult to manage.

## What's New 

This enhanced version addresses the limitations of the original project and includes:

- ✅ **Modern Python packaging** - Works with `pip`
- ✅ **Improved CLI** - Better command-line interface using `argparse`
- ✅ **Python 2.7+ and 3.6+ compatibility** - Full support for modern Python versions
- ✅ **Proper entry points** - No more path or installation issues
- ✅ **Enhanced error handling** - Better debugging and user experience
- ✅ **Active maintenance** - Regular updates and bug fixes

## Installation

### Quick Install

```bash
pip install git+https://github.com/Australes-Inc/mbutil.git
```

### In a Conda Environment

```bash
# Create a new environment
conda create -n gis python=3.9
conda activate gis

# Install mbutil enhanced
pip install git+https://github.com/Australes-Inc/mbutil.git
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/Australes-Inc/mbutil.git
cd mbutil

# Install in development mode
pip install -e .
```

## Usage

```bash
$ mb-util -h
usage: mb-util [-h] [--scheme {wms,tms,xyz,zyx,gwc,ags}] [--image_format {png,jpg,pbf,webp}]
               [--grid_callback CALLBACK] [--do_compression] [--silent] [--verbose]
               input output

MBUtil: Import and export MBTiles files

positional arguments:
  input                 Input file or directory
  output                Output file or directory

optional arguments:
  -h, --help            show this help message and exit
  --scheme {wms,tms,xyz,zyx,gwc,ags}
                        Tiling scheme of the tiles. Default is "xyz" (z/x/y), other options are "tms" which is also
                        z/x/y but uses a flipped y coordinate, and "wms" which replicates the MapServer WMS TileCache
                        directory structure "z/000/000/x/000/000/y.png", and "zyx" which is the format vips dzsave
                        --layout google uses.
  --image_format {png,jpg,pbf,webp}, --format {png,jpg,pbf,webp}
                        The format of the image tiles, either png, jpg, webp or pbf
  --grid_callback CALLBACK
                        Option to control JSONP callback for UTFGrid tiles. If grids are not used as JSONP, you can
                        remove callbacks specifying --grid_callback=""
  --do_compression      Do mbtiles compression
  --silent              Dictate whether the operations should run silently
  --verbose, -v         Verbose output
```

### Examples

**Export an mbtiles file to a directory of files:**
```bash
mb-util world.mbtiles tiles/
# Note: 'tiles/' directory must not already exist
```

**Import a directory of tiles into an mbtiles file:**
```bash
mb-util tiles/ world.mbtiles
# Note: 'world.mbtiles' file must not already exist
```

**Export with specific options:**
```bash
mb-util --scheme tms --image_format webp terrain.mbtiles output/
```

**Export metadata only:**
```bash
mb-util world.mbtiles dumps
```

## Requirements

- Python >= 2.7 (including Python 3.6+)
- Git (for installation from GitHub)

## Metadata

MBUtil imports and exports metadata as JSON, in the root of the tile directory, as a file named `metadata.json`.

```json
{
    "name": "World Light",
    "description": "A Test Metadata",
    "version": "3"
}
```

## Updates

To update to the latest version:

```bash
pip install --upgrade git+https://github.com/Australes-Inc/mbutil.git
```

## Troubleshooting

### Common Issues

**"git is not recognized"**
- Install Git from [https://git-scm.com/](https://git-scm.com/)

**"mb-util command not found"**
- Ensure you've activated the correct environment
- Try reinstalling: `pip uninstall mbutil && pip install git+https://github.com/Australes-Inc/mbutil.git`

**Permission errors**
- Use virtual environments instead of system-wide installation
- On Unix systems, avoid using `sudo` with pip

## See Also

- [Original mbutil](https://github.com/mapbox/mbutil) - The original project this fork is based on
- [node-mbtiles](https://github.com/mapbox/node-mbtiles) - Node.js implementation with mbpipe utility
- [MBTiles Specification](https://github.com/mapbox/mbtiles-spec) - Technical specification for MBTiles

## License

BSD 3-Clause License - see [LICENSE.md](LICENSE.md) for details.

**Original work:**
- Copyright (c) Development Seed
- Copyright (c) Tom MacWright

**Modified work:**
- Copyright (c) 2025 Australes Inc
- Copyright (c) Diego Posado Bañuls

## Authors and Maintainers

### Original Authors
- **Tom MacWright** ([@tmcw](https://github.com/tmcw))
- **Dane Springmeyer** ([@springmeyer](https://github.com/springmeyer))
- **Mathieu Leplatre** ([@leplatrem](https://github.com/leplatrem))

### Current Maintainer
- **Diego Posado Bañuls** ([@diegoposba](https://github.com/diegoposba))

## Changelog

### v0.3.1 (2025)
- ✅ Modern Python packaging with proper entry points
- ✅ Improved CLI using argparse
- ✅ Enhanced error handling and user experience
- ✅ Python 3.6+ compatibility improvements
- ✅ Better installation

### v0.3.0 (Original)
- ✅ Preliminary Python 3 support
- ✅ MBTiles import/export functionality

---

**Note**: This project enhances and modernizes the original mbutil while maintaining full backward compatibility. The original project is no longer actively maintained, which is why this fork was created to provide ongoing support and improvements.
