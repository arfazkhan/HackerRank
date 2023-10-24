# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

### absolutePermutation

  - [Solution](./absolutePermutation.py)
  ### - Explanation: 
>We're aiming to generate an absolute permutation, which is a rearrangement of the integers from 1 to n where each number is at a fixed distance k from its original position. First, we handle special cases: if k is zero, the permutation is simply the sequence from 1 to n. If n is not divisible by 2 * k, no absolute permutation is possible, so we return [-1].
>For valid cases, we create a list ans of size n to store our result. We iterate through the indices of this list. For each index i, we calculate the corresponding value for the absolute permutation. If the index allows, we place the value at the position i + k and fill the current position i with the value i + k + 1. By doing so, we ensure each number is at a distance k from its original position, creating a valid absolute permutation.

### ACMICPCTeam

  - [Solution](./ACMICPCTeam.py)
  ### - Explanation: 
        We go through all possible pairs of teams and calculate how many topics they collectively know. We keep track of the maximum topics known and how many teams share that knowledge. It's like discovering the most knowledgeable teams and counting how many of them are at the top. 

### AlmostSorted

  - [Solution](./AlmostSorted.py)
  ### - Explanation: 
        In this code, we begin by checking if the input array arr is sorted in its current state. We do this by comparing it to a version of itself that has been sorted, which we call is_sorted. If we find that the two arrays are identical, that's a clear sign that our input array is already sorted, and we print 'yes' to confirm this. 
        
        But if arr is not sorted, we proceed to identify the specific positions where it differs from the sorted version. These differing positions are stored in the diff_indices list. Our next step is to examine these differing indices: if there are exactly two of them, it implies that a simple swap operation can sort the array. In such a case, we print 'yes' and provide the details of the swap operation. However, if there are more than two differing indices, a swap won't work, so we attempt to reverse a segment of the array and check if the result is sorted. If it is, we print 'yes' and specify the reverse operation. If none of these conditions are met, we conclude that it's not possible to sort the array with a minimal number of operations, and we print 'no'.

### angryProfessor

  - [Solution](./angryProfessor.py)
  ### - Explanation: 
        To determine whether the professor is angry or not, We count how many students arrive on time by looking at their arrival times. If the number of on-time students is less than the "k", the professor is angry, and we return "YES." Otherwise, if enough students are on time, we return "NO."

### AppendAndDelete.py

  - [Solution](./AppendAndDelete.py)
  ### - Explanation: 
        First, I calculate total operations needed for deletion and appending. Then, to determine if it's possible within the given limit "k", I check if there are enough actions to cover the total changes. If the remaining actions after all changes are even, it returns "Yes." Additionally, if there are more actions available than the combined length of both strings, it also returns "Yes." Otherwise, it returns "No." It's all about ensuring I have the right moves to transform one string into another without interfering the prescribed limit.


### AppleAndOrange

  - [Solution](./AppleAndOrange.py)
  ### - Explanation: 
        In this code, First the values are read for the house and tree positions (s, t), the apple and orange tree positions (a, b), the number of apples and oranges (m, n), and the lists of apple and orange distances. Then, we count how many apples and oranges hit the house. If the distance from the tree (a or b) plus the fruit's distance (d) is within the range of the house (between s and t), we add 1 to the count. Finally, we get how many apples and oranges made it to the house

### AVeryBigSum

  - [Solution](./AVeryBigSum.py)
  ### - Explanation: 
        This code calculates the sum of all the numbers in a given list (ar). It initializes a variable total_sum to 0, then iterates through the list, adding each number to total_sum. Finally, it returns the total sum of all the numbers in the input list.

### beautifulDays

  - [Solution](./beautifulDays.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### BeautifulTriplets

  - [Solution](./BeautifulTriplets.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### betweenTwoSets

  - [Solution](./betweenTwoSets.py)
  ### - Explanation: 
        kla kla kli kli klu 

### BiggerIsGreater

  - [Solution](./BiggerIsGreater.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### BillDivision

  - [Solution](./BillDivision.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### BirthdayCakeCandles

  - [Solution](./BirthdayCakeCandles.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### BreakingTheRecords

  - [Solution](./BreakingTheRecords.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### ChocolateFeast

  - [Solution](./ChocolateFeast.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### circularArrayRotation

  - [Solution](./circularArrayRotation.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### climbingLeaderboard

  - [Solution](./climbingLeaderboard.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### CompareTheTriplets

  - [Solution](./CompareTheTriplets.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### cutTheSticks

  - [Solution](./cutTheSticks.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### designerPdfViewer

  - [Solution](./designerPdfViewer.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### DivisibleSumPairs

  - [Solution](./DivisibleSumPairs.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### Encryption

  - [Solution](./Encryption.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### EqualizeTheArray

  - [Solution](./EqualizeTheArray.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### extraLongFactorials

  - [Solution](./extraLongFactorials.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### FairRations

  - [Solution](./FairRations.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### FindDigits

  - [Solution](./FindDigits.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### flatlandSpaceStations

  - [Solution](./flatlandSpaceStations.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### formingMagicSquare

  - [Solution](./formingMagicSquare.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### gradingStudents

  - [Solution](./gradingStudents.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### HaloweenSale

  - [Solution](./HaloweenSale.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### jumpingOnClouds

  - [Solution](./jumpingOnClouds.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### LibraryFine

  - [Solution](./LibraryFine.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### LisasWorkbook

  - [Solution](./LisasWorkbook.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### MigratoryBirds

  - [Solution](./MigratoryBirds.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### MinimumDistances

  - [Solution](./MinimumDistances.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### MinMaxSum

  - [Solution](./MinMaxSum.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### ModifiedKaprekarNumbers

  - [Solution](./ModifiedKaprekarNumbers.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### NonDivisibleSubset

  - [Solution](./NonDivisibleSubset.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### NumberLineJumps

  - [Solution](./NumberLineJumps.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### organizingContainersofBalls

  - [Solution](./organizingContainersofBalls.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### PickingNumbers

  - [Solution](./PickingNumbers.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### PlusMinus

  - [Solution](./PlusMinus.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### QueensAttack2.py

  - [Solution](./QueensAttack2.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### MigratoryBirds

  - [Solution](./MigratoryBirds.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### MigratoryBirds

  - [Solution](./MigratoryBirds.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

### MigratoryBirds

  - [Solution](./MigratoryBirds.py)
  ### - Explanation: 
        kla kla kli kli klu l=klu

