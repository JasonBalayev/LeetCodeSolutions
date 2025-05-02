/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return[...arr].sort((a,b)=>{
        return fn(a)-fn(b);
    })
};

//QED
//Problem 2724 (Easy Of Sort By) - Jason Balayev (javascript)
