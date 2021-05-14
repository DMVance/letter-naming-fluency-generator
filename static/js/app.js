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
    // console.log('app.js, ', jsonArrData)
    console.log('app.js, jsonArrData is a string: ', typeof jsonArrData === 'string')
        
    // let table = d3.select("#letters-table").append("p").text(userLines)
    // table.selectAll("tr").remove() // remove all existing rows to reset, preventing posting data multiple times
    // let table = d3.select("#letters-table").append("p").text(userCase)
    // table.selectAll("tr").remove()

    fetch(`${window.origin}/test`, {
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
        console.log("app.js, Success! The data: ", data);
        // d3.select(".output").append("p").text(data.json())
        data.json().then(responseJson => {  // .json() 
            console.log(responseJson)
            // console.log(typeof responseJson)
            d3.select(".output").selectAll("p").remove()
            responseJson.forEach(e => {
                d3.select(".output").append("p").text(Object.values(e).join(" "))
            });
            // Plotly.newPlot("output", responseJson)  // only plotting the object, not parsed data
            })
    })
    .catch((error) => {
        console.error("app.js, Aggravating Error: ", error); // data is not showing on "/test"
    });

}

// Once logic is working and data is flowing properly between scripts and 
// webpage, work on styling the page and results.
// When this project is complete, extend the project to include more routes
// to other pages with data analysis visualizations and eventually ML plots.