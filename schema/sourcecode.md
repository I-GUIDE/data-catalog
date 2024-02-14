
# Software Source Code Metadata

To classify a record as a computer programming source code, `"@type: "SoftwareSourceCode"` should be used in the json schema. This will classify the record such as compile ready solutions, code snippet samples, scripts, etc. as a specific Schema.Org type called `SoftwareSourceCode` for which the metadata should be described using the [core metadata](https://github.com/I-GUIDE/data-catalog/blob/main/schema/core.md), as well as the software-source-code-specific properties for the [Schema:SoftwareSourceCode](https://schema.org/SoftwareSourceCode) class. The following table outlines the required and optional properties selected from Schema.Org vocabulary to design the I-GUIDE software source code metadata schema. These properties are encoded as `1` or `1+` for **required** and `0,1` or `0+` for **optional** in the Cardinality column of the table below.

|Property|Class|Expected Type|Cardinality|Description|
|---|---|---|---|---|
| [programmingLanguage](https://schema.org/programmingLanguage) | SoftwareSourceCode | ComputerLanguage \| Text | 1+ | The computer programming language |
| [runtimePlatform](https://schema.org/runtimePlatform) | SoftwareSourceCode | Text | 1+ | Runtime platform or script interpreter dependencies |
| [targetProduct](https://schema.org/targetProduct) | SoftwareSourceCode | [SoftwareApplication](https://github.com/I-GUIDE/data-catalog/blob/main/schema/softwareapp.md) | 1+ | Target Operating System or Product to which the code applies |
| [codeRepository](https://schema.org/codeRepository) | SoftwareSourceCode | URL \| Text | 0,1 | Link to the repository where the un-compiled, human readable code and related code is located |
| [codeSampleType](https://schema.org/codeSampleType) | Text | 0,1 | What type of code sample: full (compile-ready) solution, code snippet (incomplete), inline code, scripts, template |
| [text](https://schema.org/text) | CreativeWork | Text | 0,1 | The textual content of the source code. |

### Programming Language

[Schema:programmingLanguage](https://schema.org/programmingLanguage) is a property of the `Thing` class. It is used to encode the computer programming language of a record that is classified as a source code. 

A simple example is shown below.

``` json
{
  "programmingLanguage": "Python"
}
```

However, it is preferred for a programming language to be expressed as a [ComputerLanguage](https://schema.org/ComputerLanguage) class if possible. The following example illustrates how an identifier can be encoded as a `ComputerLanguage`.

``` json
{
  "programmingLanguage": {
    "@type": "ComputerLanguage",
    "name": "Python",
    "url": "https://www.python.org/",
    "description": "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
  }
}
```

### Runtime Platform

[Schema:runtimePlatform](https://schema.org/runtimePlatform) is a type of software platform that is used to indicate the platform or environment on which a given source code can be executed. Examples include Java v1, Python 3.9, .NET Framework 3.0. Here's an example of how  `RuntimePlatform` property is used to describe a software source code that can run using Ptyhon 3.9.

``` json
{
  "runtimePlatform": "Python 3.9"
}
```

### Target Product

[Schema:targetProduct](https://schema.org/targetProduct) is used in the context of software source code to describe a product that can use the source code. We use the `SoftwareApplication` class and some of its properties to specify `targetProduct`. Please refer to [SoftwareApplication](https://github.com/I-GUIDE/data-catalog/blob/main/schema/softwareapp.md) to learn more about its properties.  

Here is an example that describe a Python library intended to be used with a specific machine learning framework such as TensorFlow.

``` json
{
  "@type": "SoftwareSourceCode",
  "name": "Geospatial Library",
  "programmingLanguage": "Python",
  "targetProduct": {
    "@type": "SoftwareApplication",
    "name": "TensorFlow",
    "operatingSystem": ["Windows", "MacOS", "Linux"]
  }
}
```

An example of an IPython Jupyter Notebook as a `targetProduct` for a record in the data catalog classifed as a software source code can be shown as below.

``` json
{
  "targetProduct": {
      "@type": "SoftwareApplication",
      "name": "Jupyter Notebook",
      "applicationSuite": "JupyterLab",
      "operatingSystem": ["Windows", "MacOS", "Linux"]
    }
}
```

### Code Repository

[Schema:codeRepository](https://schema.org/targetProduct) is used to describe a software repository where source code is hosted and maintained, typically using a version control system such as Git. 

Here is the example of `codeRepository` that provides information about the GitHub repository of the next generation national water modeling project.

``` json
{
  "codeRepository": {
    "@type": "URL",
    "name": "Next Gen Water Modeling Framework",  
    "url": "https://github.com/NOAA-OWP/ngen",
    "description": ""
  }
}
```

### Code Sample Type

[schema:codeSampleType](https://schema.org/codeSampleType) can be used to represent the development stage of the source code. Examples include Incomplete Code, Partially Functional Code, Functional Code, Tested Code, Optimized Code, and Full (Compile-Ready) Code. The following example indicate that the TauDEM source code version 5.3.8 is a complete, working solution that is ready to be compiled. 

``` json
{
  "@type": "SoftwareSourceCode",
  "name": "Terrain Analysis Using Digital Elevation Models (TauDEM)",
  "codeRepository": "https://github.com/dtarb/TauDEM/tree/master",
  "version": "5.3.8",
  "programmingLanguage": ["Python", "C++"],
  "codeSampleType": "Full (compile ready)"
}
```

### Code Textual Content

[schema:text](https://schema.org/text) can be used to indicate the textual content of the code. The following example uses `text` property to represent the content of a python script that loads the AORC meteorological dataset and prints out its spatial dimensions.  

``` json
{
  "@type": "SoftwareSourceCode",
  "name": "Load the AORC v1.0 Data and Check its Dimensions",
  "programmingLanguage": "Python",
  "text": "import xarray \n 
          # load a single month of data \n  
          ds = xarray.open_dataset('http://thredds.hydroshare.org/thredds/dodsC/aorc/data/16/201001.nc',
                        chunks={'Time': 10, 'west_east': 285, 'south_north':275},
                        decode_coords='all')} \n
          print(ds.south_north) \n
          print(ds.west_east)"
}
```
