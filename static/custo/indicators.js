  (function load_data_election() {
  $.ajax({
    //url: 'ajax/interactive.html',
    //data: JSON.stringify({trump_big_elector_timeline: $("#trump_big_elector_timeline").val(), y: [2.0, 3.0, 1.0]})

    //type: 'POST',
    // Provide correct Content-Type, so that Flask will know how to process it.
    //contentType: 'application/json',
    // Encode your data as JSON.
    //data: JSON.stringify({trump_big_elector_timeline: $("#trump_big_elector_timeline").val(), y: [2.0, 3.0, 1.0]}),
    // This is the type of data you're expecting back from the server.
    //dataType: 'json',
    //url: 'ajax/index.html',

    success: function(data) {

    $.getJSON('/background_process_indicators', {

          //candidate:$("#trump_big_elector_timeline").val()
          //console.log($("#Votants").value);
          //trump_big_elector_timeline: echartLine.getOption().series[0].data,
          // clinton_big_elector_timeline: echartLine.getOption().series[1].data,
          // autres_big_elector_timeline: echartLine.getOption().series[2].data,
        }, function(res) {
          $("#Votants").text(res.nb_of_votes);
          $("#Suffrages").text(res.nb_of_suffrages);
          $("#Abstention").text(res.nb_Abstention);
          $("#Democrates").text(res.nb_of_votes_democrates);
          $("#Republicains").text(res.nb_of_votes_republicains);
          $("#Autres").text(res.nb_of_votes_autres);

          var trump_big_elector_timeline =  $("#trump_big_elector_timeline").val()
          var clinton_big_elector_timeline =  $("#clinton_big_elector_timeline").val()
          var autres_big_elector_timeline =  $("#autres_big_elector_timeline").val()
          var current_date =  $("#current_date").val()

          if($("#trump_big_elector_timeline").val().split(",").slice(-1)[0] != JSON.parse(res.trump_big_elector_timeline)
             || $("#clinton_big_elector_timeline").val().split(",").slice(-1)[0] != JSON.parse(res.clinton_big_elector_timeline)
             || $("#autres_big_elector_timeline").val().split(",").slice(-1)[0] != JSON.parse(res.autres_big_elector_timeline)
             ){

                      trump_big_elector_timeline =  $("#trump_big_elector_timeline").val() + ',' + JSON.parse(res.trump_big_elector_timeline);
                      clinton_big_elector_timeline =  $("#clinton_big_elector_timeline").val() + ',' + JSON.parse(res.clinton_big_elector_timeline);
                      autres_big_elector_timeline =  $("#autres_big_elector_timeline").val() + ',' +  JSON.parse(res.autres_big_elector_timeline);

                      document.getElementById('trump_big_elector_timeline').value = trump_big_elector_timeline
                      document.getElementById('clinton_big_elector_timeline').value = clinton_big_elector_timeline
                      document.getElementById('autres_big_elector_timeline').value = autres_big_elector_timeline

                      // console.log(trump_big_elector_timeline);
                      // console.log(clinton_big_elector_timeline);
                      // console.log(autres_big_elector_timeline);

                      var my_date = new Date()
                      current_date =  $("#current_date").val() + ',' + my_date.getHours()+ ":" +my_date.getMinutes();
                      document.getElementById('current_date').value = current_date
          }


          // console.log(res.clinton_big_elector_timeline);
          // console.log(res.autres_big_elector_timeline);
          //console.log(echartLine.getOption().series[0].data);

echartLine.setOption({
  color: ['#E74C3C','#3498DB','#003300'],
  xAxis: [{
          type: 'category',
          boundaryGap: false,
          data: current_date.split(",")
        }],
        series: [{
          name: 'Trump',
          type: 'line',
          smooth: true,
          itemStyle: {
            normal: {
              areaStyle: {
                type: 'default'
              }
            }
          },

          data: trump_big_elector_timeline.split(",").map(Number)
        }, {
          name: 'Clinton',
          type: 'line',
          smooth: true,
          itemStyle: {
            normal: {
              areaStyle: {
                type: 'default'
              }
            }
          },
          data: clinton_big_elector_timeline.split(",").map(Number)
        }, {
          name: 'Autres',
          type: 'line',
          smooth: true,
          itemStyle: {
            normal: {
              areaStyle: {
                type: 'default'
              }
            }
          },
          data: autres_big_elector_timeline.split(",").map(Number)
        }]
      });
        });

    setTimeout(load_data_election, 5000);

    }
  });
})();




