The document outlines the Schema.org properties used to describe a single ESRI Shapefile.
A Shapefile is a geospatial vector file format that is developed and regulated
by ESRI. It consists of several mandatory files (`.shp`, `.shx`, `.dbf`) as
well as numerous optional files (`.prj`, `.sbn`, `.sbx`, `.fbn`, `.fbx`,`.ain` `.aih`, `.ixs`, `.mxs`, `.atx`, `.shp.xml`, `.cpg`, `.qix`).

While all SchemaOrg properties are valid, below is a suggested subset to
represent a single Shapefile object.


**Properties inherited from SchemaOrg.Thing**

|Property|Type|Cardinality|Description|
|---|---|---|---|
|name| Text | 1 | Name of the item |
|description| Text | 0,1 | Description of the item|
|url| URL | 1 | URL of the item |
|subjectOf| CreativeWork \| Event | 0,1 | A CreativeWork or Event about this Thing. |



**Properties inherited from SchemaOrg.Thing.CreativeWork**

|Property | Type | Cardinality | Description |
|---|---|---|---|
|abstract |Text | 0,1 |	An abstract is a short description that summarizes a CreativeWork. |
|author	| Organization \| Person | 1* |	The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.|
|contentReferenceTime | DateTime | 0,1| The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.|
|contributor | Organization \| Person | 0* | A secondary contributor to the CreativeWork or Event. |
|creativeWorkStatus | DefinedTerm \| Text | 0,1 | The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle.|
|creator | Organization \| Person | 0* | The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork. |
| dateCreated | Date \| DateTime | 1 | The date on which the CreativeWork was created or the item was added to a DataFeed.|
|dateModified |	Date \| DateTime | 0,1| The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.|
|keywords | DefinedTerm  \| Text \| URL	| 0* |Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.|
|schemaVersion|Text \| URL | 0,1 | Indicates (by URL or string) a particular version of a schema used in some CreativeWork. This property was created primarily to indicate the use of a specific schema.org release, e.g. 10.0 as a simple string, or more explicitly via URL, https://schema.org/docs/releases.html#v10.0. There may be situations in which other schemas might usefully be referenced this way, e.g. http://dublincore.org/specifications/dublin-core/dces/1999-07-02/ but this has not been carefully explored in the community.|
|spatialCoverage | Place | 1 | The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content. It is a subproperty of contentLocation intended primarily for more technical and detailed materials. For example with a Dataset, it indicates areas that the dataset describes: a dataset of New York weather would have spatialCoverage which was the place: the state of New York.|
|funding| Grant | 0* | A Grant that directly or indirectly provide funding or sponsorship for this item. See also ownershipFundingInfo.|

**Properties inherited from SchemaOrg.Thing.DataSet**

|Property | Type | Cardinality | Description |
|---|---|---|---|
|variableMeasured| PropertyValue \| Text | 0* | The variableMeasured property can indicate (repeated as necessary) the variables that are measured in some dataset, either described as text or as pairs of identifier and description using PropertyValue.|
|distribution | DataDownload | 3* | A dataset in downloadable form. A valid shapefile must contain three files: `.shp`, `.shx`, and `dbf`. Therefore a valid SchemaOrg representation must contain 3 or more distribution elements.|


**Example JSON+ld Example**

An example implementation of these SchemaOrg fields can be found
[here](shapefile-json-ld.md)


### Notes 

- the `distribution` element was chosen instead of `associatedMedia` for
  representing the individual files of a dataset following the recommendation
  of ESIPFed/Science-on-Schema.org working group. Specifically the following
  discussion:
    - https://github.com/ESIPFed/science-on-schema.org/issues/4 

- the HydroShare resource containing the shapefile is referenced using the
  `subjectOf` element following the recommendations in the following link. This
  is because the HydroShare resource is just a metadata representation of the
  data.
    - https://github.com/ESIPFed/science-on-schema.org/blob/226-esip-summer-mtg-2022-tutorial/tutorials/esip-summer-mtg-2022/18_checksums.md

