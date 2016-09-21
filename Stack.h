#ifndef STACK_H_
#define STACK_H_

template <typename T>
class Stack{
	public:
		Stack();	
		void push(T &obj);
		T* getTop();
	private:
		T* top;
};

#endif
