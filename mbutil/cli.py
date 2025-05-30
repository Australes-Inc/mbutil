#!/usr/bin/env python
"""
MBUtil: a tool for MBTiles files
Supports importing, exporting, and more

(c) Development Seed 2012
(c) 2016 ePi Rational, Inc.
(c) 2025 Australes Inc

Licensed under BSD 3-Clause License
"""

import logging
import os
import sys
from argparse import ArgumentParser

from mbutil import mbtiles_to_disk, disk_to_mbtiles, mbtiles_metadata_to_disk


def create_parser():
    """Create the argument parser."""
    parser = ArgumentParser(
        description='MBUtil: Import and export MBTiles files',
        epilog="""
Examples:

  Export an mbtiles file to a directory of files:
    mb-util world.mbtiles tiles/

  Export metadata only:
    mb-util world.mbtiles dumps

  Import a directory of tiles into an mbtiles file:
    mb-util tiles/ world.mbtiles
        """
    )
    
    parser.add_argument('input', help='Input file or directory')
    parser.add_argument('output', help='Output file or directory')
    
    parser.add_argument(
        '--scheme',
        choices=['wms', 'tms', 'xyz', 'zyx', 'gwc', 'ags'],
        default='xyz',
        help='Tiling scheme of the tiles. Default is "xyz" (z/x/y), '
             'other options are "tms" which is also z/x/y but uses a flipped y coordinate, '
             'and "wms" which replicates the MapServer WMS TileCache directory structure '
             '"z/000/000/x/000/000/y.png", and "zyx" which is the format vips dzsave --layout google uses.'
    )
    
    parser.add_argument(
        '--image_format', '--format',
        dest='format',
        choices=['png', 'jpg', 'pbf', 'webp'],
        default='png',
        help='The format of the image tiles, either png, jpg, webp or pbf'
    )
    
    parser.add_argument(
        '--grid_callback',
        dest='callback',
        default='grid',
        help='Option to control JSONP callback for UTFGrid tiles. '
             'If grids are not used as JSONP, you can remove callbacks specifying --grid_callback=""'
    )
    
    parser.add_argument(
        '--do_compression',
        dest='compression',
        action='store_true',
        default=False,
        help='Do mbtiles compression'
    )
    
    parser.add_argument(
        '--silent',
        action='store_true',
        default=False,
        help='Dictate whether the operations should run silently'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    return parser


def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Configure logging
    if args.verbose and not args.silent:
        logging.basicConfig(level=logging.DEBUG)
    elif not args.silent:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.ERROR)
    
    input_path = args.input
    output_path = args.output
    
    # Convert args to dict for compatibility
    options = {
        'scheme': args.scheme,
        'format': args.format,
        'callback': args.callback,
        'compression': args.compression,
        'silent': args.silent
    }
    
    try:
        # Check if we're doing metadata dump
        if os.path.isfile(input_path) and output_path == "dumps":
            mbtiles_metadata_to_disk(input_path, **options)
            return
        
        # Export mbtiles to disk
        if os.path.isfile(input_path) and not os.path.exists(output_path):
            mbtiles_to_disk(input_path, output_path, **options)
            return
        
        # Import directory to mbtiles
        if os.path.isdir(input_path) and not os.path.isfile(input_path):
            if os.path.isfile(output_path):
                print("Error: Importing tiles into already-existing MBTiles is not yet supported", file=sys.stderr)
                sys.exit(1)
            disk_to_mbtiles(input_path, output_path, **options)
            return
        
        # Invalid combination
        if os.path.isfile(input_path) and os.path.exists(output_path):
            print("Error: To export MBTiles to disk, specify a directory that does not yet exist", file=sys.stderr)
            sys.exit(1)
        
        print("Error: Invalid input/output combination", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
        
    except Exception as e:
        if not args.silent:
            print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()