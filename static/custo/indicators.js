      (function load_data_election() {
  $.ajax({
    //url: 'ajax/interactive.html',
    success: function(data) {

    $.getJSON('/background_process_indicators', {
          candidate: "Clinton",
        }, function(res) {
          $("#Democrates").text(res.number_vote_candidate_clinton);
          $("#Republicains").text(res.number_vote_candidate_trump);
        });

    setTimeout(load_data_election, 5000);

    }
  });
})();


(function worker01() {
  $.ajax({
    //url: 'ajax/interactive.html',
    success: function(data) {
      //$('#recall').text("give a response");

      //alert($('.col-md-2 col-sm-4 col-xs-6 tile_stats_count').text())//$('.col-md-2 col-sm-4 col-xs-6 tile_stats_count').text()

    var Votants = parseInt($('#Votants').text())
    var Suffrages = parseFloat($('#Suffrages').text())
    Votants = Votants + 1
    Suffrages = Suffrages - 1
    $('#Votants').text(Votants);
    $('#Suffrages').text(Suffrages);
    setTimeout(worker01, 5000);
    }
  });
})();