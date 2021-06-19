# dividing_string.py
import sys
from typing import List

sys.stdin = open('input/dividing_string')


def my():
    pass


TC = int(input())
for test_case in range(1, TC + 1):
    answer = my()
    print(answer)


'''
const triangularNumber = n => (n * (n + 1)) / 2;
const solution = (S) => {
  debugger
  // clever and performant way to test if we can split in 3 parts
  const intervals = S.split('a');
  if (intervals.length % 3 !== 1) {
    return 0;
  }
 
  // Because we need the same number of a's in each split we need to divide the
  // number of a's by 3 so we know where the next split starts
  const splitPoint = (intervals.length - 1) / 3;
  //test if the string contains "a" or not, if the splitPoint is 0 it means the
  //string don't have any "a" in it, so we just calculate the triangular number 
  //sequence
  if(splitPoint === 0) {
    return triangularNumber(intervals[0].length - 2);
  } else {
    // the split point is the interval between the sequence of a, if this
    // interval is non-empty it means that we can split the string in diferent
    // ways, take for example the string 'aaabaaabaaa' the split interval is
    // 3 becase we need 3 a's in each split, the value of the 3 split is 'b'
    // which is length 1, the + 1 represents the before the value, because now 
    // we have two ways of spliting this stirng
    // aaa|baaa.... and aaab|bbb, 2 posibilities lets say we had 'bb' then 
    // we would have 'bb'.length + 1, because
    // aaa|bbaaa... aaab|baaa... and aaabb|aaa..., the final part is just 
    // doing the same thing for the second part of the split and multipliting 
    // both because they can happen simutaneously
    return (intervals[splitPoint].length + 1) * 
          (intervals[2 * splitPoint].length + 1)
  }
}
'''
