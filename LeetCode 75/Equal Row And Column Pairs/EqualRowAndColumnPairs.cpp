class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n=grid.size();
        int count=0;
        map<vector<int>,int> rowMap;
        for (int i=0; i<n; i++){
            rowMap[grid[i]]++;
        }
        for (int j=0; j<n; j++){
            vector<int> col;
            for (int i=0; i<n; i++){
                col.push_back(grid[i][j]);
            }
            if (rowMap.find(col)!=rowMap.end()){
                count+=rowMap[col];
            }
        }
        return count;
    }
};

//QED
//Problem 2352 (Medium of Equal Row And Column Pairs) - Jason Balayev (cpp)
