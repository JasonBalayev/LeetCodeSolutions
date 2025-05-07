var TimeLimitedCache = function() {
    this.cache=new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currTime=Date.now();
    const entry=this.cache.get(key);
    const keyExists=entry&&entry.expiry>currTime;
    if(entry&&entry.timeoutId){
        clearTimeout(entry.timeoutId);
    }
    const timeoutId=setTimeout(()=>{
        this.cache.delete(key);
    },duration);
    this.cache.set(key,{
        value:value,
        expiry:currTime+duration,
        timeoutId:timeoutId
    });
    return Boolean(keyExists);
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const currTime=Date.now();
    const entry=this.cache.get(key);
    if(entry&&entry.expiry>currTime){
        return entry.value;
    }
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const currTime=Date.now();
    let count=0;
    for(const entry of this.cache.values()){
        if(entry.expiry>currTime){
            count++;
        }
    }
    return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

//QED
//Problem 2622 - (Medium of Cache With Time Limit) - Jason Balayev (javascript)