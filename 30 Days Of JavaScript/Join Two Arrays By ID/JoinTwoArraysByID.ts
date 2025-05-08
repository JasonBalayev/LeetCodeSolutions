type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    const map=new Map<number,ArrayType>();
    for(const item of arr1){
        map.set(item.id,{...item});
    }
    for(const item of arr2){
        if(map.has(item.id)){
            map.set(item.id,{...map.get(item.id),...item});
        }else{
            map.set(item.id,{...item});
        }
    }
    return Array.from(map.values()).sort((a,b)=>a.id-b.id);
};

//QED
//Problem 2722 (Medium of Join Two Arrays By ID) - Jason Balayev (typescript)