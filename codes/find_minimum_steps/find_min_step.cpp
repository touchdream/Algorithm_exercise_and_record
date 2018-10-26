#include <queue>
#include <iostream>
#include <stack>

struct QueueInfo
{
	QueueInfo(int _x = 0, int _y = 0, int _s = 0):x(_x), y(_y), state(_s) {}
	int x, y, state;
};
std::stack<QueueInfo> mStack;

int find_min_step(int x0, int y0, int target)
{
	mStack.push(QueueInfo(x0, y0, 0));
	QueueInfo temp;
	while(!mStack.empty())
	{
		temp = mStack.top();
		if (temp.x + temp.y == target)
		{
			return mStack.size();
		}
		if (temp.x + temp.y < target && temp.state != -1)
		{
			if (temp.state == 0)
			{
				mStack.top().state = 1;
				if (temp.x < temp.y)
				{
					mStack.push(QueueInfo(temp.x + temp.y, temp.y, 0));
				}
				else
				{
					mStack.push(QueueInfo(temp.x, temp.y + temp.x, 0));
				}
				
			}
			else if (temp.state == 1)
			{
				mStack.top().state = -1;
				if (temp.x < temp.y)
				{
					mStack.push(QueueInfo(temp.x , temp.x + temp.y, 0));
				}
				else
				{
					mStack.push(QueueInfo(temp.x + temp.y , temp.y, 0));
				}				
			}			
		}
		else
		{
			mStack.pop();
		}
	}
	return 0;
}

int main()
{
	//mStack.swap(std::stack<QueueInfo>());
	int result = find_min_step(1,1, 999999);
	std::cout<<result << std::endl;
	while(!mStack.empty())
	{
		std::cout<<"("<<mStack.top().x<<","<< mStack.top().y<<")-->"<<std::endl;
		mStack.pop();
	}
	return 0;
}