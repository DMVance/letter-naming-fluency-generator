console.log("app.js is running!")

function getData() {
    console.log("Request has been made to get user input to send to letters.py");

    var userLines = d3.select("#lines-submit-button").property("value");
    // console.log("lines-submit received");
    console.log(`Number of lines: ${userLines}`)

    var userCase = d3.select("#case-submit-button").property("value")
    console.log(`Case: ${userCase}`)
    d3.select("body").append("p").text(userCase)

    let data = [userLines, userCase]
    console.log(`The data array is: ${data}`)
    
    // let table = d3.select("#letters-table").append("p").text(userLines)
    // table.selectAll("tr").remove() // remove all existing rows to reset, preventing posting data multiple times
    // let table = d3.select("#letters-table").append("p").text(userCase)
    // table.selectAll("tr").remove()

    fetch(`${window.origin}/test`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(data),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
            })
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(function (error) {
            console.log("Fetch error: " + error)
        })
}

// Once logic is working and data is flowing properly between scripts and 
// webpage, work on styling the page and results.
// When this project is complete, extend the project to include more routes
// to other pages with data analysis visualizations and eventually ML plots.