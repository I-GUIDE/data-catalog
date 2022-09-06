
# Software Source Code

This document outlines the *required* and *recommended* properties for
describing source code.

While all Schema.org properties are valid, below is a suggested subset to
represent a single source code object using the 
*[SoftwareSourceCode](https://schema.org/SoftwareSourceCode)* class.

**Note**: A valid source code entry must include the required metadata outlined
in the [Core Metadata](core.md) document, which are not
described on this page.

#### Required Properties
|Property|Class|Type|Cardinality|Description|
|---|---|---|---|---|
| programmingLanguage | SoftwareSourceCode | ComputerLanguage \| Text | 1+ | The computer programming language |
| runtimePlatform | SoftwareSourceCode | Text | 1+ | Runtime platform or script interpreter dependencies |
| targetProduct | SoftwareSourceCode | SoftwareApplication | 1+ | Target Operating System or Product to which the code applies |

The following is an example implementation of the required metadata
properties for a software source code object.

```json
{
  "@type": "Dataset",
  "@context": "https://schema.org/",
  "name": "Comparing Daily Residential Water Use at Richards Hall",
  "description": "This resource contains a dataset and code to analyze average day to day water use at a residential hall at Utah State University (USU). Included in this resource is a .csv file that contains high resolution time series of water flow from a residential building on the USU campus. The data was recorded every one second for approximately three weeks in 2017. The Jupyter Notebook in this resource demonstrates how to subset the Richards Hall dataset to analyze daily water use from March 18-24, 2017. It resamples the data to daily total volume and finds the daily average, then plots the average daily volume in gallons for each day of the week.",
  "url": "https://www.hydroshare.org/resource/2f2838b4964747c4acb2ce28d5f300b3/",
  "dateCreated": "2022-04-14T18:27:00+00:00",
 "author": {
    "@type": "Person",
    "name": "Emily Jainarain",
    "email": "emily.jainarain@usu.edu"
  },
  "hasPart": {
    "@type": "SoftwareSourceCode",
    "name": "DailyResidentialWaterUse.ipynb",
    "url":
    "https://www.hydroshare.org/resource/2f2838b4964747c4acb2ce28d5f300b3/data/contents/DailyResidentialWaterUse.ipynb",
    "programmingLanguage": {
      "@type": "ComputerLanguage",
      "name": "Python",
      "url": "https://www.python.org/",
      "description": "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed."
    },
    "runtimePlatform": "Python 3.9",
    "targetProduct": {
      "@type": "SoftwareApplication",
      "name": "Jupyter Notebook",
      "applicationSuite": "JupyterLab",
      "operatingSystem": "MacOS, Linux"
    },
    "associatedMedia": [{
        "@type": "MediaObject",
        "contentUrl":
        "https://www.hydroshare.org/resource/2f2838b4964747c4acb2ce28d5f300b3/data/contents/DailyResidentialWaterUse.ipynb",
        "encodingFormat": "application/x-ipynb+json",
        "contentSize": "33.9 KB"
      }
    ]
  }

}
```




#### Recommended Properties
|Property|Class|Type|Cardinality|Description|
|---|---|---|---|---|
| maintainer | CreativeWork | Person \| Organization | 1+ |A maintainer is a Person or Organization that manages contributions to, and/or publication of, some (typically complex) artifact |
| license | CreativeWork | CreativeWork \| URL | 1 | A license document that applies to this content, typically indicated by URL |
| version | CreativeWork | Number \| Text | 1 | The version of the CreativeWork embodied by a specified resource |
| codeRepository | SoftwareSourceCode| URL | 1 | Link to the repository where the un-compiled, human readable code and related code is located |
| codeSampleType | SoftwareApplication | Text | 1 | 	What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template |

## TODO
```
{
  ...

}
```
