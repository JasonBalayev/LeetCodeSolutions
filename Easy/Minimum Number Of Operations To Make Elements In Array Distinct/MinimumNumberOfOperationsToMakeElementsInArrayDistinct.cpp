class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int op = 0;
        vector<int> remaining = nums;
        
        while (!remaining.empty()) {
            unordered_set<int> uniqueElements(remaining.begin(), remaining.end());
            if (uniqueElements.size() == remaining.size()) {
                return op; 
            }
            int elementsToRemove = min(3, static_cast<int>(remaining.size()));
            remaining.erase(remaining.begin(), remaining.begin() + elementsToRemove);
            op++;
        }
        return op;
    }       
};

//QED
//Problem 3396 (Easy of Minimum Number of Operations to Make Elements in Array Distinct) - Jason Balayev (cpp)