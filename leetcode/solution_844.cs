// FAIL TO SOLVE



/*
first brute force approach
convert s and t following the instructions and then compare the two converted strings to see if they are equal.
The two converted strings will take up O(m + n) space complexity where m and n are length of the converted strings each.

now o(n) time complexity and O(1) space complexity approach
Since it's a O(1) space complexity solution, I will probably need to use some limited number of pointers.

    |  
s: abk##c

    |  
t: ad##ck



s: ab#
t: aca#

s: ac###a
t: ab###d

steps
1: are they equal? (a == a)
yes
2: are they equal? (b == d)
no
3: do they have a following back space character?
only t does.
4: does s have two  following back sapce characters?
yes
5: then move the pointers forward by one character
6: one pointer is pointing to null, and another is not, then return false


when condition is false, iterate until both the faults become 0 again.
if we exit the loop withougt making the condition back to true, return false;
*/


public class Solution {
    public bool BackspaceCompare(string s, string t) {
        var sPointer = 0;
        var tPointer = 0;
        var sFault = 0;
        var tFault = 0;
        var condition = true;
        
        
        while (sPointer < s.Length && tPointer < t.Length)
        {
            var sChar = s[sPointer];
            var tChar = t[tPointer];
            
            if (condition)
            {
                if (sChar == tChar)
                {
                    sPointer++;
                    tPointer++;
                    continue;
                }
                
                condition = false;
                sFault++;
                tFault++;
                sPointer++;
                tPointer++;
                continue;
            }
            
            if (sFault > 0)
            {
                if (sChar == '#')
                {
                    sFault--;
                }
                else
                {
                    sFault++;
                }
                sPointer++;
            }
            
            if (tFault > 0)
            {
                if(tChar == '#')
                {
                    tFault--;
                }
                else
                {
                    tFault++;
                }
                tPointer++;
            }
            
            if (sFault == 0 && tFault == 0)
            {
                condition = true;
            }
            
        }
        
        if (sPointer < s.Length || tPointer < t.Length)
        {
            return false;
        }
        
        return condition;
    }
}