/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((res,item)=>{
        const key=fn(item);
        if(!res[key]){
            res[key]=[];
        }
        res[key].push(item);
        return res;
    }, {});
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

//QED
//Problem 2631 (Medium of Group By) - Jason Balayev (javascript)