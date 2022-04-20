package Schedulemanage;

public class Day {
    private String work;
	
	public void day() {
		work=null;
	}
	
	public void set(String work) { // 할 일 갱신 원래는 setWork
		this.work=work;
	}
	
	public String get() { // 할 일 가져오기 원래는 getWork
		return work;
	}
	
	public void show() { // 
		if(work==null) System.out.println("없습니다.");
		else System.out.println(work+"입니다.");
	}
}
