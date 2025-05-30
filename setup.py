import os
from setuptools import setup, find_packages

# Lire le README
def read_file(filename):
    """Read file contents."""
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, filename), 'r', encoding='utf-8') as f:
        return f.read()

# Lire la version depuis __init__.py si elle existe
def get_version():
    """Get version from package."""
    try:
        with open('mbutil/__init__.py', 'r') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return '0.3.0'

setup(
    name='mbutil',
    version=get_version(),
    author='Tom MacWright',
    author_email='tom@macwright.org',
    maintainer='Diego Posado Bañuls (Australes Inc)',
    maintainer_email='diegoposba@gmail.com',
    description='An importer and exporter for MBTiles (Enhanced by Australes Inc)',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Australes-Inc/mbutil',
    
    packages=find_packages(),
    include_package_data=True,
    
    entry_points={
        'console_scripts': [
            'mb-util=mbutil.cli:main',
        ],
    },
    
    install_requires=[
    ],
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    
    python_requires='>=2.7',
    license='BSD',
    keywords='mbtiles tiles mapping gis',
    
    scripts=['mb-util'] if os.path.exists('mb-util') else [],
)