package JAVA_Algorithm.Beauty;

import java.util.Scanner;
import java.util.Vector;

public class ShapMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Vector <Shape> s = new Vector<Shape>();
		Shape input=null;
		
		System.out.println("그래픽 에디터 beauty을 실행합니다.");
		
		Scanner scan = new Scanner(System.in);
		
		while (true) {
			System.out.print("삽입(1), 삭제(2), 모두 보기(3), 종료(4)>>");
			int a = scan.nextInt();
			if(a==4) { // 종료
				System.out.println("beauty을 종료합니다.");
				break;
			}
			else if(a==1) { // 삽입
				System.out.print("Line(1), Rect(2), Circle(3)>>");
				int b = scan.nextInt();
				if (b==1) {
					input = new Line();
				} else if (b==2) {
					input = new Rect();
				} else if (b==3) {
					input = new Circle();
				}
				s.add(input);
			}
			else if(a==2) { // 삭제
				System.out.print("삭제할 도형의 위치>>");
				int c = scan.nextInt();
				try {
					s.remove(c); // try - catch 문으로 예외 잡기
				} catch (ArrayIndexOutOfBoundsException e) {
					System.out.println("삭제할 수 없습니다.");
				}
			} 
			else if(a==3) { // 모두 보기
				for(int i=0; i<s.size(); i++) {
					s.get(i).draw();
				}
			}
		}
		
		scan.close();
	}

}
