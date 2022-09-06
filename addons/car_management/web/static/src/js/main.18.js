
odoo.define(
    'car_management.car_map_view',

    function (require) {
        console.log('yolaaaaaaa')
        var __exports = {};
        var formController = require("web.FormController");
        var ExtendedFormController = formController.include({

            init: function () {

                var res= this._super.apply(this, arguments);
                // function parseURLParams(url) {
                //     var queryStart = url.indexOf("?") + 1,
                //         queryEnd = url.indexOf("#") + 1 || url.length + 1,
                //         query = url.slice(queryStart, queryEnd - 1),
                //         pairs = query.replace(/\+/g, " ").split("&"),
                //         parms = {}, i, n, v, nv;
                //     if (query === url || query === "") return;
                //     for (i = 0; i < pairs.length; i++) {
                //         nv = pairs[i].split("=", 2);
                //         n = decodeURIComponent(nv[0]);
                //         v = decodeURIComponent(nv[1]);
                //         if (!parms.hasOwnProperty(n)) parms[n] = [];
                //         parms[n].push(nv.length === 2 ? v : null);
                //     }
                //     return parms;
                // }

                if (this.modelName == "car.car") {
                    var self = this;
                    // var url = window.location.href;
                    // var page_url = url.replace("#", "?");
                    // var params = parseURLParams(page_url);
                    self._rpc({
                        model: "car.car",
                        method: "search_read",
                        fields: ["CarModel", "Lat", "Long"],
                        //domain: [["id", "=", params.id[0]]],
                        context: self.context,
                    }).then(function (result) {
                        this.result = result
                        //   console.log(result)

                        // localStorage.resultat=JSON.stringify(result["0"])
                        __exports.returneresult = function () {
                            return result
                        }
                        return __exports
                        //var map2 = L.map(mapp).setView([test.lat, test.lng], zoomlet);
                    })
                }
                return res
            }
            ,
            saveRecord: function () {

                var res = this._super.apply(this, arguments)
                function parseURLParams(url) {
                    var queryStart = url.indexOf("?") + 1,
                        queryEnd = url.indexOf("#") + 1 || url.length + 1,
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

                if (this.modelName == "car.car") {
                    var self = this;
                    var url = window.location.href;
                    var page_url = url.replace("#", "?");
                    var params = parseURLParams(page_url);

                    self._rpc({
                        model: "car.car",
                        method: "search_read",
                        fields: ["CarModel", "Lat", "Long"],
                        domain: [["id", "=", params.id[0]]],
                        context: self.context,
                    }).then(function (result) {
                        this.result = result
                        //  console.log(result)


                        //  console.log(result)
                        //var map2 = L.map(mapp).setView([test.lat, test.lng], zoomlet);
                    })
                }
                return res
            }


        })

    })
