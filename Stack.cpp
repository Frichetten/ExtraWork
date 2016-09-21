#include "Cup.cpp"
#include "Stack.h"
#include <iostream>
#include <string>

struct Node{
	int value;
	
	int getValue(){
		return value;
	}
};

int main(){
	Cup cu;
	int n = 5;
	cu.setValue(n);	
	
	Stack<Cup> st;
	st.push(cu);
	std::cout << st.getTop() -> getValue() << "\n";

	Stack<Node> ts;
	Node nu = {10};
	ts.push(nu);
	std::cout << ts.getTop() -> getValue() << "\n";
		
}

template <typename T>
Stack<T>::Stack(){
}

template <typename T>
void Stack<T>::push(T &obj){
	top = &obj;
}

template <typename T>
T* Stack<T>::getTop(){
	return top;
}


