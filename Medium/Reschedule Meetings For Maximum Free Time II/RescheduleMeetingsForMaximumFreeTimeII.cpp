class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        using ll=long long;
        int n=startTime.size();
        if(n== 0){
            return eventTime;
        }
        vector<ll>gaps;
        gaps.push_back(startTime[0]);
        for (int i=0;i<n-1;++i){
            gaps.push_back(static_cast<ll>(startTime[i+1])-endTime[i]);
        }
        gaps.push_back(static_cast<ll>(eventTime)-endTime[n-1]);
        ll max_time=0;
        for (ll gap:gaps) {
            max_time=max(max_time,gap);
        }
        vector<pair<ll,ll>>pref(n+2,{-1,-1});
        for (int i=0;i<=n;++i){
            pref[i+1]=pref[i];
            ll curr=gaps[i];
            if(curr>pref[i+1].first){
                pref[i+1].second=pref[i+1].first;
                pref[i+1].first=curr;
            }else if(curr>pref[i+1].second){
                pref[i+1].second=curr;
            }
        }
        vector<pair<ll,ll>>suff(n+2,{-1,-1});
        for (int i=n;i>=0;--i){
            suff[i]=suff[i+1];
            ll curr=gaps[i];
            if(curr>suff[i].first){
                suff[i].second=suff[i].first;
                suff[i].first=curr;
            }else if(curr>suff[i].second){
                suff[i].second=curr;
            }
        }
        for(int i=0;i<n;++i){
            ll duration=static_cast<ll>(endTime[i]) - startTime[i];
            ll start_boundary=(i==0?0:static_cast<ll>(endTime[i-1]));
            ll end_boundary=(i==n-1?static_cast<ll>(eventTime):static_cast<ll>(startTime[i+1]));
            ll merged_gap=end_boundary-start_boundary;
            pair<ll,ll>p_stat=pref[i];
            pair<ll,ll>s_stat=suff[i+2];
            ll other_max=max(p_stat.first,s_stat.first);
            ll other_smax=max({min(p_stat.first, s_stat.first),p_stat.second,s_stat.second});
            ll s_max=max(merged_gap,other_max);
            ll s_smax=max(min(merged_gap,other_max),other_smax);
            if(s_smax>=duration){
                max_time=max(max_time,s_max);
            }else if(s_max>=duration){
                max_time=max(max_time,max(s_max-duration,s_smax));
            }
        }
        return static_cast<int>(max_time);
    }
};

//QED
//Problem 3440 (Medium of Reschedule Meetings For Maximum Free Time II) - Jason Balayev (cpp)