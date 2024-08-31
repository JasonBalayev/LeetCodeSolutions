import java.util.HashMap;
import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanToInt = new HashMap<>();
        romanToInt.put('I',1);
        romanToInt.put('V',5);
        romanToInt.put('X',10);
        romanToInt.put('L',50);
        romanToInt.put('C',100);
        romanToInt.put('D',500);
        romanToInt.put('M',1000);

        int total = 0;
        int previousVal = 0;

        for (int i = s.length()-1; i>=0; i--) {
            int currentVal = romanToInt.get(s.charAt(i));
            if (currentVal<previousVal) {
                total -= currentVal;
            } else {
                total += currentVal;
            }
            previousVal = currentVal;
        }
        return total;
    }
}

//QED
//Problem 13 (Roman To Integer) - Jason Balayev (java)