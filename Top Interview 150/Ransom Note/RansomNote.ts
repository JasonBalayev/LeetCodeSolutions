function canConstruct(ransomNote: string, magazine: string): boolean {
    const letters:{[key:string]:number}={};
    for(const char of magazine){
        letters[char]=(letters[char]||0)+1;
    }
    for(const char of ransomNote){
        if(!letters[char]||letters[char]==0){
            return false;
        }
        letters[char]--;
    }
    return true;
};

//QED
//Problem 383 (Easy of Ransom Note) - Jason Balayev (typescript)