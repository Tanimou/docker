
odoo.define(
    'car_management.car_map_view22',

    function (require) {
        console.log('yolaaaaaaa')
        var __exports = {};
        var formController = require("web.FormController");
     //   var Widget = require('web.Widget');

        // var Counter = Widget.extend({
        //     template: 'some.template',
        //     events: {
        //         'click button': '_onClick',
        //     },
        //     init: function (parent, value) {
        //         this._super(parent);
        //         this.count = value;
        //     },
        //     _onClick: function () {
        //         this.count++;
        //         this.$('.val').text(this.count);
        //     },
        // });
        var ExtendedFormController = formController.include({

            init: function () {

                var res= this._super.apply(this, arguments);
                function parseURLParams(url) {
                    var queryStart = url.indexOf("#") + 1,
                        queryEnd = url.length + 1,
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
// C'est ici que j'extrait les informations de latitude et longitude à partir de l'url et je les applique sur la carte(voir main.77.js)
                if (this.modelName == "position.vehicle") {
                    //window.location.reload()
                    var self = this;
                     var url = window.location.href;
                    // var page_url = url.replace("#", "?");
                    var params = parseURLParams(url);
                  //  console.log(params)
                    self._rpc({
                        model: "stock.picking",
                        method: "search_read",
                        fields: ["vehicle_id","latitude","longitude","latitudeF","longitudeF"],
                        domain: [["id", "=", params.id[0]]],
                        context: self.context,
                    }).then(function (result) {
                        this.result = result
                           console.log(result)

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
            //c'est la fonction qui s'execute quand on appuie sur le boutton save de la vue form. Il n'ya pas de probleme avec cette fonction
            // saveRecord: function () {

            //     var res = this._super.apply(this, arguments)
            //     // function parseURLParams(url) {
            //     //     var queryStart = url.indexOf("#") + 1,
            //     //         queryEnd =  url.length + 1,
            //     //         query = url.slice(queryStart, queryEnd - 1),
            //     //         pairs = query.replace(/\+/g, " ").split("&"),
            //     //         parms = {}, i, n, v, nv;
            //     //     if (query === url || query === "") return;
            //     //     for (i = 0; i < pairs.length; i++) {
            //     //         nv = pairs[i].split("=", 2);
            //     //         n = decodeURIComponent(nv[0]);
            //     //         v = decodeURIComponent(nv[1]);
            //     //         if (!parms.hasOwnProperty(n)) parms[n] = [];
            //     //         parms[n].push(nv.length === 2 ? v : null);
            //     //     }
            //     //     return parms;
            //     // }

            //     if (this.modelName == "position.vehicle") {
            //         var self = this;
            //         //var url = window.location.href;
            //        // var page_url = url.replace("#", "?");
            //       //  var params = parseURLParams(url);

            //         self._rpc({
            //             model: "fleet.vehicle",
            //             method: "search_read",
            //             fields: ["name", "latitude", "longitude"],
            //             domain: [["id", "=", params.id[0]]],
            //             context: self.context,
            //         }).then(function (result) {
            //             window.location.reload()
            //             this.result = result
            //             //  console.log(result)


            //             //  console.log(result)
            //             //var map2 = L.map(mapp).setView([test.lat, test.lng], zoomlet);
            //         })
            //     }
            //     return res
            // }


        })

    })
