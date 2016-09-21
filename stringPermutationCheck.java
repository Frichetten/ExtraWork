import java.util.ArrayList;
import java.util.Objects;


public class Driver {
	
	static ArrayList<String> arr = new ArrayList<String>();
	
	public static void main(String[] args) {
		permutation("mathisfun");
		System.out.println(arr.size());
		
		int num = 0;
		for(int i =0; i < arr.size(); i++){
			if (arr.get(i).matches("(?i).*is.*") && arr.get(i).matches("(?i).*fun.*") && arr.get(i).matches("(?i).*math.*")){
				num++;
			}
		}
		System.out.println(num);
		
	}
	
	public static void permutation(String str) { 
	    permutation("", str); 
	}

	private static void permutation(String prefix, String str) {
	    int n = str.length();
	    if (n == 0) addArr(prefix);
	    else {
	        for (int i = 0; i < n; i++)
	            permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i+1, n));
	    }
	}
	
	static void addArr(String s){
		arr.add(s);
	}

}
