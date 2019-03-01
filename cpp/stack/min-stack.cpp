/**
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
 * **/

#include <stack>
#include <utility>
#include <algorithm>

using namespace std;

class MinStack
{
    stack<pair<int, int>> s;
    int minn;

  public:
    void push(int x)
    {
        if (s.empty())
        {
            s.push(pair<int, int>(x, x));
        }
        else
        {
            auto tmp = s.top();
            minn = min(tmp.second, x);
            s.push(pair<int, int>(x, minn));
        }
    }

    void pop()
    {
        s.pop();
    }

    int top()
    {
        return s.top().first;
    }

    int getMin()
    {
        return s.top().second;
    }
};