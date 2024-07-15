[solution](./inwords.py)

[leetcode problem](https://leetcode.com/problems/integer-to-english-words/description)

[leetcode submission](https://leetcode.com/problems/integer-to-english-words/submissions/1321134008?submissionId=1321134008)


## Workflow
1. create dictionary mappings for modular naming
2. convert the number into string
3. split the number at every 3rd digit from the right till we reach the end
4. create a function to convert 3 digit numbers to words using the mappings
5. keep applying the 3 digit number conversion function to all sets of 3 digits and add *billion*, *million*, etc as needed
6. strip extra spaces etc

## Explanation
things to note:
* the constraints of this problem say that the number is less than 2^31^-1 (= 2,147,483,647). so, the code will work only upto billions (999,999,999,999) and not further

### convert number to properly partitioned array
`num_to_str_arr(num: int) -> List[str]`
1. takes the number and reverses it first (since the 3 digit split starts from rhs to lhs)
2. iterate with a step of 3 and store the result in a list after reversing it. why reverse? we reversed the number first. so while taking the digits, we need to re-reverse them tog et back the actual order. example, 123456 when first reversed is 654321. when we split with a step 3, we get 654,321. after we reverse the numbers, we get 456 and 123
3. now, the last set will be ignored in the above step. so we write an extra line to include the last part also. this occurs because say, we have a 7 digit number. we loop by steps of 3 from 0. so we get 0-3, 3-6 and the 6-9 but since we exceeded the length, we stop at 7 and the last set (in this 7 digit example, the millions part) is ignored. so, we use `%` and some basic math to get the remaining digits. if the last set is a full 3 digit set (length is amultiple of 3, we need to consider a small change). i cant explain how i came at that exact calculation for the last set. i kept passing al lengths of numbers and made changes according to how the test case failed
4. now that we added all parts of the number to the array, we have an array of reverse order since we reversed the string initially. example, 2147483647. step 2 initially will give 746, 384, 741, and on individual reversal, we have the list `[647, 483, 147]`. then from step 3, we add 2 to the end of the list. now the list is `[647,483,147,2]`. this step will revrse the list and return it so that we get the perfect split `[2, 147, 483, 647]`. for convenience, quotes have been skipped, these lists are all string lists

### convert 3 digit partitions into words
`to_words_3_dig(num: str) -> str`
1. we extract the units, tens and hundreds places as individual digits using `//` and `%` operators
2. for hundreds, we take the word form of hundreds place digit from the mapping and append ' Hundred' to it or leave blank if hundreds place is 0
3. for tens place we have 3 possibilities
    1. teens - we club the units place digit and get the mapping from the teens dictionary
    2. 20-50 and 80 - for twnety to fifty and eighty, we need to use mappings from a tens dicntionary
    3. after 50, we just need the number and append 'ty'. example - 50 is not five-ty and 80 is not eight-ty but 60, 70 etc are six-ty, seven-ty, etc
    * this is not a mandatory step. to avoid one conditional, all tens places can be part of the mapping witout using `+ 'ty'` logic
4. if it is not a teen, we take and get the word of the units digit seperately
5. join hundreds, tens and units and return it

### convert the entire number to words
`numberToWords(number: int) -> str`
1. add an edge case for 
2. convert the number into partitioned string array using previous method
3. if the list is 4 elements long, we have a billions place. make the first part into words and add 'billions', second part to words and add 'millions' and so on. if the list is 3 elements long, we have a millions place. make the first part to words and add 'millions' and so on. similarly for 2 elements (hundred thousands) and just 3 digit numbers
4. append all the partition names to one string and that will be te final output. in case extra space were added to end of string due to need of adding spaces between places, `throw in a strip()` before returning

## Estimted Time Complexity

**O(n)**

converting to array takes n/3 + 1 steps (overall O(n))

converting 3 digit sets to words takes 4 steps and 3 conditionals (overall constant time)

converting the entire number to words uses the 3-digit conversion function approximately n/3 times - we did not loop over the list elements since we used 4 `if` clauses. however, in a general and ideal approach, we have to go through the list elements iteratively (overall O(n))

## References

