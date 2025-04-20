class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int,int> count;
        int res=0;
        for (int answer:answers){
            count[answer]++;
        }
        for (auto& pair:count){
            int groupSize=pair.first+1;
            int rabbitsSameAnswer=pair.second;
            int groups=(rabbitsSameAnswer+groupSize-1)/groupSize;
            res+=groups*groupSize;
        }
        return res;
    }
};

//QED
//Problem 781 (Medium of Rabbits In Forest) - Jason Balayev (cpp)