class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int rows=maze.size();
        int cols=maze[0].size();
        int dr[]={-1,0,1,0};
        int dc[]={0,1,0,-1};
        queue<pair<pair<int,int>,int>>q;
        q.push({{entrance[0],entrance[1]},0});
        maze[entrance[0]][entrance[1]]='+';
        while(!q.empty()){
            int r=q.front().first.first;
            int c=q.front().first.second;
            int steps=q.front().second;
            q.pop();
            for(int i=0;i<4;i++){
                int nr=r+dr[i];
                int nc=c+dc[i];
                if(nr>=0&&nr<rows&&nc>=0&&nc<cols&&maze[nr][nc]=='.'){
                    if(nr==0||nr==rows-1||nc==0||nc==cols-1){
                        return steps+1;
                    }
                    maze[nr][nc]='+';
                    q.push({{nr,nc},steps+1});
                }
            }
        }
        return -1;
    }
};

//QED
//Problem 1926 - (Medium of Nearest Exit From Entrance In Maze) - Jason Balayev (cpp)