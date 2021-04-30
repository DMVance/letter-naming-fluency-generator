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
    console.log(data)
    
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
        .then(function (response) {
            return response.json();
        })
        .then(function (response) {
            if (response.status !== 200) {
                console.log(`Houston, we have a Lines problem. Status code: ${response.status}`);
                return;
            }
        })
        .then(function (text) {
            console.log('GET response:');
            console.log(text.greeting);
        })
    }

// function getLines() {
//     console.log("Request has been made to get user input to send to letters.py");
//     var userLines = d3.select("#lines-submit-button").property("value");
//     // console.log("lines-submit received");
//     console.log(`Number of lines: ${userLines}`)
    
//     let table = d3.select("#letters-table").append("p").text(userLines)
//     table.selectAll("tr").remove() // remove all existing rows to reset, preventing posting data multiple times
    
//     fetch(`${window.origin}/test`, {
//         method: "POST",
//         credentials: "include",
//         body: JSON.stringify(userLines),
//         cache: "no-cache",
//         headers: new Headers({
//             "content-type": "application/json"
//         })
//     })
//         .then(function (response) {
//             return response.json();
//         })
//         .then(function (response) {
//             if (response.status !== 200) {
//                 console.log(`Houston, we have a Lines problem. Status code: ${response.status}`);
//                 return;
//             }
//         })
//         .then(function (text) {
//             console.log('GET response:');
//             console.log(text.greeting);
//         })
//     }

// function getCase() {
//     console.log("Getting user input to send to letters.py");
//     var userCase = d3.select("#case-submit-button").property("value")
//     console.log(`Case: ${userCase}`)
//     d3.select("body").append("p").text(userCase)

//     fetch(`${window.origin}/test`, {
//         method: "POST",
//         credentials: "include",
//         body: JSON.stringify(userCase),
//         cache: "no-cache",
//         headers: new Headers({
//             "content-type": "application/json"
//         })
//     })
//         .then(function (response) {
//             return response.json();
//         })
//         .then(function (response) {
//             if (response.status !== 200) {
//                 console.log(`Houston, we have a Case problem. Status code: ${response.status}`);
//                 return;
//             }
//         })
//         .then(function (text) {
//             console.log('GET response:');
//             console.log(text.greeting);
//         })
//     }

    // fetch(`${window.origin}/test`, {
    //     method: "POST",
    //     credentials: "include",
    //     body: JSON.stringify(userLines),
    //     cache: "no-cache",
    //     headers: new Headers({
    //         "content-type": "application/json"
    //     })
    // })
    //     .then(function (response) {
    //         return response.json();
    //     })
    //     .then(function (response) {
    //         if (response.status !== 200) {
    //             console.log(`Houston, we have a problem.Status code: ${response.status}`);
    //             return;
    //         }
    //     })
    //     .then(function (text) {
    //         console.log('GET response:');
    //         console.log(text.greeting);
    //     })

// Once logic is working and data is flowing properly between scripts and 
// webpage, work on styling the page and results.
// When this project is complete, extend the project to include more routes
// to other pages with data analysis visualizations and eventually ML plots.