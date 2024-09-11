public class main {
    public static void main(String args[]) {
        String v = greet("divya");
        System.out.println(v);

    }

    static String greet(String name) {
        String a = "how are you?" + name;
        return a;
    }

}
