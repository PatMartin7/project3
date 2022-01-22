// Creating the map object
var myMap = L.map("map", {
    center: [54.135258, -4.341021],
    zoom: 7
  });
  
  // Adding the tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);
  

//bring flask variable to javascript
const dataresult = fetch("/api").then((response) => response.json())
    .then((entry) => {
        return entry;
    });
const data = async () => {
    const a = await dataresult;
    console.log(a);
    var markers = L.markerClusterGroup();

    for (let i=0; i < a.Mongo.length; i++) {
      try{
        markers.addLayer(L.marker([a.Mongo[i].Latitude, a.Mongo[i].Longitude])
            .bindPopup(`<h2> ${a.Mongo[i]["First Name"][0]} ${a.Mongo[i]["Last Name"][0]} </h2><hr> 
            <h4>Died on ${a.Mongo[i]["Date of Death"][1]} ${a.Mongo[i]["Date of Death"][0]}, ${a.Mongo[i]["Date of Death"][2]} </h4>`))
      }
      catch (error) {
        console.log(error);
      }
    }
    myMap.addLayer(markers);
};

data();


  
