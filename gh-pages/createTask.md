{% include navigation.html %}

# Create Task

## Requirements:
* Input and an Output
* At least one list
* At least one procedure
* for loop 
* At least one algorithm

## Video
We will submit a video that is:
* Less than 1 minute 
* With no collaboration
* No voice, only text captions
* Less than 30 MB in file size
* .mp4, .wmv, .avi, or .mov format

## Idea: Farming Simulator

Input: User adds seeds to virtual garden. User can also sell crops and make money to use other features.

Output: Seeds grow into crops. 2 Crops per planted seed.

List: Crop storage is in list format.

Procedure: The user adds seeds to virtual garden which take time to grow and get appended into list and displayed as storage.

Iteration: A feature that will repeatedly spit out crops at a rapid speed for a monetary cost.

## Written Response
3 a. Provide a written response that does all three of the following:
Approx. 150 words (for all subparts of 3a combined)

**i. Describes the overall purpose of the program**   
The program will allow the user to plant seeds which grow into crops. These can be sold for money, which can be used for more efficient crop gaining methods.

**ii. Describes what functionality of the program is demonstrated in
the video**   
The video demonstrates all of the above.

**iii. Describes the input and output of the program demonstrated in
the video**   
The input is the user planting seeds, selling crops, and using "super crop growth." Output is the crops growing, the money gained from sales, and the crops gained from super crop growth.

3 b. Capture and paste two program code segments you developed during
the administration of this task that contain a list (or other collection
type) being used to manage complexity in your program.
Approx. 200 words (for all subparts of 3b combined, exclusive of
program code)

**i. The first program code segment must show how data have been
stored in the list.**   
```
cropList = [0,0,0,0]

function plantCorn(){
    let cornGrowth = cornGrowTime
    let downloadTimer = setInterval(function(){
        if(cornGrowth <= 0){
            clearInterval(downloadTimer);
            document.getElementById("cornButton").style.pointerEvents = ""
            document.getElementById("cornButton").innerHTML = "Plant Corn";
            cropList[1] += 2
            document.getElementById("cornCount").innerHTML = "Corn: " + cropList[1]
        } else {
            document.getElementById("cornButton").style.pointerEvents = "none"
            document.getElementById("cornButton").innerHTML = cornGrowth + " seconds remaining";
        }
        cornGrowth -= 1;
    }, 1000);}
 ```

**ii. The second program code segment must show the data in the
same list being used, such as creating new data from the existing
data or accessing multiple elements in the list, as part of fulfilling
the program’s purpose.**   
```
let cornCounter = 0;
function cornSuperGrow(){
    setTimeout(function() {
        if(window.superGrowCount > 0){
            cropList[1] += 2
            document.getElementById("cornCount").innerHTML = "Corn: " + cropList[1]
            cornCounter++
            if(cornCounter <= window.superGrowCount){
                cornSuperGrow();
            } else{
                cornCounter = 0
            }
        }
    },50)
}

let carrotCounter = 0
function carrotSuperGrow(){
    setTimeout(function() {
        if(window.superGrowCount > 0){
            cropList[2] += 2
            document.getElementById("carrotCount").innerHTML = "Carrot: " + cropList[2]
            carrotCounter++
            if(carrotCounter <= window.superGrowCount){
                carrotSuperGrow();
            } else{
                carrotCounter = 0
            }
        }
    },50)
}
```

**iii. Identifies the name of the list being used in this response**   
The list is called 'cropList'

**iv. Describes what the data contained in the list represent in your
program**   
Each index stores the count of a certain crop. In order, the list represents the count of: wheat, corn, carrots, and tomatoes.

**v. Explains how the selected list manages complexity in your program
code by explaining why your program code could not be written, or
how it would be written differently, if you did not use the list**   
Instead of keeping track of 4 global variables, this reduces it to 1. I could have used 4 separate variables to store data, but this was a simpler method for me.

3 c. Capture and paste two program code segments you developed during
the administration of this task that contain a student-developed
procedure that implements an algorithm used in your program and a
call to that procedure.
Approx. 200 words (for all subparts of 3c combined, exclusive of
program code)

**i. The first program code segment must be a student-developed
procedure that:
□ Defines the procedure’s name and return type (if necessary)
□ Contains and uses one or more parameters that have an effect
on the functionality of the procedure
□ Implements an algorithm that includes sequencing, selection,
and iteration**   

**ii. The second program code segment must show where your
student-developed procedure is being called in your program.
Then, provide a written response that does both of the following:**

**iii. Describes in general what the identified procedure does and how it
contributes to the overall functionality of the program**   

**iv. Explains in detailed steps how the algorithm implemented in the
identified procedure works. Your explanation**   
