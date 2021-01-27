# msfs-pln-file-parser
 
Microsoft Flight Simulator 2020 uses .PLN files to plan routes.

They can be generated through the simulator or third party tools such as Navigraph or SimBrief.

They're also pretty annoying because:

1. They use XML. Is this 1999?

2. They display latitude and longitude in a format which is pretty difficult to do anything with.


This simple script does a few things:

1. Reads an PLN file into a Python dictionary so you can do something with it. Call *parse_pln_file(filename)* to do this.

2. Reads the latitudes and longitudes in the annoying PLN format and converts them to decimal lat/lons which you can, for instance, plot on a map. Call *simplify_route(source_dictionary)* to do this.

3. Outputs this all to a lovely usable JSON. Call *save_json_file(output_filename, source_dictionary)* to do this.


It also includes an example.py to show how it works and a sample.pln file which you can use to test.
