class Solution {
public:
    int findClosest(int x, int y, int z) {
        int dist_x=abs(x-z);
        int dist_y=abs(y-z);

        if (dist_x < dist_y) {
            return 1;
        } else if (dist_y < dist_x) {
            return 2;
        } else {
            return 0;
        }
    }
};

//QED
//Problem 3516 (Easy of Find Closest Person) - Jason Balayev (cpp)