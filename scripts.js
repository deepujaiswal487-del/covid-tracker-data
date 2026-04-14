fetch("https://disease.sh/v3/covid-19/all")
  .then(res => res.json())
  .then(data => {
    document.body.innerHTML += `
      <h2>Total Cases: ${data.cases}</h2>
      <h2>Recovered: ${data.recovered}</h2>
      <h2>Deaths: ${data.deaths}</h2>
    `;
  })
  .catch(err => console.log(err));
