Find _ids for matching routes where the src airport is DXB
var matches = db.routes.find({src_ap: "DXB"}, {"dst_apid": 1, _id: 0});

// Store matching _id values into an array of ObjectIDs
var dst = [];
matches.forEach(function(match) {
  if (match.dst_apid != null) {
    dst.push(match.dst_apid);
  }
});

// Iterate through the array of ObjectIDs holding matching values of the previous query
// and use each id to find the matching airport, then get the name of that airport
var results = [];
dst.forEach(function(one) {
  results.push(db.airports.find({"_id": one}, {"name": 1, "_id": 0}).toArray());
});

// Print results as json
printjson(results);