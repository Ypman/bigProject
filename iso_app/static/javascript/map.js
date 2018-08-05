AmCharts.makeChart( "mapdiv", {
  /**
   * this tells amCharts it's a map
   */
  "type": "map",

  /**
   * create data provider object
   * map property is usually the same as the name of the map file.
   * getAreasFromMap indicates that amMap should read all the areas available
   * in the map data and treat them as they are included in your data provider.
   * in case you don't set it to true, all the areas except listed in data
   * provider will be treated as unlisted.
   */
  "dataProvider": {
    "map": "worldLow",
    "responsive": {
       "enabled": true
    },
    "areas":[
      {"id": "DK", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{"id": "DKc1", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{ "id": "DKc2", "color": "#009900" },{ "id": "DKc3", "color": "#000099" },{ "id": "DKc4", "color": "#999900" },{ "id": "DKc5", "color": "#990099" },{ "id": "DKc6", "color": "#009999" },{ "id": "DKc7", "color": "#999999" },{ "id": "DKc8", "color": "#555555" },{"id": "DE", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{ "id": "DEc1", "color": "#990000" },{ "id": "DEc2", "color": "#009900" },{ "id": "DEc3", "color": "#000099" },{ "id": "DEc4", "color": "#999900" },{ "id": "DEc5", "color": "#990099" },{ "id": "DEc6", "color": "#009999" },{ "id": "DEc7", "color": "#999999" },{ "id": "DEc8", "color": "#555555" },{"id": "MA", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{ "id": "MAc1", "color": "#990000" },{ "id": "MAc2", "color": "#009900" },{ "id": "MAc3", "color": "#000099" },{ "id": "MAc4", "color": "#999900" },{ "id": "MAc5", "color": "#990099" },{ "id": "MAc6", "color": "#009999" },{ "id": "MAc7", "color": "#999999" },{ "id": "MAc8", "color": "#555555" },{"id": "AE", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{ "id": "AEc1", "color": "#990000" },{ "id": "AEc2", "color": "#009900" },{ "id": "AEc3", "color": "#000099" },{ "id": "AEc4", "color": "#999900" },{ "id": "AEc5", "color": "#990099" },{ "id": "AEc6", "color": "#009999" },{ "id": "AEc7", "color": "#999999" },{ "id": "AEc8", "color": "#555555" },{"id": "US", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{ "id": "USc1", "color": "#990000" },{ "id": "USc2", "color": "#009900" },{ "id": "USc3", "color": "#000099" },{ "id": "USc4", "color": "#999900" },{ "id": "USc5", "color": "#990099" },{ "id": "USc6", "color": "#009999" },{ "id": "USc7", "color": "#999999" },{ "id": "USc8", "color": "#555555"},{"id": "RU", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{"id": "RUc1", "color": "#990000", "description":"hier soll stehen, mit welcher source welche Methode funktioniert" },{ "id": "RUc2", "color": "#009900" },{ "id": "RUc3", "color": "#000099" },{ "id": "RUc4", "color": "#999900" },{ "id": "RUc5", "color": "#990099" },{ "id": "RUc6", "color": "#009999" },{ "id": "RUc7", "color": "#999999" },{ "id": "RUc8", "color": "#555555" },
    ]
  },

  /**
   * create areas settings
   * autoZoom set to true means that the map will zoom-in when clicked on the area
   * selectedColor indicates color of the clicked area.
   */
  "areasSettings": {
    "autoZoom": true,
    "selectedColor": "#CC0000"
  },

  // hierbe hätte ich natürlich
  legend: {
      width: "100%",
      divId: "legenddiv",
      marginRight: 27,
      marginLeft: 27,
      equalWidths: false,
      backgroundAlpha: 0.5,
      backgroundColor: "#FFFFFF",
      borderColor: "#ffffff",
      borderAlpha: 1,
      top: 450,
      left: 0,
      horizontalGap: 10,
      data: [{
        title: "v1",
        color: "#990000"
      }, {
        title: "v2",
        color: "#009900"
      }, {
        title: "v3",
        color: "#000099"
      }, {
        title: "v1+v2",
        color: "#999900"
      }, {
        title: "v2+v3",
        color: "#990099"
      }, {
        title: "v1+v3",
        color: "#009999"
      }, {
        title: "v1+v2+v3",
        color: "#999999"
      }, {
        title: "null",
        color: "#555555"
      }]
  },

  /**
   * let's say we want a small map to be displayed, so let's create it
   */
  "smallMap": {}
} );