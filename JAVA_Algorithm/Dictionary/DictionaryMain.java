package JAVA_Algorithm.Dictionary;

public class DictionaryMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dictionary dic = new Dictionary(10); // 10칸 생성하는 거 같음
		dic.put("황기태", "자바");
		dic.put("이재문", "파이썬");
		dic.put("이재문", "C++"); // 이재문의 값을 C++로 수정
		System.out.println("이재문의 값은 "+dic.get("이재문"));
		System.out.println("황기태의 값은 "+dic.get("황기태"));
		dic.delete("황기태"); // 황기태 아이템 삭제
		System.out.println("황기태의 값은 "+dic.get("황기태")); // 삭제된 아이템 접근
	}

}