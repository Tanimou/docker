// function init() {
// var test
// var zoomlet
//     var mainLayer
//     if(test===undefined){
//     var test = {
//         lat: 5.393937,
//         lng: -3.976591
//     }
// }
// if (zoomlet === undefined) {
//     var zoomlet = 15;
// }

// mapp=document.querySelector('#map')
// var map = L.map(mapp).setView([test.lat, test.lng], zoomlet);

// if (mainLayer === undefined) {

//     const mainlayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 25,
//     attribution: '© OpenStreetMap'
//     });
//     mainlayer.addTo(map);
// }




//var marker = L.marker([5.393937, -3.976591]).addTo(map);
//var marker2 = L.marker([5.393393, -3.976322]).addTo(map);
// L.Routing.control({
//     waypoints: [
//         L.latLng(5.393937, -3.976591),
//         L.latLng(5.393393, -3.976322)
//     ]
// }).addTo(map);

// }

odoo.define(
    'car_management.carmap',

    function (require) {
        console.log('yolaaaaaaa')
        'use strict'
        var formController = require("web.FormController");
        var ExtendedFormController = formController.include({
            saveRecord: function () {
                var res = this._super.apply(this, arguments)
                if (this.modelName == "car.car") {
                    var self = this;
                    self._rpc({
                        model: "car.car",
                        method: "search_read",
                        fields: ["CarModel", "Lat", "Long"],
                        context: self.context,
                    }).then(function (result) { console.log(result) })
                    return res
                    // var record = this.model.get(this.handle, {raw: true});
                    // var recordData = record.data;
                    // var lat = recordData.lat;
                    // var lng = recordData.lng;
                    // var zoom = recordData.zoom;
                    // var map = document.querySelector('#map')
                    // var map = L.map(map).setView([lat, lng], zoom);
                    // var mainLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    // maxZoom: 25,
                    // attribution: '© OpenStreetMap'
                    // });
                    // mainLayer.addTo(map);
                    // var marker = L.marker([lat, lng]).addTo(map);
                }
            }
        })
    }
)