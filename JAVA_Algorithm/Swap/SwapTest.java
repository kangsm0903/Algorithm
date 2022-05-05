// swap 함수가 호출될 때마다 몇번 째 호출인지 출력
package Swap;

public class SwapTest {
	static int count=0;
	
	static void swap(int arr[]) {
		int base=arr[0]; // base=10
		arr[0]=arr[1];
		arr[1]=base;
		count++;
		System.out.println(count+"번째 호출");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x=20;
		int y=10;
		
		int arr [] = {x,y};
		
		swap(arr);
		swap(arr);
		swap(arr);
		swap(arr);
	}

}
