class Foo {
    private boolean firstDone = false;
    private boolean secondDone = false;
    private final Object lock = new Object();

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        synchronized (lock) {
            firstDone = true;
            lock.notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        synchronized (lock) {
            while (!firstDone) {
                lock.wait();
            }
        }
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        synchronized (lock) {
            secondDone = true;
            lock.notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        synchronized (lock) {
            while (!secondDone) {
                lock.wait();
            }
        }
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}

//QED
//Problem 1114 (Easy Of Print In Order) - Jason Balayev (java)