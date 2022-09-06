# GeoPackage

This document outlines the *required* and *recommended*  properties for describing GeoPackage.
A [GeoPackage](https://www.geopackage.org/) is an open, standards-based, format for describing geographic
information using SQLite. 

While all Schema.org properties are valid, below is a suggested subset for
describing a single GeoPackage using using the
*[Dataset](https://schema.org/Dataset)* class.

**Note**: A valid GeoPackage object must include the required metadata
outlined in the [Core Metadata](core.md) document, which
are not described on this page.

#### Required Properties

|Property|Class|Type|Cardinality|Description|
|---|---|---|---|---|
|spatialCoverage | CreativeWork | Place | 1 | The spatial extent of the GeoPackage as a bounding box. |
|associatedMedia | CreativeWork	| MediaObject | 1 | One media object for the GeoPackage.|

``` json
{
 ...
 
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-176.69,19.06 -66.99,19.06 -66.99,71.34 -176.69,71.34 -176.69,19.06"
    },
    "additionalProperty": {
      "@type": "PropertyValue",
      "propertyID":"http://dbpedia.org/resource/Spatial_reference_system",
      "value": "http://www.w3.org/2003/01/geo/wgs84_pos#lat_long"
    }
  },
  "associatedMedia": [ 
    {
      "@type": "MediaObject",
      "contentSize": "382255104",
      "contentUrl": "https://www.hydroshare.org/resource/3295a17b4cc24d34bd6a5c5aaf753c50/data/contents/states.gpkg",
      "encodingFormat": "application/geopackage+sqlite3",
      "sha256": "c04ed02d82a461e98f27b59cb744fa1aa6ebe8e2301d1856c840c046adbc95ef"
    }
  ]
}
```

#### Recommended Properties

|Property|Class|Type|Cardinality|Description|
|---|---|---|---|---|
|distribution|Dataset|DataDownload|0,1|A downloadable form of this dataset, at a specific location, in a specific format.|
|variableMeasured| Dataset | PropertiesValue | 0+ | The variables contained in the GeoPackage.

<pre lang="json">
{
 ...
 
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-176.69,19.06 -66.99,19.06 -66.99,71.34 -176.69,71.34 -176.69,19.06"
    },
    "additionalProperty": {
      "@type": "PropertyValue",
      "propertyID":"http://dbpedia.org/resource/Spatial_reference_system",
      "value": "http://www.w3.org/2003/01/geo/wgs84_pos#lat_long"
    }
  },
  "associatedMedia": [ 
    {
      "@type": "MediaObject",
      "contentSize": "382255104",
      "contentUrl": "https://www.hydroshare.org/resource/3295a17b4cc24d34bd6a5c5aaf753c50/data/contents/states.gpkg",
      "encodingFormat": "application/geopackage+sqlite3",
      "sha256": "c04ed02d82a461e98f27b59cb744fa1aa6ebe8e2301d1856c840c046adbc95ef"
    }
  ],
  <strong>
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "propertyID": "fid",
      "value": "Int64"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "uri",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "STATEFP",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "STATENS",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "AFFGEOID",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "GEOID",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "STUSPS",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "NAME",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "LSAD",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "census_profile",
      "value": "String"
    }
  ],
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://www.hydroshare.org/hsapi/resource/3295a17b4cc24d34bd6a5c5aaf753c50/",
    "encodingFormat": "application/zip",
    "contentSize": "4.9 MB"
  }
  </strong>
}
</pre>

