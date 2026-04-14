document.addEventListener("DOMContentLoaded", function () {

  fetch("https://disease.sh/v3/covid-19/all")
    .then(response => response.json())
    .then(data => {
      document.getElementById("data").innerHTML = `
        <h2>Total Cases: ${data.cases}</h2>
        <h2>Recovered: ${data.recovered}</h2>
        <h2>Deaths: ${data.deaths}</h2>
      `;
    })
    .catch(error => {
      document.getElementById("data").innerHTML = "Error loading data";
      console.log(error);
    });

});
