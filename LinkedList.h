#ifndef LinkedList_H_
#define LinkedList_H_
#include <string>
class LinkedList
{
	public:
		struct Node{
			std::string name;
			LinkedList::Node* next;
		};

		LinkedList();
		~LinkedList();

		struct LinkedList::Node* head;
		struct LinkedList::Node* tail;

		void addNode(std::string name);
		void removeAtIndex(int i);
		int getSize();
		LinkedList::Node* getTail();
		LinkedList::Node* getAtIndex(int i);



	private:

};

#endif
