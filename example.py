import parse_pln

filename = input ("Enter .PLN file name to parse> ")

parsed_dictionary = parse_pln.parse_pln_file(filename)
print(parsed_dictionary)

input("Press key to tidy waypoint lat / lons into sensible format")

fixed_dictionary = parse_pln.fix_waypoints(parsed_dictionary)
print (fixed_dictionary)

input("Press key to write the dictionary to JSON")

parse_pln.save_json_file("output.json", fixed_dictionary)