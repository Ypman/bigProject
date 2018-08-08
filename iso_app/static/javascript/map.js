function create_map(data) {

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
    "areas": data
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
}