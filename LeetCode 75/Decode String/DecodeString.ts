function decodeString(s: string): string {
    const table=[];
    for(let char of s){
        if(char!==']'){
            table.push(char);
        }else{
            let curr=table.pop();
            let str=''
            while(curr!=='['){
                str=curr+str
                curr=table.pop();
            }
            let num=''
            while(table.length>0&&!isNaN(parseInt(table[table.length-1]))){
                num=table.pop()+num;
            }
            table.push(str.repeat(Number(num)));
        }
    }
    return table.join('');
};

//QED
//Problem 394 (Medium of Decode String) - Jason Balayev (typescript)