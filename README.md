# letter-naming-fluency-generator
### [Link to App Deployed on Heroku: https://letter-naming-fluency.herokuapp.com/](https://letter-naming-fluency.herokuapp.com/)
<img src=./Readme-Images/letters.jpg width=1000></img>

### What is letter naming fluency?

In a Letter Name Fluency (LNF) task, a student is given a random list of upper- and lower-case letters and has 1 minute to identify the names of as many letters as possible. Schools often use these scores to determine which students are at risk for reading difficulties.

### Why is letter naming fluency important? 

Letter naming fluency is included in many assessments because it’s a great indicator of risk and a strong predictor of reading success. Letter-naming speed is the single most significant predictor for word reading ability for first-grade students. (Neuhaus & Swank, 2002).  

When children can recognize and name the letters of the alphabet accurately and automatically, they have a foundation for learning the alphabetic principle and learning to read. (Adams, 1994; Ehri, 2005)

Also, students who recognize letters with accuracy and speed have an easier time learning the sounds associated with them. (Adams, 1999)

This app generates lists of letters that educators can use in the classroom for this important assessment.

### Technologies Used
* Python
* JavaScript
* D3
* Flask, Jinja
* JSON
* HTML/CSS
* Bootstrap

### This app is a work in progress.  With that qualification, here are some images of the current state of the webpage.
#### The user enters the number of lines to generate and selects the case they would like from a dropdown menu (Uppercase, Lowercase or Mixed).
#### The user selects 10 lines with Mixed Case:
<img src=./Readme-Images/LNFG_App_1.png width=750></img>

#### The user may then run the program again with different selections, and the output will update accordingly. Here the user has selected 5 lines in Uppercase:
<img src=./Readme-Images/LNFG_App_2.png width=750></img>

#### Once more with 7 lines in Lowercase:
<img src=./Readme-Images/LNFG_App_3.png width=750></img>

#### The user does not have to manually refresh the page each time before running new selections.

### Next Steps:
* Add PDF export functionality.
* Format output on the page to resemble the exportable PDF.
* Deploy the app via Heroku to make it fully functional and available.
