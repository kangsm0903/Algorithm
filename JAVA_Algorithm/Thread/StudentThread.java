package Thread;

public class StudentThread extends Thread{
	private ShareBoard board;
	public StudentThread(String name, ShareBoard board) { // board==공유객체
		super(name);
		this.board=board;
	}
	
	@Override
	public void run() {
//		for(int i=0; i<10; i++) {
			while(true) {
				board.add();
				try {
					sleep(100);
				} catch (InterruptedException e) {return;}
			}
		}		
//	}
}
