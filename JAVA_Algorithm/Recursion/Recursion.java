package Recursion;
// x의 n제곱을 계산
import java.util.Scanner;

public class Recursion {
	public int power(int x, int n) {
		if (n==0) {
			return 1;
		} else {
			return power(x,n-1)*x;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int x=scan.nextInt();
		int n=scan.nextInt();
		
		Recursion r1= new Recursion();
		
		System.out.println(r1.power(x,n));
		
		scan.close();
	}

}
