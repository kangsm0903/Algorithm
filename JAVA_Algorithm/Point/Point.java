package JAVA_Algorithm.Point;

import java.util.*;

public class Point {
	HashMap<String,Integer> dic = new HashMap<String,Integer>();
	
	public void PointMain() {
		Scanner scan = new Scanner(System.in);
		
		while(true) {
			System.out.print("이름과 포인트 입력>>");
			String name = scan.next();
			
			if(name.equals("그만")) {
				break;
			}
			else {
				int point = scan.nextInt();
				if(dic.get(name)==null) {
					dic.put(name, point);
				} else {
					dic.put(name, dic.get(name)+point); // point값 갱신
				}
				Set<String> nameKeys = dic.keySet();
				Iterator<String> it = nameKeys.iterator();
				
				while(it.hasNext()) {
					String tag=it.next();
					int score=dic.get(tag);
					System.out.print('('+tag+','+score+')');
				}
				System.out.println();
			}
		}
		scan.close();
	}
}

