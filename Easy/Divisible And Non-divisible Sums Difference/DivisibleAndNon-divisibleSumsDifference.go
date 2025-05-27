func differenceOfSums(n int, m int) int {
    total:=n*(n+1)/2
    count:=n/m
    divisible:=m*count*(count+1)/2
    nonDivisible:=total-divisible
    return nonDivisible-divisible
}

//QED
//Problem 2894 (Easy of Divisible And Non-Divisible Sums Difference) - Jason Balayev (go)