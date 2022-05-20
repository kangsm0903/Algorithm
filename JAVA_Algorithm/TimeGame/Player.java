package JAVA_Algorithm.TimeGame;

import java.util.Calendar;

public class Player {
	String name;
	int SecondArray[]=new int[2]; // 배열 2개 생성
	
	public Player(String name) {
		this.name=name;
	}
	
	public void GameStart() {
		System.out.print(name+" 시작 <Enter>키>>");
	}
	
	public void Time(int num) { // 0번 배열에 첫 시간 값, 1번 배열에 다음 시간 값을 넣어줌
		Calendar cal = Calendar.getInstance();
		SecondArray[num]=cal.get(Calendar.SECOND);
		
		System.out.print("  현재 초 시간 = ");
		System.out.println(SecondArray[num]);
	}
	
	public int Result() {
		if (SecondArray[1]<SecondArray[0]) { // 0번째 인덱스가 더 크다면 1번 인덱스에 60을 더해줌
			SecondArray[1]+=60;
		}
		
		int result = SecondArray[1]-SecondArray[0];
		return result;
	}
}
