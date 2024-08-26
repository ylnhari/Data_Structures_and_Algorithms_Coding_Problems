# Problem
https://leetcode.com/problems/print-in-order/description/

# Intuition
- Synchronization: The problem requires ensuring that the three methods are executed in a specific order: first, second, and third. To achieve this, we need a mechanism to synchronize the execution of these methods.
- Locks: Using locks is a common approach to synchronize concurrent execution in multi-threaded environments. By acquiring and releasing locks, we can control the order in which methods are executed.

# Approach
- Initialize Locks: Create two locks, `lock_second` and `lock_third`.
- Acquire Locks: Acquire both locks in the constructor to ensure that the `first` method is executed before `second` and `third`.
- Release Locks: In the `first` method, release `lock_second` to allow `second` to proceed. In the `second` method, release `lock_third` to allow `third` to proceed.

# Complexity
- Time Complexity: `O(1)` for each method. The operations involving locks are typically constant time operations.
- Space Complexity: `O(1)`. The space used for the locks is constant.


# Code
```python3 []
from threading import Lock
class Foo:
    def __init__(self):
        self.lock_second = Lock()
        self.lock_third = Lock()

        self.lock_second.acquire()
        self.lock_third.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock_second.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock_second.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock_third.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock_third.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
```
