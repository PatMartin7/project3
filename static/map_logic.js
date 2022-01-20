// Creating the map object
var myMap = L.map("map", {
    center: [40.7, -73.95],
    zoom: 11
  });
  
// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);

// //bring flask variable to javascript
// const dataresult = fetch("/api").then((response) => response.json())
//     .then((entry) => {
//         return entry;
//     });
// const data = async () => {
//     const a = await dataresult;
//     console.log(a);
//     var markers = L.markerClusterGroup();
//     markers.addLayer(L.marker([a.Latitude, a.Longitude])
//         .bindPopup(a["First Name"][0] + " " + a["Last Name"][0]))
//     myMap.addLayer(markers);
// };

// data();


  
