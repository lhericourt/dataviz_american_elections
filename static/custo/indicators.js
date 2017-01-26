  (function load_data_election() {
  $.ajax({
    //url: 'ajax/interactive.html',
    success: function(data) {

    $.getJSON('/background_process_indicators', {
          candidate: "Clinton",
        }, function(res) {
          $("#Votants").text(res.nb_of_votes);
          $("#Suffrages").text(res.nb_of_suffrages);
          $("#Abstention").text(res.nb_Abstention);
          $("#Democrates").text(res.nb_of_votes_democrates);
          $("#Republicains").text(res.nb_of_votes_republicains);
          $("#Autres").text(res.nb_of_votes_autres);
        });

    setTimeout(load_data_election, 5000);

    }
  });
})();


