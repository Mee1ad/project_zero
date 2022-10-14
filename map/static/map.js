const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map("map");
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: attribution,
}).addTo(map);
const markers = JSON.parse(document.getElementById("markers-data").textContent);
let feature = L.geoJSON(markers)
    .bindPopup(function (layer) {
        return "ID: " + layer.feature.properties.pk
            + "<br>Name: " + layer.feature.properties.name
            + "<br>Lat: " + layer.feature.properties.lat
            + "<br>Long: " + layer.feature.properties.long
            + "<br>Category: " + layer.feature.properties.category
            + "<br>Description: " + layer.feature.properties.description
            + "<br><img width='150px' height='150px' src=" + layer.feature.properties.image + "/>";
    })
    .addTo(map);
map.fitBounds(feature.getBounds(), {padding: [100, 100]});