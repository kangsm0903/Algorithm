package Thread;
// 공유 데이터 sum
public class ShareBoard {
	private int sum=0;
	int n;
	synchronized public void add() {
		if (sum>=100) {
			try {
				wait();
			}catch(InterruptedException e) {return;}
		}
		n=sum;
		n+=10;
		sum=n;
		System.out.println(Thread.currentThread().getName()+":"+sum);
		notify(); // 대기 중인 thread에 끝났음을 알림
	}
	
	synchronized public void sub() {
		if (sum<=0) {
			try {
				wait(); // 기다림
			} catch(InterruptedException e) {return;}
		}
		n=sum;
		n-=10;
		sum=n;
		System.out.println(Thread.currentThread().getName()+":"+sum);
		notify();
	}
	
	int getSum() {return sum;}
}
