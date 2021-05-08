console.log("app.js is running!")

function getData() {

    let userLines = d3.select("#lines-submit-button").property("value");
    console.log(`app.js, Number of lines: ${userLines}`)

    let userCase = d3.select("#case-submit-button").property("value")
    console.log(`app.js, Case: ${userCase}`)
    // d3.select("body").append("p").text(userCase)

    var data = [userLines, userCase]
    console.log(`app.js, The data array is: ${data}`)

    jsonArrData = JSON.stringify(data)
    console.log('app.js, ', jsonArrData)
    console.log('app.js, ', typeof jsonArrData === 'string')
        
    // let table = d3.select("#letters-table").append("p").text(userLines)
    // table.selectAll("tr").remove() // remove all existing rows to reset, preventing posting data multiple times
    // let table = d3.select("#letters-table").append("p").text(userCase)
    // table.selectAll("tr").remove()

    fetch(`${window.origin}/test`, {
    // fetch("http://127.0.0.1:5000", {
        method: "POST",
        // mode: "cors",
        credentials: "include",
        headers: new Headers({
            "content-type": "application/json"
        }),
        body: JSON.stringify(data),
        cache: "no-cache",
    })
    // .then(response => response.json()) # This was part of the problem!! response is not json serializable!
    .then(data => {
        console.log("app.js, Success, the data: ", data);
        data.json().then(function (responseJson) {
            console.log(responseJson)
            // d3.select(".output").append("p").text(responseJson)
            Plotly.newPlot("output", responseJson)  // only plotting the object, not parsed data
            })
    })
    .catch((error) => {
        console.error("app.js, Aggravating Error: ", error); // data was not making it to "/test"
    });

    // fetch(`${window.origin}/test`)
    // .then(response => response.json())
    // .then(data => console.log(data));

    // d3.select(".output").append("p").text(data)

}

// Once logic is working and data is flowing properly between scripts and 
// webpage, work on styling the page and results.
// When this project is complete, extend the project to include more routes
// to other pages with data analysis visualizations and eventually ML plots.