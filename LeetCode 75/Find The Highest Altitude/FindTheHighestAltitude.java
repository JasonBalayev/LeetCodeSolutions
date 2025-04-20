class Solution {
    public int largestAltitude(int[] gain) {
        int curr=0;
        int max=0;
        for (int g:gain){
            curr+=g;
            max=Math.max(max,curr);
        }
        return max;
    }
}

//QED
//Problem 1732 (Easy of Find The Highest Altitude) - Jason Balayev (java)