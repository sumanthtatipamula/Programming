package static_class;

import static_class.OuterClass;

public class Program {
    public static void main(String[] args) {
        OuterClass.StaticClass staticClass = new OuterClass.StaticClass();
        staticClass.print();
        OuterClass outer = new OuterClass();
        OuterClass.InnerClass inner = outer.new InnerClass();
        inner.printInnerClass();
    }
}
