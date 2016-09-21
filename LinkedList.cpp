#include "LinkedList.h"
#include <iostream>
#include <string>

LinkedList::LinkedList(){
	head = NULL;
	tail = NULL;
}

LinkedList::~LinkedList(){
	LinkedList::Node* temp,*tempNxt;
	temp = tail;
	tempNxt = tail;
	while(tempNxt != NULL){
		temp = temp->next;
		delete tempNxt;
		tempNxt = temp;
	}
}

void LinkedList::addNode(std::string name){
	if (head == NULL){
		LinkedList::Node* node = new Node();
		head = node;
		node->name = name;
		node->next = NULL;
		tail = head;
	}
	else{
		LinkedList::Node* node = new Node();
		node->name = name;	
		node->next = tail;
		tail = node;
	}
}

int LinkedList::getSize(){
	int toReturn = 0;
	LinkedList::Node* toNext = tail;
	while(toNext != NULL){
		toReturn++;
		toNext = toNext->next;
	}	
	return toReturn;
}

void LinkedList::removeAtIndex(int i){
	int to = (this->getSize() -i)-1;
	LinkedList::Node* hold = tail;
	LinkedList::Node* temp = NULL;
	for(int i = 1; i < to; i++){
		hold = hold->next;
	}
	if (to !=0){
		temp = hold->next;
		hold->next = temp->next;
		delete temp;
	}
	else{
		temp = hold;
		tail = temp->next;
		delete temp;
	}
}

LinkedList::Node* LinkedList::getAtIndex(int i){
	LinkedList::Node* toReturn = tail;
	int to = (this->getSize() - i);
	for(int i = 1; i < to; i++){
		toReturn = toReturn->next;	
	}
	return toReturn;
}

LinkedList::Node* LinkedList::getTail(){
	return tail;
}


