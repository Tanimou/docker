// function init() {
    
    const test = {
        lat: 5.395609,
        lng: -3.978498
    }

    const zoomlet = 13;

    var map = L.map('map').setView([test.lat, test.lng], zoomlet);

    const mainlayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
    });

    mainlayer.addTo(map);
    var marker = L.marker([51.5, -0.09]).addTo(map);
// }


    console.log('car_management.carmap loaded successfully')
