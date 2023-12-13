
# with ome-types environment
* `xsdata generate ome-2016-06.xsd --output pydantic-basemodel`
* write ome.schema.json
* edit ome.schema.json to remove timepoints

# with linkml environment
* `schemauto import-json-schema ome-edited.schema.json --output ome.yaml`
* edit yaml to have nice URIs
* `gen-owl -f xml ome-edited.yaml --output ome.owl`
* `./robot convert --input ome-edited.owl --output ome.obo`
