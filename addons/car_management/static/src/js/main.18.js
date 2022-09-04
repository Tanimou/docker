
odoo.define(
    'car_management.car_map_view',

    function (require) {
        console.log('yolaaaaaaa')

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
                    }).then(function (result) {
                        console.log(result["0"]["Lat"], result["0"]["Long"])

                        var marker2 = L.marker([result["0"]["Lat"], result["0"]["Long"]]).addTo(map);
                        marker2.bindPopup(result["0"]["CarModel"]).openPopup();
                        //var map2 = L.map(mapp).setView([test.lat, test.lng], zoomlet);


                    })

                }
                return res
            }
        })
    }
)
