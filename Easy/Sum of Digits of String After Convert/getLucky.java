class Solution {
    public int getLucky(String s, int k) {
        StringBuilder numStr = new StringBuilder();

        for (char c : s.toCharArray()) {
            int position = c - 'a' +1;
            numStr.append(position);
        }
        int result = 0;

        for (char digit: numStr.toString().toCharArray()) {
            result += Character.getNumericValue(digit);
        }
        for (int i = 1; i < k; i++) {
            int newResult =0;
            while (result >0) {
                newResult += result %10;
                result /= 10;
            }
            result = newResult;
        }
        return result;
    }
}

//QED
//Problem 1945 (Daily Problem: Sum of Digits of String After Convert) - Jason Balayev (python)   