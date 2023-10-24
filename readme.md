# Here is my HackerRank Solutions

The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

### absolutePermutation

  - [Solution](./absolutePermutation.py)
  - ### Explanation: 
>We're aiming to generate an absolute permutation, which is a rearrangement of the integers from 1 to n where each number is at a fixed distance k from its original position. First, we handle special cases: if k is zero, the permutation is simply the sequence from 1 to n. If n is not divisible by 2 * k, no absolute permutation is possible, so we return [-1].
>For valid cases, we create a list ans of size n to store our result. We iterate through the indices of this list. For each index i, we calculate the corresponding value for the absolute permutation. If the index allows, we place the value at the position i + k and fill the current position i with the value i + k + 1. By doing so, we ensure each number is at a distance k from its original position, creating a valid absolute permutation.

### ACMICPCTeam

  - [Solution](./ACMICPCTeam.py)
  ### - Explanation: 
>We go through all possible pairs of teams and calculate how many topics they collectively know. We keep track of the maximum topics known and how many teams share that knowledge. It's like discovering the most knowledgeable teams and counting how many of them are at the top. 

### AlmostSorted

  - [Solution](./AlmostSorted.py)
  ### - Explanation: 
>In this code, we begin by checking if the input array arr is sorted in its current state. We do this by comparing it to a version of itself that has been sorted, which we call is_sorted. If we find that the two arrays are identical, that's a clear sign that our input array is already sorted, and we print 'yes' to confirm this. But if arr is not sorted, we proceed to identify the specific positions where it differs from the sorted version. These differing positions are stored in the diff_indices list. Our next step is to examine these differing indices: if there are exactly two of them, it implies that a simple swap operation can sort the array. In such a case, we print 'yes' and provide the details of the swap operation. However, if there are more than two differing indices, a swap won't work, so we attempt to reverse a segment of the array and check if the result is sorted. If it is, we print 'yes' and specify the reverse operation. If none of these conditions are met, we conclude that it's not possible to sort the array with a minimal number of operations, and we print 'no'.

### angryProfessor

  - [Solution](./angryProfessor.py)
  ### - Explanation: 
>To determine whether the professor is angry or not, We count how many students arrive on time by looking at their arrival times. If the number of on-time students is less than the "k", the professor is angry, and we return "YES." Otherwise, if enough students are on time, we return "NO."

### AppendAndDelete.py

  - [Solution](./AppendAndDelete.py)
  ### - Explanation: 
>First, I calculate total operations needed for deletion and appending. Then, to determine if it's possible within the given limit "k", I check if there are enough actions to cover the total changes. If the remaining actions after all changes are even, it returns "Yes." Additionally, if there are more actions available than the combined length of both strings, it also returns "Yes." Otherwise, it returns "No." It's all about ensuring I have the right moves to transform one string into another without interfering the prescribed limit.


### AppleAndOrange

  - [Solution](./AppleAndOrange.py)
  ### - Explanation: 
>In this code, First the values are read for the house and tree positions (s, t), the apple and orange tree positions (a, b), the number of apples and oranges (m, n), and the lists of apple and orange distances. Then, we count how many apples and oranges hit the house. If the distance from the tree (a or b) plus the fruit's distance (d) is within the range of the house (between s and t), we add 1 to the count. Finally, we get how many apples and oranges made it to the house

### AVeryBigSum

  - [Solution](./AVeryBigSum.py)
  ### - Explanation: 
>This code calculates the sum of all the numbers in a given list (ar). It initializes a variable total_sum to 0, then iterates through the list, adding each number to total_sum. Finally, it returns the total sum of all the numbers in the input list.

### beautifulDays

  - [Solution](./beautifulDays.py)
  ### - Explanation: 
>To count the number of "beautiful days" within a given range. First, we iterate through the range of days from "i" to "j." For each day, reverse its digits and check if the absolute difference between the day and its reverse is divisible by "k." If it is divisible, then it is a beautiful day and increment the count. At last, I return the count of beautiful days. It's all about identifying and counting those special days when the difference between a day and its reverse is a multiple of "k".

