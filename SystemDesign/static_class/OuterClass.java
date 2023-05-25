package static_class;

public class OuterClass{
    private static String message = "hello";
    public static class StaticClass{
        public void print(){
            System.out.println("Static Class");
            System.out.println(message);
        }
    }
    public class InnerClass{
        public void printInnerClass() {
            System.out.println("Inner Class");
            System.out.println(message);
        }
    }
}