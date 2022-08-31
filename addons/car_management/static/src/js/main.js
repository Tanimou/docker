// function init() {
var test
var zoomlet
    var mainLayer
    if(test===undefined){
    var test = {
        lat: 5.393937,
        lng: -3.976591
    }
}
if (zoomlet === undefined) {
    var zoomlet = 15;
}
    
mapp=document.querySelector('#map')
var map = L.map(mapp).setView([test.lat, test.lng], zoomlet);

if (mainLayer === undefined) {
 
    const mainlayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 25,
    attribution: '© OpenStreetMap'
    });
    mainlayer.addTo(map);
}




var marker = L.marker([5.393937, -3.976591]).addTo(map);
//var marker2 = L.marker([5.393393, -3.976322]).addTo(map);
L.Routing.control({
    waypoints: [
        L.latLng(5.393937, -3.976591),
        L.latLng(5.393393, -3.976322)
    ]
}).addTo(map);
// for (let index = 0; index < 6; index++) {
//     var randomNumX = Math.random() * (5.393393 - 5.393937) + 5.393937;
//     var randomNumY = Math.random() * (-3.976322 + 3.976591) - 3.976591;
//     console.log(randomNumX, randomNumY);
//     X = Math.round(randomNumX * 10000) / 10000
//     Y = Math.round(randomNumY * 10000) / 10000
// var circle = L.circle([X,Y ], {
//     color: 'blue',
//     fillColor: 'blue',
//     fillOpacity: 0.5,
//     radius: 2
// }).addTo(map);
//     circle.bindPopup(X + " " + Y);
// }

//var marker3 = L.marker([10.5, -8.97]).addTo(map);
    // }


    
