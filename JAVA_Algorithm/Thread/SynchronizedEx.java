package Thread;

public class SynchronizedEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ShareBoard board = new ShareBoard();
		StudentThread t1 = new StudentThread("add+", board);
		StudentThread2 t2 = new StudentThread2("sub-", board);
		//StudentThread2 t3 = new StudentThread2("sub--", board);
		
		t1.start();
		t2.start();
		//t3.start();
	}

}
