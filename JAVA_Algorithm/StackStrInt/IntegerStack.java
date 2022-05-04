package StackStrInt;

public class IntegerStack implements Stack {
	int IntStack[];
	int top=0;
	
	public IntegerStack() {
		IntStack=new int[10];
	}
	
	@Override
	public int length() {
		// TODO Auto-generated method stub
		return IntStack.length;
	}

	@Override
	public Object pop() {
		// TODO Auto-generated method stub
		int item=IntStack[top];
		top--;
		return item;
	}

	@Override
	public boolean push(Object ob) {
		// TODO Auto-generated method stub
		if (top>IntStack.length) {
			return false;
		} else {
			IntStack[top]=(int)ob;
			top++;
			return true;
		}
	}

}