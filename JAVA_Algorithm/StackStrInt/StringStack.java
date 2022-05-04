package StackStrInt;

public class StringStack implements Stack {
	String Strstack[];
	int top=0;
	
	public StringStack() {
		Strstack = new String[10];
	}
	
	@Override
	public int length() {
		// TODO Auto-generated method stub
		return Strstack.length;
	}

	@Override
	public Object pop() {
		// TODO Auto-generated method stub
		String item=Strstack[top-1];
		Strstack[top-1]=null;
		top--;
		return item;
	}

	@Override
	public boolean push(Object ob) {
		// TODO Auto-generated method stub
		if (top>Strstack.length) {
			return false; // full stack
		} else {
			Strstack[top]=(String)ob; // 삽입 후 top++
			top++;
			return true;
		}
	}

}
