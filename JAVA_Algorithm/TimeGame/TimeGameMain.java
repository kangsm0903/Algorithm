package TimeGame;

import java.util.Scanner;

public class TimeGameMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.println("10초에 가까운 사람이 이기는 게임입니다.");
		
		Player p1 = new Player("유재석"); // 객체 생성
		Player p2 = new Player("강호동");
		
		p1.GameStart();
		
		for(int i=0; i<2; i++) {
			if(scan.nextLine()=="") { // 배열 인덱스 접근
				p1.Time(i);
			}
			if(i==1) break;
			System.out.print("10초 예상 후 <Enter>키>>");
		}
		
		p2.GameStart();
		for(int i=0; i<2; i++) {
			if(scan.nextLine()=="") {
				p2.Time(i);
			}
			if(i==1) break;
			System.out.print("10초 예상 후 <Enter>키>>");
		}
		
		String winner;
		if (p1.Result()>p2.Result()) {
			winner=p1.name;
		} else winner=p2.name;
		
		System.out.println(p1.name+"의 결과 "+p1.Result()+", "+p2.name+"의 결과 "+p2.Result()+", 승자는 "+winner);
		
		scan.close();
	}

}
