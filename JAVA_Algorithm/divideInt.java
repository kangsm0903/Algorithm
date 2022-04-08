public class divideInt {

	public static void main(String[] args) {
		int n=567;
		int share;
		
		for (int i=2; i>=0; i--) {
			share = n / (int)Math.pow(10, i); // 10의 n으로 나누어서 백,십,일의 자리 분리
			n=n % (int)Math.pow(10, i);
			if (i==2) {
				System.out.println("백의자리="+share);
			} 
			else if (i==1) {
				System.out.println("십의자리="+share);
			}
			else {
				System.out.println("일의자리="+share);
			}
		}
	}

}