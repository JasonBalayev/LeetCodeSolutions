class Solution {
    public String pushDominoes(String dominoes) {
        char[] domArray=dominoes.toCharArray();
        int n=domArray.length;
        int[] forces=new int[n];
        int force=0;
        for (int i=0;i<n;i++){
            if(domArray[i]=='R'){
                force=n;
            }else if(domArray[i]=='L'){
                force=0;
            }else{
                force=Math.max(force-1,0);
            }
            forces[i]+=force;
        }
        force=0;
        for(int i=n-1;i>=0;i--){
            if(domArray[i]=='L'){
                force=n;
            }else if(domArray[i]=='R'){
                force=0;
            }else{
                force=Math.max(force-1,0);
            }
            forces[i]-=force;
        }
        StringBuilder res=new StringBuilder();
        for(int f:forces){
            if(f>0){
                res.append('R');
            }else if(f<0){
                res.append('L');
            }else{
                res.append('.');
            }
        }
        return res.toString();
    }
}

//QED
//Problem 838 (Medium Of Push Dominoes) - Jason Balayev (java)
