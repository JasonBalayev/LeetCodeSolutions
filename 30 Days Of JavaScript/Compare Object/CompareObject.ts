type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    //Arrays
    if(Array.isArray(obj)){
        const res: JSONValue[]=[];
        for(const item of obj){
            if(Boolean(item)){
                if(typeof item==='object'&&item!==null){
                    res.push(compactObject(item as Obj));
                }else{
                    res.push(item);
                }
            }
        }
        return res;
    }else{ //Objects
        const res:Record<string,JSONValue>={};
        for(const key in obj){
            const val=obj[key];
            if(Boolean(val)){
                if(typeof val==='object'&&val!==null){
                    res[key]=compactObject(val as Obj);
                }else{
                    res[key]=val;
                }
            }
        }
        return res;
    }
}; 

//QED
//Problem 2705 (Medium of Compare Object) - Jason Balayev (typescript)