# GeoPackage

The following is an example of how the I-GUIDE metadata schema can be used to represent a  GeoPackage. A [GeoPackage](https://www.geopackage.org/) is an open, standards-based, format for describing geographic information using SQLite. 


``` json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Geoconnex Reference Features",
  "identifier": "<internal catalog identifier>",
  "dateCreated": "2022-07-14",
  "dateModified": "2023-02-09",
  "keywords": ["Geoconnex", "geopackage", "states"],
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "url": "https://www.hydroshare.org/resource/3295a17b4cc24d34bd6a5c5aaf753c50/",
  "creativeWorkStatus": "public",
  "provider": {
    "@type": "Organization",
    "name": "HydroShare",
    "url": "https://hydroshare.org",
    "parentOrganization": {
      "@type": "Organization",
      "name": "CUAHSI",
      "url": "https://www.cuahsi.org/",
      "address": "1167 Massachusetts Ave Suites 418 & 419, Arlington, MA 02476"
    }
  },
  "creator": {
    "@type": "Organization",
    "name": "Internet of Water Initiative, Center for Geospatial Solutions",
    "email": "cgsinternetofwater@gmail.com",
    "url": "https://internetofwater.org/"
  },
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
    "contentUrl": "https://www.hydroshare.org/resource/3295a17b4cc24d34bd6a5c5aaf753c50/data/contents/states.gpkg",
    "encodingFormat": "application/geopackage+sqlite3",
    "contentSize": "4.7 MB"
  }
}
```

