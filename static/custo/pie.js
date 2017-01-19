$(document).ready(function() {
      var candidats = {
        "Clinton":
        {
            nom : "Clinton",
            nb_votes : 0,
            color_pie : "#3498DB"
         },
        "Trump":
        {
            nom : "Trump",
            nb_votes : 0,
            color_pie : "#E74C3C"
        },
        "Dupont":
        {
            nom : "Dupont",
            nb_votes : 0,
            color_pie : "#9B59B6"
        },
      };

      for (var i = 0; i < nb_votes.length; i++) {
            if(nb_votes[i][0] == state_clicked.value){
                candidats[nb_votes[i][1]].nb_votes = nb_votes[i][2];
            }
        }

      $(document).ready(function(){

        $('#result_clinton').text(candidats["Clinton"].nb_votes);
        $('#result_trump').text(candidats["Trump"].nb_votes);
        $('#result_dupont').text(candidats["Dupont"].nb_votes);

        var options = {
          legend: false,
          responsive: false
        };

        $('#canvas1').empty();

        new Chart(document.getElementById("canvas1"), {
          type: 'doughnut',
          tooltipFillColor: "rgba(51, 51, 51, 0.55)",
          data: {
            labels: [candidats["Clinton"].nom, candidats["Trump"].nom, candidats["Dupont"].nom],
            datasets: [{
              data: [candidats["Clinton"].nb_votes, candidats["Trump"].nb_votes, candidats["Dupont"].nb_votes],
              backgroundColor: [candidats["Clinton"].color_pie, candidats["Trump"].color_pie, candidats["Dupont"].color_pie],
              //hoverBackgroundColor: [candidats["Clinton"].color_hover, candidats["Trump"].color_hover, candidats["Dupont"].color_hover]
            }]
          },
          options: options
        });
      });
     });