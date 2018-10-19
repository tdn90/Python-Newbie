# Basic Python Programs
Implementing several simple programs using Python to get familiar with it.

## List of programs:
1. Taylor Series computation example. 
2. Bouncing ball. 
3. Monte Carlo Simulation example.
4. Text document analyzer. 
5. Simple interactive data visualization example.

## Taylor Series Computation
### Description
Compute the value of cosine(a), with a is an angle given in radians, using Taylor Series formula. 
Compare the result computed with the actual value computed by math.cos()

### Run the program
1. Required modules:
    - math.py
    - matplotlib.py
    - TaylorSeries.py
2. Run the program by calling the following in python shell:
    `plotRealCosVersusComputed(low, high, number, taylorN)`
    where:
    - low: lower bound of angle to graph
    - high: upper bound of angle to graph
    - number: number of points to compute and graph (recommended more than 1000 to have a good curve)
    - taylorN: the number of terms in the calculated Taylor Series. 

### Sample output: 
For range -6 to 6:

| Taylor Series with 6 terms  |  Taylor series with 10 terms |
|:----------------:|:--------------:|
|![](../assets/Taylor6.png)  | ![](../assets/Taylor10.png) | 

For range -10 to 10:

| Taylor Series with 10 terms  |  Taylor series with 15 terms |
|:----------------:|:--------------:|
|![](../assets/Taylor10_10.png)  | ![](../assets/Taylor15_10.png)|

## Bouncing Ball:
### Description
Implement a simple interactive bouncing ball program, where the user can choose the start point and velocity (including direction) of the ball. 

### Run the program: 
1. Required modules: 
    - graphics.py
    - BoucingBall.py
2. Run the program by calling the following in python shell:
    `bounce(resolution)`

## Monte Carlo Simulation Example
### Description
A simulation based on random numbers to drive a computational model is called a Monte Carlo Simulation. The simulation program "plays" the computational model over and over again, each time assigning random values to the input variables. It then builds up a probabilistic characterization of the system that it is trying to model. 

This specific program simulates the game of Craps, plots the probabilities of winning and losing. 

Game of Craps rule:
In one game of Craps, a player initially rolls a pair of normal, six-sided dice: 
    - If this initial roll is 7 or 11, the player wins.
    - If this initial roll is 2, 3, or 12, the player loses.
    - With any other value for the initial roll, the player “rolls for point.” That is, the player repeatedly rolls the dice until either a 7 or the value of the initial roll appears. If the value of the initial roll appears before the 7, the player wins. However, if a 7 appears before the value of the initial roll, the player loses.

### Run the program:
1. Required modules: 
    - GameOfCrap.py: responsible for playing one game of Craps. Record the result and turns. 
    - StatsGenerator.py: keep track of the games' statistics.
    - GraphSimResult.py: graph the simulation result.
2. Run the program by typing the following in Python shell:
    `graphResult(#games)`
    where #games is the number of games to simulate (the more the better)

### Sample output: 
Simulation with 10000 games  |  Simulations with 100000 games
:----------------:|:--------------:
![](../assets/MCSimulation10000.png)  | ![](../assets/MCSimulation100000.png)

## Text Document Analyzer:
### Description: 
Implement a simple program that opens and reads one or more files containing normal English text, scans each one and accumulate a list of individual words appearing in that file, and then, when each input file has been scanned, writes to another file the list of unique words appearing in the entire set of input files — in
alphabetical order — along with the number of occurrences of each word.

### Run the program:
1. Required modules:
    - dataProcessor.py
    - outputGenerator.py
    - main.py
2. Run the program straight from the command-line:
    `python main.py [file1] [file2] [...]`
    where:
    [fileN] is the name of the text file provided 
3. Open the ouput text: search for output.txt file in directory.
4. Enjoy!

### Sample output: 
Run with:
    `python main.py test.txt`

Output:

| Test.txt content  | output.txt content |
|:----------------:|:--------------:|
| ![](../assets/TestFile.PNG)|![](../assets/DocAnalyzerOutput.PNG) |

## Simple interactive data visualization example
### Description:
Implement a program that reads a set of public data (about real estate prices, in csv format) from the region around Sacramento, California. Plot the locations of properties of the real estate transactions on a map of the region. 

### Run the program:
1. Required modules: 
    - graphics.py
    - Map.py
    - Filter.py
    - Map.py
    - Plot.py
    - ReportGenerator.py
2. Data files:
    - SacramentoRealEstateTransactions.csv
    - SacramentoMap.gif
3. Run the program from command-line:
   `python main.py`
4. A window with the map of Sacramento Area will pop up. Click anywhere on the map to choose the center point.
5. Click anywhere around the center point to specify the radius of data wanted. 
6. Check out report: search for report.txt
7. Enjoy!

### Sample output:
Data plotted on map  |  Sample report
:----------------:|:--------------:
![](../assets/DataPlot.PNG)  | ![](../assets/RealEstateReport.PNG)

## Author
These programs are implemented by Dung (Kevin) Nguyen, the owner of this repository, with the general instructions provided by Professor Lauer at Worcester Polytechnic Institute.


