type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    private event:Map<string,Callback[]>=new Map();
    subscribe(eventName: string, callback: Callback): Subscription {
        if(!this.event.has(eventName)){
            this.event.set(eventName,[]);
        }
        let callbacks=this.event.get(eventName)!;
        callbacks.push(callback)
        return {
            unsubscribe: () => {
                let idx=callbacks.indexOf(callback);
                if(idx!==-1){
                    callbacks.splice(idx,1);
                }
            }
        };
    }
    
    emit(eventName: string, args: any[] = []): any[] {
        if(!this.event.has(eventName)){
            return[];
        }
        let callbacks=this.event.get(eventName)!;
        return callbacks.map(callback=>callback(...args));
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */

//QED
//Problem 2694 (Medium of Event Emitter) - Jason Balayev (typescript)