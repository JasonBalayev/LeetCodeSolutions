func findWordsContaining(words []string, x byte) []int {
    var res []int
    for i,word:=range words{
        for j:=0;j<len(word);j++{
            if word[j]==x{
                res=append(res,i)
                break
            }
        }
    }
    return res
}

//QED
//Problem 2942 (Easy of Find Words Containing Character) - Jason Balayev (go)