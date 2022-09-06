/**@odoo-module**/
//import { returneresult } from './main.18'

var test
var zoomlet
var mainLayer
if (test === undefined) {
    var test = {
        lat: 5.393393,
        lng: -3.976322
    }
}
if (zoomlet === undefined) {
    var zoomlet = 15;
}

var mapp = document.querySelector('#map')
var map = L.map(mapp).setView([test.lat, test.lng], zoomlet);

if (mainLayer === undefined) {

    const mainlayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 25,
        attribution: '© OpenStreetMap'
    });
    mainlayer.addTo(map);
}
    var value
    const {returneresult} = require('./main.18')
console.log(returneresult)
for (let key in result) {
    if (result.hasOwnProperty(key)) {
        value = result[key];
        // console.log(key, value);
        map.setView([result[key]["Lat"], result[key]["Long"]], 15)
        var marker = L.marker([result[key]["Lat"], result[key]["Long"]]).addTo(map);
        marker.bindPopup(result[key]["CarModel"]).openPopup();
    }
}

//export default map;
//

// L.Routing.control({
//     waypoints: [
//         L.latLng(5.393937, -3.976591),
//         L.latLng(5.393393, -3.976322)
//     ]
// }).addTo(map);

// }
