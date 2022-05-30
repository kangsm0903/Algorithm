import java.io.*;
import java.util.HashMap;
import java.util.Scanner;

public class Phone {
	HashMap<String,String> dic = new HashMap<String,String>();
	
	public Phone() {}
	
	public void ReadNumber() {
		try {
			FileInputStream fin = new FileInputStream("C:\\temp\\phone.txt");
			InputStreamReader in = new InputStreamReader(fin, "UTF-8"); 
			Scanner scan = new Scanner(in);
			while(scan.hasNext()) { // 다음이 있다면
				String name = scan.next();
				String number= scan.next();
				dic.put(name, number);
			}
			scan.close();
			fin.close();
			in.close();
		} catch (IOException e) {
			System.out.println("입출력 오류");
		}
		System.out.println("총 7개의 전화번호를 읽었습니다.");
		getNumber();
	}
	
	public void getNumber() {
		Scanner scan = new Scanner(System.in);
		while(true) {
			System.out.print("이름>>");
			String name=scan.next();
			if(name.equals("그만")) {
				break;
			} else if(dic.get(name)==null) {
				System.out.println("찾는 이름이 없습니다");
			} else {
				System.out.println(dic.get(name));
			}
		}
		scan.close();
	}
}
