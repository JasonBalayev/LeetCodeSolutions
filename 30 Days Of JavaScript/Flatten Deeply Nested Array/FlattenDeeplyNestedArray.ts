type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    let res:MultiDimensionalArray=[];
    for(const item of arr){
        if(Array.isArray(item)&&n>0){
            res.push(...flat(item,n-1));
        }else{
            res.push(item);
        }
    }
    return res;
};

//QED
//Problem 2625 (Medium of Flatten Deeply Nested Array) - Jason Balayev (typescript)