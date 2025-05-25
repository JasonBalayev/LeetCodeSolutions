func longestPalindrome(words []string) int {
    wordCount:=make(map[string]int)
    for _,word:=range words{
        wordCount[word]++
    }
    len:=0
    center:=false
    for word,count:=range wordCount{
        if word[0]==word[1]{
            pairs:=count/2
            len+=pairs*4
            if count%2==1&&!center{
                len+=2
                center=true
            }
        }else{
            reverse:=string([]byte{word[1],word[0]})
            if word<reverse{
                reverseCount:=wordCount[reverse]
                pairs:=min(count,reverseCount)
                len+=pairs*4 
            }
        }
    }  
    return len
}
func min(a,b int)int{
    if a<b {
        return a
    }
    return b
}

//QED
//Problem 2131 (Medium of Longest Palindrome By Concatenating Two Letter Words) - Jason Balayev (go)