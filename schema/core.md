# Core Metadata

Core metadata is a set of common metadata fields that all catalog
holdings share and consists largely of high-level dataset attributes
and properties. This document outlines the **required** and **recommended**
high-level properties that are required.

**Required Metadata**

|Property|Schema.org Class|Expected Type|Cardinality|Description| 
|---|---|---|---|---|
|url|Thing|URL|1|the url of the item|
|name|Thing|Text|1|the name or title of the item| 
|description|Thing|Text|1|the description or abstract of the item|
|author|Creative Work|Person OR Organization|1+| person or organization that authored the work|
| dateCreated | CreativeWork | Date \| DateTime | 1 | The date on which the work was created|

The following is an example implementation of the required metadata properties
for a Schema.org Dataset item:

``` json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "IGUIDE Shapefile Testing Resource",
  "description": "This resource contains medium-resolution (1:100k) National Hydrography Dataset (NHDPlus) [1] map data for a region of 39 Hydrologic Unit Code (HUC) 6-digit (HUC6) basins around the Hurricane Harvey impact zone across Texas, Louisiana, Mississippi and Arkansas. This includes 5978 subwatersheds, 190,192 catchments, and 192,267 flowlines. USGS active stream gages (924) were downloaded from the USGS National Water Information System (NWIS) [2] and augmented with each gage's HUC2, HUC4, HUC6, HUC8, HUC10 & HUC12 basin identifiers, and COMID of the NHD stream reach for the containing catchment. This allows the user to easily aggregate gages by various watershed boundaries. NOAA Advanced Hydrologic Prediction System (AHPS) [3] has 362 river forecast points in the Harvey study area. Many of these are co-located with USGS NWIS gages to leverage authoritative observation data. A shapefile of Texas dams (7290) was directly received from the Texas Commission for Environmental Quality (TCEQ) [4]. They suggest if you have any questions about data, to make an Open Records Request [5].",
  "url": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/",
  "dateCreated": "2022-08-16T17:35:21+00:00",
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
  }
}
```



**Recommended Metadata**

|Property|Class|Type|Cardinality|Description| 
|---|---|---|---|---|
|hasPart|CreativeWork|CreativeWork|0+|Indicates an item or CreativeWork that is part of this item|
|isPartOf|CreativeWork|CreativeWork OR URL |0+|Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of.|
|associatedMedia|CreativeWork|MediaObject|0+| A media object that encodes this CreativeWork. This property is a synonym for encoding.|
|creativeWorkStatus | CreativeWork | DefinedTerm \| Text | 0,1 | The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle.|
|dateModified |	CreativeWork |Date \| DateTime | 0,1| The date on which the CreativeWork was most recently modified or updated. | 
|keywords | CreativeWork | DefinedTerm  \| Text \| URL	| 0+ |Keywords or tags used to describe the dataset, delimited by commas.|
|funding| CreativeWork | Grant | 0+ | A Grant that directly or indirectly provide funding or sponsorship for creation of the dataset.|


The following is an example implementation of recommended metadata
properties for a Schema.org Dataset item:

<pre lang="json">
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
  <strong>
  "creativeWorkStatus": "published",
  "dateModified": "2022-08-16T17:35:21+00:00",
  "keywords": ["Hurricane", "Flood", "Texas"],
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
  "hasPart": [
    {
      "@type": "Dataset",
      "url": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp?zipped=true&aggregation=true",
      "isPartOf": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51",
      "associatedMedia": [
        {
          "@type": "MediaObject",
          "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp.xml",
          "encodingFormat": "application/fgdc+xml",
          "contentSize": "88.0 KB"
        },
        {
          "@type": "MediaObject",
          "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shx",
          "encodingFormat": "x-gis/x-shapefile",
          "contentSize": "412.0 B"
       },
       {
         "@type": "MediaObject",
         "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.shp",
         "encodingFormat": "x-gis/x-shapefile",
         "contentSize": "7.6 MB"
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
         "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.dbf",
         "encodingFormat": "application/octet-stream",
         "contentSize": "1.8 KB"
      },
      {
         "@type": "MediaObject",
         "contentUrl": "https://www.hydroshare.org/resource/9d413b9d57824a79b8239a5f7c4fdf51/data/contents/HUC6_Harvey_TxLaMsAr.cpg",
         "encodingFormat": "x-gis/x-shapefile",
         "contentSize": "5.0 B"
      }
    ]
   }
  ]</strong>
}
</pre>
