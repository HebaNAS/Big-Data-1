results = db.countries.aggregate(
  {
    "$match": {"name": "United Arab Emirates"}
  }, {
    "$unwind": "$airlines"
  }, {
    "$sort": {"airlines.name": 1}
  }, {
    "$project" : {"airlines.name": 1, "_id": 0}
  }
).toArray();

printjson(results);