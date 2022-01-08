//bring flask variable to javascript
fetch('/api').then((res)=>{ console.log(res)})

// Create a map object.
var myMap = L.map("map", {
    center: [15.5994, -28.6731],
    zoom: 3
  });
  
  // Add a tile layer.
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);