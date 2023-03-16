# Dataset Metadata

To classify a record as a dataset, `"@type": "Dataset"` should be used in the json schema. This will classify the record as a specific Schema.Org type called `Dataset` for which the metadata should be described using the [core metadata](https://github.com/I-GUIDE/data-catalog/blob/main/schema/core.md), as well as the dataset-specific properties for the [Schema:Dataset](https://schema.org/Dataset) class. The following table outlines the required and optional properties selected from Schema.Org vocabulary to design the I-GUIDE dataset metadata schema. These properties are encoded as `1` or `1+` 
for **required** and `0,1` or `0+` for **optional** in the Cardinality column of the table below. 

|Property|Class|Expected Type|Cardinality|Description|
|---|---|---|---|---|
|[`Schema:distribution`](https://schema.org/distribution)| Dataset| DataDownload | 1+ | A downloadable form of this dataset, at a specific location, in a specific format. This property can be repeated if different variations are available. There is no expectation that different downloadable distributions must contain exactly equivalent information (see also DCAT on this point). Different distributions might include or exclude different subsets of the entire dataset, for example.|
|[`Schema:variableMeasured`](https://schema.org/variableMeasured)| Dataset | Text \| PropertyValue | 0+| The variableMeasured property can indicate (repeated as necessary) the variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue. |
|[`Schema:includedInDataCatalog`](https://schema.org/includedInDataCatalog)| Dataset | DataCatalog | 0,1 | A data catalog which contains this dataset. |

The following examples demonstrate how each of these properties may
be implemented in JSON+LD. 

### Distribution

The [`Schema:distribution`](https://schema.org/distribution) is a property of the [Schema:Dataset](https://schema.org/Dataset) class and must be expressed using the [`Schema:DataDownload`](https://schema.org/DataDownload) subtype. `Distribution` describes how the content related to the catalog record may be obtained. The `DataDownload` type contains a number of optional properties including `contentUrl`, `contentSize`, and `encodingFormat` that can be used to describe the downloadable content of the dataset.

``` json
{
    "@context" : "https://schema.org/",
    "@type" : "Dataset",
    "name":"Fiber-optic distributed temperature sensing data collected in mine-impacted streams near Silverton, Colorado in September 2019 and 2021 (ver. 2.0, May 2022)",
    "url":"https://www.sciencebase.gov/catalog/item/626b086bd34e76103cd183c5",
    "identifier":"",
    "description":"This dataset contains fiber-optic distributed temperature sensing (FO-DTS) data collected along the streambed interface of two streams named Cement Creek and California Gulch Creek, as well as the Animas River, located near Silverton Colorado. ",

    ...

    "distribution": {
            "@type":"DataDownload",
            "name":"Fiber_opticdist.zip",
            "contentUrl":"https://www.sciencebase.gov/catalog/file/get/626b086bd34e76103cd183c5",
            "encodingFormat": "application/zip",
            "contentSize": "439 MB",
            "comment":"Downloading all the data within this dataset"
    }
}
```

### Variable Measured

[`Schema:variableMeasured`](https://schema.org/variableMeasured) is a property of the `Dataset` class and can be expressed as either `Text` or a [`Schema:PropertyValue`](https://schema.org/PropertyValue), the latter being preferred. The `variableMeasured` represents the scientific variables that are measured or present within the dataset. Note, the `PropertyValue` type contains a number of useful properties that may be implements including units, min/max values, etc. For a complete list of properties see the [`Schema:PropertyValue`](https://schema.org/PropertyValue) definition.

``` json
{
    "@context" : "https://schema.org/",
    "@type" : "Dataset",
    "name":"Fiber-optic distributed temperature sensing data collected in mine-impacted streams near Silverton, Colorado in September 2019 and 2021 (ver. 2.0, May 2022)",
    "url":"https://www.sciencebase.gov/catalog/item/626b086bd34e76103cd183c5",
    "description":"This dataset contains fiber-optic distributed temperature sensing (FO-DTS) data collected along the streambed interface of two streams named Cement Creek and California Gulch Creek, as well as the Animas River, located near Silverton Colorado. ",

    ...
       
    "variableMeasured": {
        "@type": "PropertyValue",
        "name": "Streambed interface temperature values",
        "unitText": "degC"
    }
}
```

### Included in DataCatalog

DataCatalog is a collection of datasets. [`Schema:includedInDataCatalog`](https://schema.org/includedInDataCatalog) can be used to show the data catalog containing a dataset. 

In the example below, we used the `includedInDataCatalog` property to show that the dataset is included in the U.S. Geological Survey Science Data Catalog (SDC). 


``` json
{
    "@context" : "https://schema.org/",
    "@type" : "Dataset",
    "name":"Fiber-optic distributed temperature sensing data collected in mine-impacted streams near Silverton, Colorado in September 2019 and 2021 (ver. 2.0, May 2022)",
    "url":"https://www.sciencebase.gov/catalog/item/626b086bd34e76103cd183c5",
    "description":"This dataset contains fiber-optic distributed temperature sensing (FO-DTS) data collected along the streambed interface of two streams named Cement Creek and California Gulch Creek, as well as the Animas River, located near Silverton Colorado. ",

    ...

    "includedInDataCatalog": {
        "@type" :"DataCatalog",
        "name": "The USGS Science Data Catalog (SDC)",
        "description" : "The Science Data Catalog (SDC) is the official public and searchable index that aggregates descriptions of all public research data that have been published by the USGS.",
        "url":"https://data.usgs.gov/datacatalog/",
        "identifier": "<internally-created-identifier>",
        "creator": "U.S. Geological Survey"
    } 
}
```