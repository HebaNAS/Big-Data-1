# Copying Airlines Table from MySQL into a MongoDB Collection
# Airlines Table will be embedded as a subdocument inside Countries Collection on the Country Field
table "airlines", :embed_in => :countries, :on => :country do
  column "alid", :integer, :references => :airlines
  column "name", :text
  column "iata", :string
  column "country", :string, :references => :countries
end

# Copying Airlines Table from MySQL into a MongoDB Collection
table "airlines" do
  column "alid", :key, :as => :integer
  column "name", :text
  column "iata", :string
  column "icao", :string
  column "callsign", :text
  column "country", :string, :references => :countries
  column "alias", :text
  column "mode", :string
  column "active", :string
end

# Copying Airports Table from MySQL into a MongoDB Collection
# Airports Table will be embedded as a subdocument inside Cities Collection on the City Field
table "airports", :embed_in => :cities, :on => :city do
  column "apid", :integer, :references => :airports
  column "name", :text
  column "city", :integer, :references => :cities
  column "iata", :text
end

# Copying Airports Table from MySQL into a MongoDB Collection
table "airports" do
  column "apid", :key, :as => :integer
  column "name", :text
  column "city", :integer, :references => :cities
  column "iata", :key, :as => :string
  column "icao", :string
  column "x", :float
  column "y", :float
  column "elevation", :integer
end

# Copying Routes Table from MySQL into a MongoDB Collection
# Routes Table will be embedded as a subdocument inside Airlines Collection on the Airline ID Field
table "routes", :embed_in => :airlines, :on => :alid do
  column "alid", :integer, :references => :airlines
  column "rid", :integer, :references => :routes
  column "src_ap", :string
  column "dst_ap", :string
  column "stops", :text
end

# Copying Routes Table from MySQL into a MongoDB Collection
table "routes" do
  column "rid", :key, :as => :integer
  column "alid", :integer, :references => :airlines
  column "src_ap", :string, :references => :airports
  column "src_apid", :integer, :references => :airports
  column "dst_ap", :string, :references => :airports
  column "dst_apid", :integer, :references => :airports
  column "codeshare", :text
  column "stops", :text
  column "equipment", :text
end

# Copying Countries Table from MySQL into a MongoDB Collection
table "countries" do
  column "code", :key, :as => :string
  column "name", :text
  column "city", :integer, :references => :cities
  column "oa_code", :string
  column "dst", :string
end

# Copying Cities Table from MySQL into a MongoDB Collection
# Cities Table will be embedded as a subdocument inside Countries Collection on the Country Field
table "cities", :embed_in => :countries, :on => :country do
  column "cid", :integer, :references => :cities
  column "name", :text
  column "country", :string, :references => :countries
  column "tz_id", :text
  column "airports", :integer, :references => :airports
end

# Copying Cities Table from MySQL into a MongoDB Collection
table "cities" do
  column "cid", :key, :as => :integer
  column "name", :text
  column "country", :string, :references => :countries
  column "timezone", :float
  column "tz_id", :text
end
