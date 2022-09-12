/** @odoo-module **/

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
    var zoomlet = 10;
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
function parseURLParams(url) {
    var queryStart = url.indexOf("#") + 1,
        queryEnd =  url.length + 1,
        query = url.slice(queryStart, queryEnd - 1),
        pairs = query.replace(/\+/g, " ").split("&"),
        parms = {}, i, n, v, nv;
    if (query === url || query === "") return;
    for (i = 0; i < pairs.length; i++) {
        nv = pairs[i].split("=", 2);
        n = decodeURIComponent(nv[0]);
        v = decodeURIComponent(nv[1]);
        if (!parms.hasOwnProperty(n)) parms[n] = [];
        parms[n].push(nv.length === 2 ? v : null);
    }
    return parms;
}

var url = window.location.href;

//var page_url = url.replace("#", "?")
//var page_url2 = page_url.replace("&", "é")
var params = parseURLParams(url);

console.log(params)

for (let key in result) {
    if (result.hasOwnProperty(key)) {
        value = result[key];
        if (params.active_id[0] == result[key]["id"]) {
            // console.log(key, value);
            map.setView([result[key]["latitude"], result[key]["longitude"]], 10)
              L.Routing.control({
        waypoints: [
                      L.latLng(result[key]["latitude"], result[key]["longitude"]),
                      L.latLng(result[key]["latitudeF"], result[key]["longitudeF"])
        ]
    }).addTo(map);

          //  var marker = L.marker([result[key]["latitude"], result[key]["longitude"]]).addTo(map);
           // marker.bindPopup(result[key]["vehicle_id"][1]).openPopup();
        }
    }
    //import { returneresult } from './main.18'



    //export default map;
    //

  
    // }
}