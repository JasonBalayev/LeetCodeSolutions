class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n=startTime.size();
        vector<long long> duration(n);
        for (int i= 0;i<n;++i) {
            duration[i]=(long long)endTime[i]-startTime[i];
        }
        vector<long long>pref(n+1,0);
        for(int i=0;i<n;++i){
            pref[i+1]=pref[i]+duration[i];
        }
        long long max_time=0;
        vector<long long>A(n),B(n);
        for(int i=0;i<n;++i) {
            A[i]=startTime[i]-pref[i];
            B[i]=-endTime[i]+pref[i+1];
        }
        deque<int>dq;
        for (int j=0;j<n;++j){
            if(j>0){
                while(!dq.empty()&&B[dq.back()]<B[j-1]){
                    dq.pop_back();
                }
                dq.push_back(j-1);
            }
            if(!dq.empty()&&dq.front()<j-k-1) {
                dq.pop_front();
            }
            if(!dq.empty()){
                max_time=max(max_time,A[j]+B[dq.front()]);
            }
        }
        for(int j=0;j<=k&&j<n;++j) {
            max_time=max(max_time,A[j]);
        }
        long long end=(long long)eventTime-pref[n];
        for (int i=n-1;i>=0&&(n-i)<=k;--i){
            long long curr=end+(i>0?B[i-1]:0);
            if(i==0){
                curr=(long long)eventTime-pref[n];
            }
            max_time=max(max_time,curr);
        }
        return(int)max_time;
    }
};

//QED
//Problem 3439 (Medium of Reschedule Meetings For Maximum Free Time I) - Jason Balayev (cpp)