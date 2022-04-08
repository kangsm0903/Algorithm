import java.util.Scanner;

public class MainPhone {
    public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		System.out.print("인원수>>");
		int count = scan.nextInt();
		
		Phone p[]=new Phone[count]; // 레퍼런스 생성
		
		for (int i=0; i<count; i++) {
			System.out.print("이름과 전화번호(이름과 번호는 빈 칸없이 입력)>>");
			String name = scan.next(); // name
			String tel = scan.next();  // tel
			p[i]=new Phone(name,tel);  // 객체 생성
		}
		System.out.println("저장되었습니다...");
		
		System.out.print("검색할 이름>>"); //while문 돌아가기 전 출력
		String compare=scan.next();     //name과 비교할 입력 값
		while (!compare.equals("그만")) {// !equals로 두 문자열이 같지 않으면 while문이 계속 돌아감  
			for (int i=0; i<count; i++) {
				if (p[i].name.equals(compare)) { // compare과 name이 같은 것을 찾으면 출력 후 break
					System.out.println(p[i].name+"의 번호는 "+p[i].tel+"입니다.");
					break;
				} else if (i==count-1) { // i가 마지막 인덱스일 때까지 같은 것이 없으면 없다고 출력
					System.out.println(compare+" 이 없습니다.");
				}
			}
			System.out.print("검색할 이름>>"); // "그만"일 때까지 입력 받음
			compare=scan.next();
		}
		scan.close();
	}
}
