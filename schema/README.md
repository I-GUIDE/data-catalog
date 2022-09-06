# I-GUIDE Catalog Schema Definition

The I-GUIDE catalog must be capable of storing metadata about diverse resource
types, including the examples listed below. These examples are expressed as
`json+ld` as a standardized and readable way to capture metadata, leveraging
Schema.org classes and properties whenever possible.

All cataloged items must be described using a standard, core set of metadata
derived from the Schema.org *Thing* and *CreativeWork* classes. Metadata for
cataloged items may then be customized to include additional properties
specific to the type of resource being described.

The following are references to required and recommended Schema.org properties
for common data formats.

- [Generic/Core Properties](core.md)
- Geospatial 
  - [Shapefile](shapefile.md)
  - [Geopackage](geopackage.md)
  - [GeoTiff](geotiff.md)
- Software
  - [Source Code](sourcecode.md)
  - [Software Application](softwareapp.md)


