package Thread;

public class StudentThread2 extends Thread{
	private ShareBoard board;
	public StudentThread2(String name, ShareBoard board) {
		super(name);
		this.board=board;
	}
	
	@Override
	public void run() {
//		for(int i=0; i<10; i++) {
			while(true) {
				board.sub();
				try {
					sleep(105);
				}catch(InterruptedException e) {return;}
			}
		}	
	// }
}
