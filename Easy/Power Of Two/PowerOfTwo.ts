function isPowerOfTwo(n: number): boolean {
    return n > 0 && (n & (n - 1)) === 0;
};

//QED
//Problem 231 (Easy of Power of Two) - Jason Balayev (ts)   