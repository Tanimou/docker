// function init() {
var test
var zoomlet
    var mainLayer
    if(test===undefined){
    var test = {
        lat: 5.395609,
        lng: -3.978498
    }
}
if (zoomlet === undefined) {
    var zoomlet = 5;
}
    
mapp=document.querySelector('#map')
var map = L.map(mapp).setView([test.lat, test.lng], zoomlet);

if (mainLayer === undefined) {
 
    const mainlayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 5,
    attribution: '© OpenStreetMap'
    });
    mainlayer.addTo(map);
}




var marker = L.marker([5.5, -3.97]).addTo(map);
var marker2 = L.marker([7.5, -1.97]).addTo(map);
var marker3 = L.marker([10.5, -8.97]).addTo(map);
    // }


    
