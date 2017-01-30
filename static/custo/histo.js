$(function load_data_histo() {
  $.ajax({
    url: '/background_process_histo',
    success: function(data) {
        console.log(data);
        var trump_nb_electors = data.trump_nb_electors_process
        var clinton_nb_electors = data.clinton_nb_electors_process

        console.log(trump_nb_electors);

        $('#histo').empty();


        $('#histo').replaceWith("<canvas id='histo' height='15' width='80' style='margin: 15px 10px 10px 0'></canvas>");

        var ctx = document.getElementById("histo");

        var data = {
        labels: ["Trump", "Clinton"],
            datasets: [
                {
                    label: "Nb grands electeurs",

                    backgroundColor: [
                        "#E74C3C",
                        '#3498DB',
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)'
                    ],
                    borderWidth: 1,
                    data: [trump_nb_electors, clinton_nb_electors],
                }
            ]
        };

        var options = {
            animation: false,
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true
                }]
            }
        }

        var myBarChart = new Chart(ctx, {
            type: 'horizontalBar',
            data: data,
            options: options
        });

        setTimeout(load_data_histo, 5000);


    }
  });
});
