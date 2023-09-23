"""
First you will be given a sequence of integers representing males. Afterwards you will be given another sequence of
integers representing females.
You have to start from the first female and try to match it with the last male.
 If their values are equal, you have to match them and remove both of them. Otherwise you should remove
only the female and decrease the value of the male by 2.
 If someone’s value is equal to or below 0, you should remove him/her from the records before trying to
match him/her with anybody.
 Special case ‐ if someone’s value divisible by 25 without remainder, you should remove him/her and the
next person of the same gender before trying to match them with anybody.
You need to stop matching people when you have no more females or males.
Input
 On the first line of input you will receive the integers, representing the males, separated by a single space.
 On the second line of input you will receive the integers, representing the females, separated by a single
space.
Output
 On the first line of output ‐ print the number of successful matches:
o "Matches: {matchesCount}"
 On the second line ‐ print all males left:
o If there are no males: "Males left: none"
o If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
 On the third line ‐ print all females left:
o If there are no females: "Females left: none"
o If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"
Constraints
 All of the given numbers will be valid integers in the range [‐100, 100].

Input                   Output                      Comment
4 5 7 3 6 9 12
12 9 6 1
                        Matches: 3
                        Males left: 1, 7, 5, 4
                        Females left: none
                                                    The first pair is the first female with value of 12 and the last male of
                                                    value 12, their values are equal, so we match them, therefore ‐
                                                    remove them from the records. Then we have two more matches
                                                    (9 == 9 and 6 == 6). But the value of the next male is 3 and the value
                                                    of the next female is 1, it's not a match and we remove the female
                                                    and reduce the male’s value by 2.Then, we print the desired
                                                    output.
3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4
                        Matches: 4
                        Males left: none
                        Females left: 15, 13, 4
"""