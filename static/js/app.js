// JS brings the web app to life

console.log("app.js is running!")

function getInfo() {
    console.log("Getting user input to send to letters.py");

    d3.select("#lines-submit-button").on("change", (event) => {
        var userLines = d3.event.target.value;
        console.log("lines-submit received");
        console.log(`Number of lines: ${userLines}`)
        d3.select("body").append("p").text(userLines)
    })

    d3.select("#case-submit-button").on("change", (event) => {
        var userCase = d3.event.target.value;
        console.log("case-submit received");
        console.log(`Case: ${userCase}`)
        d3.select("body").append("p").text(userCase)
    })

    fetch('/test')
        .then(function (response) {
            return response.json();
        }).then(function (text) {
            console.log('GET response:');
            console.log(text.greeting);
        })
    }
// Once logic is working and data is flowing properly between scripts and 
// webpage, work on styling the page and results.
// When this project is complete, extend the project to include more routes
// to other pages with data analysis visualizations and eventually ML plots.