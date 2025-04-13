class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n==0) return true;
        int size = flowerbed.size();

        for (int i=0; i<size && n>0; i++) {
            if (flowerbed[i] ==0 &&
                (i==0 || flowerbed[i-1] == 0) &&
                (i==size-1 || flowerbed[i+1] == 0)) {
                    flowerbed[i] = 1;
                    n--;
                }
        }
        return n==0;
    }
};

//QED
//Problem 605 (Easy of Can Place Flowers) - Jason Balayev (cpp)