### BeautifulTriplets

  - [Solution](./BeautifulTriplets.py)
  ### - Explanation: 
>I start by converting the array into a set for faster lookups. Then, I iterate over each element in the array. For each element, I check if the element incremented by 'd' and the element incremented by '2d' are both present in the set. If they are, it means I've found a beautiful triplet, so I increment my count. This approach allows me to find all beautiful triplets in the array with just a single pass, significantly improving the efficiency of the algorithm.

### betweenTwoSets

  - [Solution](./betweenTwoSets.py)
  ### - Explanation: 
>kla kli kli klu 

### BiggerIsGreater

  - [Solution](./BiggerIsGreater.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### BillDivision

  - [Solution](./BillDivision.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### BirthdayCakeCandles

  - [Solution](./BirthdayCakeCandles.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### BreakingTheRecords

  - [Solution](./BreakingTheRecords.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### ChocolateFeast

  - [Solution](./ChocolateFeast.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### circularArrayRotation

  - [Solution](./circularArrayRotation.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### climbingLeaderboard

  - [Solution](./climbingLeaderboard.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### CompareTheTriplets

  - [Solution](./CompareTheTriplets.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### cutTheSticks

  - [Solution](./cutTheSticks.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### designerPdfViewer

  - [Solution](./designerPdfViewer.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### DivisibleSumPairs

  - [Solution](./DivisibleSumPairs.py)
  ### - Explanation: 
>kla kli kli klu l=klu

### Encryption
  - [Problem Statement](#https://www.hackerrank.com/challenges/encryption)
  - [Solution](./Encryption.py)
  - ### Explanation: 
>We're encrypting a message by arranging its characters into a grid and then reading the characters column by column. We remove spaces from the message and calculate the grid's dimensions based on the square root of the message length, visualizing it as a rectangular layout. We then construct the encrypted message by iterating through the columns, collecting characters from the original message and separating words with spaces. This method efficiently transforms the message into an encrypted format for secure communication.

### EqualizeTheArray

  - [Solution](./EqualizeTheArray.py)
  ### - Explanation: 
>In this code, I'm finding the minimum number of deletions needed to make all elements in an array equal. First, I create a dictionary to count the occurrences of each element, and then identify the most frequently occurring element. The deletions required will be the total number of elements minus the count of the most frequent element. This approach efficiently helps me determine the minimal deletions to equalize the array. It's like figuring out how many elements I need to remove to have them all the same

### extraLongFactorials

  - [Solution](./extraLongFactorials.py)
  ### - Explanation: 
>I'm calculating and printing the factorial of a given number "n" I start with a value of 1 and then multiply it by each integer from 1 to "n" 


### FairRations

  - [Solution](./FairRations.py)
  ### - Explanation: 
>First, I find all the number of people needing an extra loaf (those with odd bread counts). If the count of such people is odd, it's impossible to distribute fairly, so I return "NO." If there's an even count of needy people, I calculate the additional loaves required by looking at the gaps between their number. These gaps represent the number of extra loaves needed for each pair of adjacent needy people. Multiplying this count by 2 ensures a fair distribution. This approach guarantees fairness and provides the required additional loaves efficiently.

### FindDigits

  - [Solution](./FindDigits.py)
  ### - Explanation: 
>In this function, I'm counting how many digits in a number evenly divide the number itself. I start with a count of zero and loop through each digit in the number. For each digit, I check if it's not zero and if dividing the number by the digit leaves no remainder. If both conditions are met, I increment the count. 

### flatlandSpaceStations

  - [Solution](./flatlandSpaceStations.py)
  ### - Explanation: 
>We begin by sorting the space station locations. We then calculate the maximum distance by considering the extreme cases - the distance from the first city to the first space station and from the last space station to the last city. These distances represent the initial maximums. Moving through the sorted space station locations, we calculate the maximum distance between adjacent stations and update our maximum if we find a longer distance. This method ensures an efficient exploration of the cityscape, identifying the farthest a city can be from the closest space station. The final value in the max_distance variable gives us this answer.

### formingMagicSquare

  - [Solution](./formingMagicSquare.py)
  ### - Explanation: 
>I have pre-defined magic squares and I compare the given square with each of them. For each comparison, I calculate the cost by finding the absolute differences between corresponding elements. The minimum cost among all magic squares is what I should be getting. It's like determining the most cost-effective way to convert the given square into a magic square

### gradingStudents

  - [Solution](./gradingStudents.py)
  ### - Explanation: 
>In this code, I'm simplifying grades for students. For each grade, I check if it's less than 38; if it is, I keep it unchanged. If it's 38 or higher, I find the next multiple of 5 and see if the difference is less than 3. If it is, I round up to that multiple of 5; otherwise, I keep the grade as it is. 

### HaloweenSale

  - [Solution](./HaloweenSale.py)
  ### - Explanation: 
>I start by setting the count of games I can buy to zero and the current price of the game to 'p'. Then, I enter a loop that continues as long as my remaining money 's' is greater than or equal to the current price. In each iteration of the loop, I increment my game count by one, subtract the current price from my money, and update the current price to be either its value minus 'd' or 'm', whichever is greater. This ensures that the price decreases by 'd' after each purchase until it reaches 'm'. The loop ends when I don't have enough money to buy a game at the current price. Finally, I return the count of games I can buy.

### jumpingOnClouds

  - [Solution](./jumpingOnClouds.py)
  ### - Explanation: 
>In this code, we imagine simulating a game where I jump on clouds. I start with 100 units of energy. I iterate through clouds by jumping k steps at a time, looping back to the start if needed. For each jump, I decrease my energy by 1. If I land on a thundercloud (indicated by 1), I lose 2 energy. I repeat until I return to the initial cloud (cloud 0). The final energy level is my output, representing my energy after these jumps.


### LibraryFine

  - [Solution](./LibraryFine.py)
  ### - Explanation: 
>I'm calculating the fine for a library book return. I compare the return date (d1, m1, y1) with the due date (d2, m2, y2). If the return is on or before the due date, there's no fine (return 0). If the return is within the same month, I calculate the fine based on the number of days late. If the return is in a later month of the same year, I calculate the fine based on the number of months late. If the return is in a later year, there's a fine of 10000.

### LisasWorkbook

  - [Solution](./LisasWorkbook.py)
  ### - Explanation: 
>We begin with a count of special_problems set to 0 and initialize the page number to 1. For each chapter's problems in the arr, we iterate through the problems using a loop. We check if the problem number matches the current page number, and if so, we increment the special_problems count. Additionally, we keep track of the page number, ensuring it advances when we reach either the end of a chapter or after k problems, making it easy to count special problems per page. Finally, we return the total count of special problems found.

### MigratoryBirds

  - [Solution](./MigratoryBirds.py)
  ### - Explanation: 
>To find the most frequently sighted bird species from a list. Using a Counter, we tally the occurrences of each bird. Then find the maximum count among the bird species. If there are multiple birds with the highest count, we select the one with the lowest ID, which is the most frequent. This approach finds and returns the ID of the most commonly spotted bird.

### MinimumDistances

  - [Solution](./MinimumDistances.py)
  ### - Explanation: 
>I start by initializing the minimum distance as infinity and creating an empty dictionary to store the last position of each element in the array. Then, I iterate over the array. For each element, I check if it’s already in the dictionary, which means I’ve seen it before. If it is, I calculate the distance between its current position and the last position where I saw it, and update the minimum distance if this new distance is smaller. Whether or not the element was in the dictionary, I update its last seen position in the dictionary to be its current position. After going through all elements, if the minimum distance is still infinity, it means I didn’t find any pair of identical elements, so I return -1. Otherwise, I return the minimum distance.


### MinMaxSum

  - [Solution](./MinMaxSum.py)
  ### - Explanation: 
>First, I sort the numbers in ascending order. Then, I find the sum of the smallest four numbers for the minimum sum and the sum of the largest four numbers for the maximum sum. Finally, I print these two sums.

### ModifiedKaprekarNumbers

  - [Solution](./ModifiedKaprekarNumbers.py)
  ### - Explanation: 
>I start by creating an empty list to store the Kaprekar numbers. Then, I iterate over each number in the range from ‘p’ to ‘q’ inclusive. For each number, I square it and convert both the number and its square into strings. I then split the string representation of the square into two parts: a right part consisting of the last ‘d’ digits (where ‘d’ is the number of digits in the original number) and a left part consisting of the remaining digits. If there are no remaining digits, I consider the left part to be zero. I then check if the sum of the right and left parts equals the original number. If it does, I append the number to my list of Kaprekar numbers. After checking all numbers in the range, if I have found any Kaprekar numbers, I print them out. Otherwise, I print “INVALID RANGE”.

### NonDivisibleSubset

  - [Solution](./NonDivisibleSubset.py)
  ### - Explanation: 
>To identify a non-divisible subset within a given list. We maintain an array to count the remainders of elements when divided by "k" Then, we calculate the result by considering the minimum of remainders that are evenly divisible by "k" and adding the maximum count for remainders that have complementary pairs. If "k" is even, add 1 to the result. This helps us find the largest non-divisible subset within the given list. It's about determining which elements can't be divided evenly by "k" and forming the largest possible subset from them.

### NumberLineJumps

  - [Solution](./NumberLineJumps.py)
  ### - Explanation: 
>In this code, I'm helping two kangaroos, each starting at a different position and jumping with a specific distance. I want to know if they'll ever land on the same spot. First, I check if they have the same jumping distance; if they do, I check if they're already at the same position, and if they are, It will return "YES," indicating they'll meet. If their jumping distances are different, I calculate whether the relative distance between them and the relative speed allows them to meet at some point. If the claculations are correct, it will return "YES" otherwise "NO."

### organizingContainersofBalls

  - [Solution](./organizingContainersofBalls.py)
  ### - Explanation: 
>In this function, I'm determining whether it's possible to organize the balls within the containers in a specific way. For each container, I calculate the total number of balls and for each type of ball, I calculate the total number in all containers. By sorting these sums, I can compare whether the total number of balls in each container matches the total number of each type of ball across all containers. If the sorted sums match, it's possible to organize the balls as required, and the function returns "Possible." Otherwise, it returns "Impossible." This approach checks the distribution of balls within containers to determine if a specific organization is achievable.

### PickingNumbers

  - [Solution](./PickingNumbers.py)
  ### - Explanation: 
>In this function, we're finding the longest subarray where the absolute difference between any two elements is at most 1. We create a dictionary to count the occurrences of each number in the array. Then, we iterate through the dictionary and check for the maximum length by considering the count of the current number and the count of the number one greater. This helps us find the maximum possible length of such a subarray

### PlusMinus

  - [Solution](./PlusMinus.py)
  ### - Explanation: 
>I want to understand the proportions of positive, negative, and zero values. So, I'm counting how many numbers fall into each of these categories. Then, I calculate and print the fractions of positive, negative, and zero values relative to the total number of elements

### QueensAttack2

  - [Solution](./QueensAttack2.py)
  ### - Explanation: 
>For calculating the number of squares a queen can attack on an n×n chessboard. First define the possible directions a queen can move: horizontally, vertically, diagonally. Then,  use these directions to iterate through the board, considering obstacles. For each direction, move the queen until she encounters an obstacle, reaching the boundary, or completes the diagonal. Then count the squares she can attack in each direction and return the total. 
