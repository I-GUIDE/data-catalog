# Shapefile

This document outlines the *required* and *recommended* properties for describing an ESRI
Shapefile. A Shapefile is a geospatial vector file format that is developed and
regulated by ESRI. It consists of several mandatory files (`.shp`, `.shx`,
`.dbf`) as well as numerous optional files (`.prj`, `.sbn`, `.sbx`, `.fbn`,
`.fbx`,`.ain` `.aih`, `.ixs`, `.mxs`, `.atx`, `.shp.xml`, `.cpg`, `.qix`).

While all Schema.org properties are valid, below is a suggested subset to
represent a single Shapefile object using the
*[Dataset](https://schema.org/Dataset)* class.

**Note**: A valid Shapefile entry must include the required metadata outlined
in the [Core Metadata](core.md) document, which are not
described on this page.

#### Required Properties
|Property|Class|Type|Cardinality|Description|
|---|---|---|---|---|
|spatialCoverage | CreativeWork | Place | 1 | The spatial extent of the Shapefile as a bounding box. |
|associatedMedia | CreativeWork	| MediaObject | 3+ | One media object for each of the files that comprise the Shapefile. At minimum this includes `.shp`, `.shx`, and `.dbf`.|


The following is an example implementation of the required metadata
properties.

```
{
 ...
 
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-101.05799349299997,34.99981308000001 -88.02901011799993,34.99981308000001 -88.02901011799993,25.837074428000108 -101.05799349299997,25.837074428000108 -101.05799349299997,34.99981308000001"
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
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "7.6 MB"
   },
    {
      "@type": "MediaObject",
      "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shx",
      "encodingFormat": "x-gis/x-shapefile",
      "contentSize": "412.0 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.dbf",
     "encodingFormat": "application/octet-stream",
     "contentSize": "1.8 KB"
   }
  ]
}
```


#### Recommended Properties

|Property|Class|Type|Cardinality|Description|
|---|---|---|---|---|
|distribution|Dataset|DataDownload|0,1|A downloadable form of this dataset, at a specific location, in a specific format.|
|variableMeasured| Dataset | PropertiesValue | 0+ | The variables contained in the Shapefile's attribute table.

The following is an example implementation of the recommended metadata properties.

<pre lang="json">
{
 ...
 
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-101.05799349299997,34.99981308000001 -88.02901011799993,34.99981308000001 -88.02901011799993,25.837074428000108 -101.05799349299997,25.837074428000108 -101.05799349299997,34.99981308000001"
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
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "7.6 MB"
   },
    {
      "@type": "MediaObject",
      "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shx",
      "encodingFormat": "x-gis/x-shapefile",
      "contentSize": "412.0 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.dbf",
     "encodingFormat": "application/octet-stream",
     "contentSize": "1.8 KB"
   },
   <strong>
    {
      "@type": "MediaObject",
      "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp.xml",
      "encodingFormat": "application/fgdc+xml",
      "contentSize": "88.0 KB"
    },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.sbx",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "164 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.sbn",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "532 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.prj",
     "encodingFormat": "application/text",
     "contentSize": "167.0 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.cpg",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "5.0 B"
   }
  ],
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://www.hydroshare.org/hsapi/resource/9d413b9d57824a79b8239a5f7c4fdf51/",
    "encodingFormat": "application/zip",
    "contentSize": "7.7 MB"
  },
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "propertyID": "HUC_6",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "Shape_Leng",
      "value": "Real"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "Shape_Area",
      "value": "Real"
    }
  ]
  </strong>
}
</pre>

#### Complete Example


```

{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "IGUIDE Shapefile Testing Resource",
  "description": "This resource contains medium-resolution (1:100k) National Hydrography Dataset (NHDPlus) [1] map data for a region of 39 Hydrologic Unit Code (HUC) 6-digit (HUC6) basins around the Hurricane Harvey impact zone across Texas, Louisiana, Mississippi and Arkansas. This includes 5978 subwatersheds, 190,192 catchments, and 192,267 flowlines. USGS active stream gages (924) were downloaded from the USGS National Water Information System (NWIS) [2] and augmented with each gage's HUC2, HUC4, HUC6, HUC8, HUC10 & HUC12 basin identifiers, and COMID of the NHD stream reach for the containing catchment. This allows the user to easily aggregate gages by various watershed boundaries. NOAA Advanced Hydrologic Prediction System (AHPS) [3] has 362 river forecast points in the Harvey study area. Many of these are co-located with USGS NWIS gages to leverage authoritative observation data. A shapefile of Texas dams (7290) was directly received from the Texas Commission for Environmental Quality (TCEQ) [4]. They suggest if you have any questions about data, to make an Open Records Request [5].",
  "url": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/",
  "dateCreated": "2022-01-01T00:00:00+00:00",
  "author": {
    "@list":[
      {
        "@type": "Organization",
        "name": "U.S. Geological Survey (USGS)"
      },
      {
        "@type": "Organization",
        "name": "NOAA National Weather Service"
      },
      {
        "@type": "Organization",
        "name": "Texas Commission for Environmental Quality (TCEQ)"
      },
      {
        "@type": "Person",
        "name": "David Arctur",
        "email": "david.arctur@utexas.edu",
        "identifier": {
          "@id": "https://orcid.org/0000-0002-4708-6302",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0002-4708-6302",
          "value": "0000-0002-4708-6302"
        }
      }
    ]
  },
  "creativeWorkStatus": "published",
  "dateModified": "2022-08-16T17:35:21+00:00",
  "keywords": ["Hurricane", "Flood", "Texas"]
  "funding": [
  {
    "@type": "MonetaryGrant",
    "name": "RAPID: Archiving and Enabling Community Access to Data from Recent US Hurricanes",
     "url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1761673",
     "funder": {
        "@type": "Organization",
        "name": "National Science Foundation"
      }
    }
  ],
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://www.hydroshare.org/hsapi/resource/9d413b9d57824a79b8239a5f7c4fdf51/",
    "encodingFormat": "application/zip",
    "contentSize": "7.7 MB"
  },
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-101.05799349299997,34.99981308000001 -88.02901011799993,34.99981308000001 -88.02901011799993,25.837074428000108 -101.05799349299997,25.837074428000108 -101.05799349299997,34.99981308000001"
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
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "7.6 MB"
   },
    {
      "@type": "MediaObject",
      "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shx",
      "encodingFormat": "x-gis/x-shapefile",
      "contentSize": "412.0 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.dbf",
     "encodingFormat": "application/octet-stream",
     "contentSize": "1.8 KB"
   },
    {
      "@type": "MediaObject",
      "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp.xml",
      "encodingFormat": "application/fgdc+xml",
      "contentSize": "88.0 KB"
    },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.sbx",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "164 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.sbn",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "532 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.prj",
     "encodingFormat": "application/text",
     "contentSize": "167.0 B"
   },
   {
     "@type": "MediaObject",
     "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.cpg",
     "encodingFormat": "x-gis/x-shapefile",
     "contentSize": "5.0 B"
   }
  ],
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://www.hydroshare.org/hsapi/resource/9d413b9d57824a79b8239a5f7c4fdf51/",
    "encodingFormat": "application/zip",
    "contentSize": "7.7 MB"
  },
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "propertyID": "HUC_6",
      "value": "String"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "Shape_Leng",
      "value": "Real"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "Shape_Area",
      "value": "Real"
    }
  ]
}
```

