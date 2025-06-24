function isPowerOfFour(n: number): boolean {
    return n>0&&(n&(n-1))==0&&(n&0x55555555)!==0;
};

//QED
//Problem 342 (Easy of Power of Four) - Jason Balayev (ts) 