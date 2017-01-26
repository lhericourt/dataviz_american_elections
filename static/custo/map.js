$(function load_data_map() {
  $.ajax({
    //url: 'ajax/interactive.html',
    url: '/background_process_map',
    success: function(data) {



      var data_victory = data.data_victory_process;

      $('#world-map-gdp').empty();



      $('#world-map-gdp').replaceWith("<div id='world-map-gdp' class='col-md-8 col-sm-12 col-xs-12' style='height:230px;'></div>");

      var color_trump = "#E74C3C";
      var color_clinton = "#3498DB";
      var colors = {};
      for (var i = 0; i < data_victory.length; i++) {
          var state = data_victory[i][0];
          if(data_victory[i][1] == "Clinton"){
             colors[state] = color_clinton;
          } else {
             colors[state] = color_trump;

          }
        }
      console.log(colors);
      var max = 0,
        min = Number.MAX_VALUE,
        cc,
        startColor = [200, 238, 255],
        endColor = [0, 100, 145],
        hex;

        jQuery('#world-map-gdp').vectorMap({
          backgroundColor: '#FFFFFF',
          borderColor: '#006666',
          borderOpacity: 0.25,
          borderWidth: 1,
          color: '#f4f3f0',
          map: 'usa_en',
          enableZoom: true,
          showTooltip: false,
          selectedColor: null,
          colors: colors,
          onRegionClick: function(element, code, region)
            {
                $('#pie_result').attr("hidden", false);
                $('#title_state').text("Etat : " + region);

                state_clicked.value = code;
                jQuery.ajaxSetup({
                  cache: false
                });
                jQuery.getScript("static/custo/pie.js")
                    .done(function() {
                        /* yay, all good, do something */
                        jQuery.ajaxSetup({
                        cache: false
                      });
                    })
                    .fail(function() {
                        /* boo, fall back to something else */
                });
            }
        });





         setTimeout(load_data_map, 500000);




    }
  });
});
