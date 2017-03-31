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
        "Johnson":
        {
            nom : "Johnson",
            nb_votes : 0,
            color_pie : "#9B59B6"
        },
        "Stein":
        {
            nom : "Stein",
            nb_votes : 0,
            color_pie : "#1ABB9C"
        },
        "Castle":
        {
            nom : "Castle",
            nb_votes : 0,
            color_pie : "#9CC2CB"
        },
        "McMullin":
        {
            nom : "Autre",
            nb_votes : 0,
            color_pie : "#34495E"
        },
        "Autre":
        {
            nom : "Autre",
            nb_votes : 0,
            color_pie : "#34495E"
        },
         "Blanc":
        {
            nom : "Blanc",
            nb_votes : 0,
            color_pie : "#DDDEA4"
        }
      };

      for (var i = 0; i < state_clicked.nb_votes.length; i++) {
            if(state_clicked.nb_votes[i][0] == state_clicked.value){
                candidats[state_clicked.nb_votes[i][1]].nb_votes = state_clicked.nb_votes[i][2];

            }
        }

      $(document).ready(function(){
        $('#result_clinton').text(candidats["Clinton"].nb_votes);
        $('#result_trump').text(candidats["Trump"].nb_votes);
        $('#result_johnson').text(candidats["Johnson"].nb_votes);
        $('#result_stein').text(candidats["Stein"].nb_votes);
        $('#result_castle').text(candidats["Castle"].nb_votes);
        $('#result_mcmullin').text(candidats["McMullin"].nb_votes);
        $('#result_autre').text(candidats["Autre"].nb_votes);
        $('#result_blanc').text(candidats["Blanc"].nb_votes);

        if(candidats["Clinton"].nb_votes == 0){
            $('#clinton').attr("hidden", true);
        } else {
            $('#clinton').attr("hidden", false);
        }

        if(candidats["Trump"].nb_votes == 0){
            $('#trump').attr("hidden", true);
        } else {
            $('#trump').attr("hidden", false);
        }

        if(candidats["Johnson"].nb_votes == 0){
            $('#johnson').attr("hidden", true);
        } else {
            $('#johnson').attr("hidden", false);
        }

        if(candidats["Stein"].nb_votes == 0){
            $('#stein').attr("hidden", true);
        } else {
            $('#stein').attr("hidden", false);
        }

        if(candidats["Castle"].nb_votes == 0){
            $('#castle').attr("hidden", true);
        } else {
            $('#castle').attr("hidden", false);
        }

        if(candidats["Autre"].nb_votes == 0){
            $('#autre').attr("hidden", true);
        } else {
            $('#autre').attr("hidden", false);
        }

        if(candidats["Blanc"].nb_votes == 0){
            $('#blanc').attr("hidden", true);
        } else {
            $('#blanc').attr("hidden", false);
        }

        if(candidats["McMullin"].nb_votes == 0){
            $('#mcmullin').attr("hidden", true);
        } else {
            $('#mcmullin').attr("hidden", false);
        }


        var options = {
          legend: false,
          responsive: false
        };

        $('#canvas1').empty();


        new Chart(document.getElementById("canvas1"), {
          type: 'doughnut',
          tooltipFillColor: "rgba(51, 51, 51, 0.55)",
          data: {
            labels: [candidats["Clinton"].nom, candidats["Trump"].nom, candidats["Johnson"].nom, candidats["Stein"].nom, candidats["Castle"].nom, candidats["McMullin"].nom, candidats["Autre"].nom, candidats["Blanc"].nom],
            datasets: [{
              data: [candidats["Clinton"].nb_votes, candidats["Trump"].nb_votes, candidats["Johnson"].nb_votes, candidats["Stein"].nb_votes, candidats["Castle"].nb_votes, candidats["McMullin"].nb_votes, candidats["Autre"].nb_votes, candidats["Blanc"].nb_votes],
              backgroundColor: [candidats["Clinton"].color_pie, candidats["Trump"].color_pie, candidats["Johnson"].color_pie, candidats["Stein"].color_pie, candidats["Castle"].color_pie, candidats["McMullin"].color_pie, candidats["Autre"].color_pie, candidats["Blanc"].color_pie],
            }]
          },
          options: options
        });
      });
     });
