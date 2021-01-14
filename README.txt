Written by Alan Tu
14 January 2021
Saga, Elevator Control Exercise

INSTRUCTIONS FOR RUNNING

In a terminal command line, enter this folder and then type:

python elevator.py [test-file] [num-floors]

where [test-file] should be replaced with the name of the desired test file (e.g. ritz.txt)
and [num-floors] should be replaced with however many floors the hotel has (e.g. 10).

TEST FILES

I include the following test files: ritz.txt, ritz2.txt, sheraton.txt, marriott.txt. They should be run with 10 or more floors.

Each test file looks something like the following:

1-2, 4-3

3-5
10-6, 5-2, 5-7

This is an ordered list of requests. The syntax X-Y means that a person waiting on Floor X has requested the elevator and would like to reach Floor Y.

Requests can only be made at discrete "time steps": at every "exchange" (i.e. every time the elevator doors open), or whenever the elevator is empty. Multiple people can make requests at each time step. Requests on the same line are made simultaneously and are separated by commas as shown.

A blank line denotes a time step in which no requests are made.

By default the elevator starts on Floor 1.

TEST OUTPUT

Running the program with a test file will print a list of floors on which exchanges were made, with details regarding how many people were picked up and dropped off. This elevator will keep moving up (or down) until there are no more requested floors above (below) the current floor; then it will change direction. The correctness of the tests can be quickly verified by hand.

QUESTIONS

3.5 hrs.

I would work on the user interface to make it easier to understand (perhaps make it interactive and real-time, like a real elevator). I would also try to think of a way to use fewer conditionals/cleaner code for the edge cases. I would also add error-catching functionalities, in case the test file is nonsensical, or the user inputs a negative number of floors, etc.

I appreciated the freedom I had to implement this project. However, I struggled to figure out how simple or complex to make my program. Thus I decided to write code until the scope of my initial idea was realized, which took me longer than the suggested 2 hrs. It was fun though!