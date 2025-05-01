/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let fnCalled=false;
    let res;
    return function(...args){
        if (!fnCalled){
            fnCalled=true;
            res=fn(...args)
            return res;
        }
        return undefined;
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */

//QED
//Problem 2666 (Easy Allow One Function Call) - JavaScript