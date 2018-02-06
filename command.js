// Find _ids for matching locations based on some criteria (eg. "abbrev")
var matches = db.routes.find({src_ap: "DXB"}, {"dst_apid": 1, _id: 0});

// Transform matching _id values into an array
var dst = [];
matches.forEach(function(match) {
  if (match.dst_apid != null) {
    dst.push(match.dst_apid);
  }
});

// Look for widgets matching the location criteria
var results = [];
dst.forEach(function(one) {
  results.push(db.airports.find({"_id": one}, {"name": 1, "_id": 0}).toArray());
});

printjson(results);