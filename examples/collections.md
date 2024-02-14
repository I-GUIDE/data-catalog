# Resource Collection

The following contains examples for various collections of data.

- [Collection of Resources](#collection-of-resources)
- [Collection of Collections](#collection-of-collections)
- [Collection and Dataset](#collection-and-dataset)



## Collection of Resources

Because the resources referenced in this example contain metadata described on another web page, they are expressed using the `hasPart` property.

```json

{
    "@context": "https://schema.org",
    "@type": "CreativeWork",
    "name": "Illilouette Creek Basin Weather Stations",
    "description": "This data is part of a project studying the effects of wildfire on the Illilouette Creek Basin, a watershed within Yosemite National Park. Three temporary weather stations were installed under distinct types of vegetation cover (A is forested, B is shrub\u002Ddominated, and C is in a wetland). Each station measures air temperature, relative humidity, rainfall (the rain gage is not heated, so only the portion of snowfall that melts within the gage is measured), wind speed and direction, solar radiation, and both soil moisture and temperature at three depths. These measurements are recorded every 10 minutes, beginning in the summer of 2015. The stations are located within an area that burned most recently in 2004 and 2017. For descriptions of the data format and units, see the included WeatherStnMetadata.xlsx file.",
    "url": "https://www.hydroshare.org/resource/9ccbb5e2754f40d1bda439f5020f252a",
    "identifier": "_9ccbb5e2754f40d1bda439f5020f252a",
    "creator": {
      "@list": [
            {
                  "@type": "Person",
                  "email": "gboisrame@berkeley.edu",
                  "name": "Gabrielle Boisrame",
                  "url": "https://www.hydroshare.org/user/1281/"
            },
            {
                  "@type": "Person",
                  "affiliation": {
                        "@type": "Organization",
                        "name": "UC Berkeley"
                  },
                  "email": "sally.thompson@berkeley.edu",
                  "name": "Sally Thompson"
            }
      ]
    },
    "dateCreated": "2017-04-14T21:31:16.122742+00:00",
    "keywords": ["temperature", "humidity", "solar radiation", "soil moisture", "precipitation", "wind", "Yosemite"],
	"license": "http://creativecommons.org/licenses/by/4.0/",
	"provider": {
        "@type": "Organization",
        "name": "HydroShare",
        "url": "https://www.hydroshare.org"
    }, 
    "creativeWorkStatus": "Discoverable",
    "inLanguage": "en-US",    
    "temporalCoverage": "2015-07-30/2021-06-20",
    "spatialCoverage": {
        "@type": "Place",
        
        "name": "Illilouette Creek Basin",
        
        "geo": {
            
            "@type": "GeoShape",
            "box": "37.6754 -119.5668 37.6765 -119.5649"
            
        }
    },
    "funding": [
    
        {
            "@type": "Grant",
            "identifier": "",
            "name": "",
            "funder": {
                "@type": "Organization",
                "name": "Joint Fire Science Program",
                "identifier": "https://www.firescience.gov/"
            }
        },
        
        {
            "@type": "Grant",
            "identifier": "",
            "name": "Critical Zone Collaborative Network",
            "funder": {
                "@type": "Organization",
                "name": "National Science Foundation",
                "identifier": ""
            }
        }
        
    ],
    "hasPart": [
    	{
    		"@type": "DataSet",
    		"name": "Illilouette Creek Basin Weather Station B",
    		"description": "This data is part of a project studying the effects of wildfire on the Illilouette Creek Basin, a watershed within Yosemite National Park. Three temporary weather stations were installed under distinct types of vegetation cover. Each station measures air temperature, relative humidity, rainfall (the rain gage is not heated, so only the portion of snowfall that melts within the gage is measured), wind speed and direction, solar radiation, and both soil moisture and temperature at three depths. These measurements are recorded every 10 minutes, beginning in the summer of 2015. Station B is located in a shrub field within an area that burned at high severity in 2004 and in 2017 (Empire Fire).. For descriptions of the data format and units, see the included WeatherStnMetadata.xlsx file.",
    		"identifier": "_0ddbdb4bd282436da9e4f3c032b30971",
    		"url": "https://www.hydroshare.org/resource/0ddbdb4bd282436da9e4f3c032b30971/"
    	},
    	    	{
    		"@type": "DataSet",
    		"name": "Illilouette Creek Basin Weather Station C",
    		"description": "This data is part of a project studying the effects of wildfire on the Illilouette Creek Basin, a watershed within Yosemite National Park. Three temporary weather stations were installed under distinct types of vegetation cover. Each station measures air temperature, relative humidity, rainfall (the rain gage is not heated, so only the portion of snowfall that melts within the gage is measured), wind speed and direction, solar radiation, and both soil moisture and temperature at three depths. These measurements are recorded every 10 minutes, beginning in the summer of 2015. Station C is located in a wetland within an area that burned most recently in 2004 and in 2017 (Empire Fire).. For descriptions of the data format and units, see the included WeatherStnMetadata.xlsx file.",
    		"identifier": "_9a00756fa3ee4a82872ffcd0cd40c3be",
    		"url": "https://www.hydroshare.org/resource/9a00756fa3ee4a82872ffcd0cd40c3be/"
    	},
    	    	{
    		"@type": "DataSet",
    		"name": "Illilouette Creek Basin Snow Depth Time Series",
    		"description": "This dataset is part of a project assessing the impacts of wildfires on the water balance of the Illilouette Creek Basin in Yosemite National Park. Three weather stations were mounted on poles in an area that had burned under various severities in 2004 and in 2017 (Empire Fire). Each station is located in a distinct vegetation type: closed canopy mixed conifer, shrubfield (dominated by Ceanothus cordulatus), and a wetland. Each weather station has at least two time lapse cameras capturing images four times per day. These images were used to calculate the depth of snow by comparing the height of the snowpack against the weather station pole or a nearby tree to known heights along the pole or tree. Measurements from different cameras at the same station may differ slightly from each other if snow piles up against the side of a pole, or if snow melts preferentially near a pole, but these differences are small compared to the maximum depths of snow. The data shows that peak snowpack was deepest at the wetland site, and shallowest under the closed canopy. Spring snowmelt also finished earliest in the closed canopy site.",
    		"identifier": "_95b3b827c1d14551bcfa11770df7748d",
    		"url": "https://www.hydroshare.org/resource/95b3b827c1d14551bcfa11770df7748d/"
    	},
    	    	{
    		"@type": "DataSet",
    		"name": "Illilouette Creek Basin Weather Station A",
    		"description": "This data is part of a project studying the effects of wildfire on the Illilouette Creek Basin, a watershed within Yosemite National Park. Three temporary weather stations were installed under distinct types of vegetation cover. Each station measures air temperature, relative humidity, rainfall (the rain gage is not heated, so only the portion of snowfall that melts within the gage is measured), wind speed and direction, solar radiation, and both soil moisture and temperature at three depths. These measurements are recorded every 10 minutes, beginning in the summer of 2015. Station A is located under a dense mixed conifer canopy in an area that burned at low severity in 2004 and in 2017 (Empire Fire). For descriptions of the data format and units, see the included WeatherStnMetadata.xlsx file.",
    		"identifier": "_0d212b8577d74bcca018f421fbd765d9",
    		"url": "https://www.hydroshare.org/resource/0d212b8577d74bcca018f421fbd765d9/"
    	},
    	    	{
    		"@type": "DataSet",
    		"name": "Illilouette Creek Basin Weather Station B",
    		"description": "This data is part of a project studying the effects of wildfire on the Illilouette Creek Basin, a watershed within Yosemite National Park. Three temporary weather stations were installed under distinct types of vegetation cover. Each station measures air temperature, relative humidity, rainfall (the rain gage is not heated, so only the portion of snowfall that melts within the gage is measured), wind speed and direction, solar radiation, and both soil moisture and temperature at three depths. These measurements are recorded every 10 minutes, beginning in the summer of 2015. Station B is located in a shrub field within an area that burned at high severity in 2004 and in 2017 (Empire Fire).. For descriptions of the data format and units, see the included WeatherStnMetadata.xlsx file.", 
    		"identifier": "_683e88318c8d4a54add8035207b19068",
    		"url": "https://www.hydroshare.org/resource/683e88318c8d4a54add8035207b19068/"
    	},
    	    	{
    		"@type": "DataSet",
    		"name": "Illilouette Creek Basin Weather Station C",
    		"description": "This data is part of a project studying the effects of wildfire on the Illilouette Creek Basin, a watershed within Yosemite National Park. Three temporary weather stations were installed under distinct types of vegetation cover. Each station measures air temperature, relative humidity, rainfall (the rain gage is not heated, so only the portion of snowfall that melts within the gage is measured), wind speed and direction, solar radiation, and both soil moisture and temperature at three depths. These measurements are recorded every 10 minutes, beginning in the summer of 2015. Station C is located in a wetland within an area that burned most recently in 2004 and in 2017 (Empire Fire).. For descriptions of the data format and units, see the included WeatherStnMetadata.xlsx file.",
    		"identifier": "_394bf620d1bb4e35bac8b2ce52bc75e1",
    		"url": "https://www.hydroshare.org/resource/394bf620d1bb4e35bac8b2ce52bc75e1/"
    	}
    ]
}
```

Why use `hasPart` instead of `citation` to describe the relationships that exist between the collection resource and the child resources? `hasPart` was chosen because it contains an inverse property called `isPartOf`. Each of the "child" resources use the `isPartOf` property to point to the collection resource which provides bidirectional navigation. Moreover, the `hasPart` property allows us to express the metadata for an entire `CreativeWork` if we want. The amount of metadata that is describe here can be chosen based on how the data will be rendered in the catalog. Including additional metadata, as needed, eliminates the need to invoke secondary searches to collect metadata. For instance, if we plan to allow the child resources to be downloaded from the collection resource, the `distribution` propery can also be included.

## Collection of Collections


## Collection and Dataset

In this scenario the resource contains both data and other resources as content. Since the data does not contain metadata elsewhere (i.e. it doesn't have its own landing page), these are expressed using `AssociatedMedia` and/or `Distribution` whereas the other resources use `hasPart`.