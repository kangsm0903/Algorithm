package Schedulemanage;

import java.util.Scanner;

public class NewMonthSchedule {
	// 생성자
	private Scanner scan = new Scanner(System.in);
	int num;
	int date;
	String todo;
	private Day d[]; // 전역변수로 설정해주어야 다른 메소드에서도 사용가능
	
	public NewMonthSchedule(int day) { // 객체 생성 생성자
		d = new Day[day+1]; // 객체 레퍼런스 선언
		
		for (int i=0; i<d.length; i++) {
			d[i] = new Day();
		}
	}
	
	public void input() {
		System.out.print("날짜(1~30)?");
		date = scan.nextInt();
		
		if (date<1 || date>30) { // 범위 밖의 숫자를 받으면 경고 문구 날리기
			System.out.println("1~30까지의 숫자를 입력해주세요.");
		} else { // 날짜와 할 일을 입력받고 저장
			System.out.print("할일(빈칸없이 입력)?");
			todo = scan.next();
			d[date].set(todo);
		}
	}
	
	public void view() {
		System.out.print("날짜(1~30)");
		date = scan.nextInt();
		
		if (date<1 || date>30) { // 날짜를 입력받고 범위 밖이면 경고
			System.out.println("1~30까지의 숫자를 입력해주세요.");
		}
		else if (d[date].get()==null) { // 할 일이 null일 때,없을 땐 준비된 메시지 출력
			System.out.println(date+"일의 할 일은 없습니다.");
		} 
		else {System.out.println(date+"일의 할 일은 "+d[date].get()+"입니다.");} // 할일이 있으면 그거대로 출력
	}
	
	public void finish() {
		System.out.println("프로그램을 종료합니다.");
	}
	
	public void run() {
		System.out.println("이번 달 스케쥴 관리 프로그램.");
		while(true) {
			System.out.print("할일(입력:1, 보기:2, 끝내기:3) >>");
			num = scan.nextInt();
			if (num==1) {
				input();
				System.out.println();
			}
			else if (num==2) {
				view();
				System.out.println();
			}
			else if (num==3) {
				finish();
				break;
			}
			else {System.out.println("1~3의 숫자를 입력해주세요.");}
		}
	}
}
