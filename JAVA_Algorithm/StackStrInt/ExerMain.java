// stack 인터페이스를 구현한 StringStack, IntegerStack
// 실행하는 main 메소드
package StackStrInt;

import java.util.Scanner;

public class ExerMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		Stack stack = new StringStack(); // 스택 생성
		
		System.out.println("Please input 10 elements.");
		for(int i=0; i<stack.length(); i++) {
			if(stack.push(scan.next())==false) break; // 옴팡지게 push
		}
		
		System.out.println("Full stack. Now start 'pop'");
		for(int i=0; i<stack.length(); i++) {
			System.out.println(stack.pop() +" ");
		}
		
		scan.close();
	}

}